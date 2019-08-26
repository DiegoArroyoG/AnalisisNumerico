library(Matrix)

crearMatriz <- function(){
  return (matrix(data = floor(runif(36, min=0, max=20)), nrow = 6, ncol = 6))
  
}


con=0
A = crearMatriz()
con=norm(A,"I")*norm(inv(A),"I")

while(con<1000 ){
  A = crearMatriz()
  con=norm(A,"I")*norm(inv(A),"I")
}
A

lu <-lu(A)
lu
