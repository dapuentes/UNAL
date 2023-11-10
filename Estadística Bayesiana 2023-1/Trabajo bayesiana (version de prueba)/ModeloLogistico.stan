data{
  int<lower=1> N; // Number of observations 
  int<lower=1> K; // Number of parameters
  int<lower=0,upper=1> y[N];
  matrix[N, K] X;
}

parameters{
  vector[K] beta;
}


model{
  beta ~ normal(0, 100);
 
  y ~ bernoulli_logit(X * beta);
}
