
GaussJordan <- function(A, b){
  if(is.matrix(A)) {
    n = nrow(A); m = ncol(A)
    if (m != n) stop("'A' debe ser una matriz cuadrada.")
  }
  cant <- 0
  Ab = cbind(A,b)
  for (k in 1:(n)){ 
    
    if(k != n){
      fila = which.max( abs(A[k:n,k]) ) + k-1
      
      Ab[c(k, fila), ] = Ab[c(fila, k), ]
      
      if(A[fila,k]==0) stop("La matriz es singular")
      
      for (i in (k+1):n){
        
        Ab[i, ] = Ab[i, ] - Ab[i, k]/Ab[k,k]*Ab[k, ]
        cant <- cant + 1
      }  
    }
    for(i in (k):1){
      if(i == k){
        Ab[i, ] = Ab[i, ]/Ab[i,k]
        cant <- cant + 1
      }
      else{
        Ab[i, ] = Ab[i, ] - Ab[i,k]*Ab[k,]
        cant <- cant + 1
      }
    }
  }
  cat("El cantero de multiplicaciones es de = ", cant, '\n')
  return(Ab)
}

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
b = c(1,2,3,4,5,6)

GaussJordan(A,b)

