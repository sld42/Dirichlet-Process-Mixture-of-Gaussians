# Dirichlet-Process-Mixture-of-Gaussians
This repo shows how data generated from a Dirichlet process mixture of Gaussians with a NIW prior on the Gaussian parameters changes as we vary the parameters 

The code here is written in Python and generates figures to show what happens to the data as you vary the following parameters:

alpha: The concentration parameter of the stick breaking process 

nu: The degree of freedom parameter of the inverse Wishart distribution

psi: A positive-semidefinite matrix that parameterizes the inverse Wishart distribution

lambda: The covariance coefficient in the normal distribution of the NIW

mu: The mean of the normal distribution in the NIW

The DPM.pdf file has an explanation of how each of the parameters affect the generated data. The figures in the pdf are generated from Matlab, and the figures in the images folder of this repo were generated in Python. 
