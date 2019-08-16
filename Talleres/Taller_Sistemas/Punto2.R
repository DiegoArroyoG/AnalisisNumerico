rm(list=ls())
library(pracma)
library(Matrix)

n=4

A = matrix(c(-8.1, -7, 6.123, -2,
             -1, 4,-3, -1,
             0, -1, -5, 0.6,
             -1, 0.33, 6, 1/2), nrow=n, byrow=TRUE)
U=A

L=A
U[lower.tri(U,diag=TRUE)] <- 0
L[upper.tri(L, diag = TRUE)] <- 0
print (A)
D = diag(diag(A))
D
U
L
b = matrix(c(1.45,3,5.12,-4), nrow=n, byrow=TRUE)

#punto 2B
print("Gauss-Seidel:")
tol = 1e-9
sol = itersolve(A, b, x0=c(1,2,1,1), tol=1e-9 , method = "Gauss-Seidel")
print(sol)
