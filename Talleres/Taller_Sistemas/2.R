library(pracma)
library(Matrix)

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

#Punto 2-b
print("Punto 2-b")
print(itersolve(A, b, tol = 1e-9 , method = "Gauss-Seidel"))



#punto 2-c
print("Punto 2-c")
jacobiPr <- function(A,b, x0, tol = 1e-9){
  x_n = matrix(x0)
  
  t = 0
  repeat
  {
    p = matrix(b-((L+U)%*%x_n))
    D1 = (solve(D))
    xn1 = D1%*%p
    
    cat("Error ",t," ",norm(xn1-x_n,"F")/norm(x_n), " ")
    
    x_n = xn1
    t = t + 1
    
    if(t == tol)
      break
  }
  cat("5 iteraciones respuestas: ",x_n)
}


x0 = c(1,2,3,4,5,6)
jacobiPr(A, b, x0, 5)
