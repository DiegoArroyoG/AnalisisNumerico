crearMatriz <- function(){
  return (matrix(data = floor(runif(36, min=0, max=20)), nrow = 6, ncol = 6))
  
}


con=0
A = crearMatriz()
con=norm(A,"F")*norm(inv(A),"F")

while(con<1000 ){
  A = crearMatriz()
  con=norm(A,"F")*norm(inv(A),"F")
}
A
b = matrix(c(1,2,3,4,5,6), nrow=6, byrow=TRUE)

D = diag(diag(A))
L = tril(A,k=-1,diag = FALSE)
U = triu(A,k=1,diag = FALSE)

N <- 3
A <- Diag(rep(3,N)) + Diag(rep(-2, N-1), k=-1) + Diag(rep(-1, N-1), k=1)
x0 <- rep(0, N)
b = c(4,5,6)
print(itersolve(A, b, tol=1e-9 , method = "Gauss-Seidel"))
