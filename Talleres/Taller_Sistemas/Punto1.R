#install.packages("pracma")
library("pracma")

n=4

D1<-eye(n, m = n)
D2<-ones(n, m = n)
D3<-zeros(n, m = n)

A = matrix(c(-8.1, -7, 6.123, -2,
             -1, 4,-3, -1,
             0, -1, -5, 0.6,
             -1, 0.33, 6, 1/2), nrow=n, byrow=TRUE)

b = matrix(c(1.45,3,5.12,-4), nrow=n, byrow=TRUE)

diag1 <- function(M) {
  
  M[col(M)!=row(M)] <- 0
  
  return(M)
}

D = diag1(A)
L = tril(A,k=-1)
U = triu(A,k=1)

T = (-solve(D))%*%(L+U)
print("T")
print(T)
print("Norma")
print(norm(T,"F"))
