library(dplyr)
library(ggplot2)
library(readxl)
library(HDInterval)
library(rstan)
Microdatos_encuesta_de_percepción_MCV_y_diccionario_de_datos <- read_excel("Microdatos encuesta de percepción MCV y diccionario de datos.xlsx")
View(Microdatos_encuesta_de_percepción_MCV_y_diccionario_de_datos)
datos <- Microdatos_encuesta_de_percepción_MCV_y_diccionario_de_datos[,c(10,11,13,16,557)]

# 10: Comuna, 11: Sexo, 13: Edad, 16: Estrato, 557: Vulnerabilidad

Comuna <- datos$Q6
Sexo <- datos$CS1
Edad <- datos$CS2
Estrato <- datos$CCS2
Vulnerabilidad <- datos$RVE5


# Codificar Vulnerabilidad y Sexo como 0 y 1
Vulnerabilidad <- ifelse(Vulnerabilidad == 1, 0, 1)
Sexo <- ifelse(Sexo == 1, 0, 1)


# Prepara los datos para el modelo
N <- nrow(datos)
K <- 4  # Número de variables predictoras en tus datos
X <- as.matrix(datos[, 2:(K+1)])  #Matriz de datos predictores
y <- as.vector(Vulnerabilidad)

stan_data <- list(
  "X" = X,
  "y" = y,
  "N" = N, # Numero de observaciones
  "K" = ncol(X) # numero de varaibles
)

fit <- stan(file = 'modelo.stan',
            data = stan_data, chains = 4, iter = 2000)

print(fit) #Resumen del modelo, verificando Rhat

traceplot(fit) # Para ver como las cadenas oscilan entorno a los mismos valores

Beta.poste  <- extract(fit, pars = "beta")
Beta.poste  <- Beta.poste[[1]]


#Intervalos HDI para Beta_i
dev.new()
par(mfrow=c(dim(Beta.poste)[2],2))
for(i in 1:dim(Beta.poste)[2]){
  #Inicio
  HDI.interval.beta <- hdi(Beta.poste[,i])
  value1 <- HDI.interval.beta[1]
  value2 <- HDI.interval.beta[2]
  DENSITITY.BETA <- density(Beta.poste[,i])
  plot(DENSITITY.BETA, main = "Densidad Posterior", xlab = parse(text=(paste0("beta[",i,"]"))))
  DENSITITY.BETAy <- DENSITITY.BETA$y
  DENSITITY.BETAx <- DENSITITY.BETA$x
  # Lower and higher indices on the X-axis
  l <- min(which(DENSITITY.BETAx >= value1))
  h <- max(which(DENSITITY.BETAx < value2))
  
  polygon(c(DENSITITY.BETAx[c(l, l:h, h)]),
          c(0, DENSITITY.BETAy[l:h], 0),
          col = "slateblue1")
  #Fin
}
dev.off()

mcmc_dens_overlay(fit)
