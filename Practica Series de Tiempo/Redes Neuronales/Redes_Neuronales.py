import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler

# Cargar los datos
data = pd.read_csv("C:/Users/dani_/Desktop/Prueba ST/NU Historical Data.csv")
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# Plot the original price series data
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Price'], color='blue', label='Original Data')
plt.title('Original Series of NU Holdings Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# Suponiendo que la columna de precios es 'Price'
serie = data['Price'].values.reshape(-1, 1)

# Normalizar los datos entre 0 y 1
scaler = MinMaxScaler(feature_range=(0, 1))
serie_norm = scaler.fit_transform(serie)

# Dividir los datos en entrenamiento y prueba
def crear_secuencias(data, pasos):
    X, Y = [], []
    for i in range(len(data)-pasos-1):
        X.append(data[i:(i+pasos), 0])
        Y.append(data[i + pasos, 0])
    return np.array(X), np.array(Y)

train_size = int(len(serie_norm) * 0.8)
train_data = serie_norm[:train_size]
test_data = serie_norm[train_size:]

pasos = 10
X_train, Y_train = crear_secuencias(train_data, pasos)
X_test, Y_test = crear_secuencias(test_data, pasos)

# Definiendo el modelo

model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(pasos, 1)),
    Dropout(0.2),
    LSTM(50, return_sequences=False),
    Dropout(0.2),
    Dense(1)
])

# Compilar el modelo
model.compile(optimizer='adam', loss='mean_squared_error')

# Entrenar el modelo
model.compile(optimizer='adam', loss='mean_squared_error')

# Ahora, entrenamos el modelo

history = model.fit(X_train, Y_train, epochs=100, batch_size=32)

# Haciendo predicciones
train_predict = model.predict(X_train)

# Deshacer la normalización
train_predict = scaler.inverse_transform(train_predict)
real_values = scaler.inverse_transform(Y_train.reshape(-1, 1))

# Visualizar los resultados
plt.plot(real_values, color='red', label='Precio real')
plt.plot(train_predict, color='blue', label='Precio predicho')
plt.title('Predicción de precios')
plt.xlabel('Tiempo')
plt.ylabel('Precio')
plt.legend()
plt.show()


# Evaluando el modelo
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(real_values, train_predict)
print('Error cuadrático medio:', mse)
mae = np.mean(np.abs(real_values - train_predict))
print('Error absoluto medio:', mae)