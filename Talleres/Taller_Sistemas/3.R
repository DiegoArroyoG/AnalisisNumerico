tril1 <- function(M, k = 0) {
  if (k == 0) {
    M[upper.tri(M, diag = TRUE)] <- 0
  } else {
    M[col(M) >= row(M) + k + 1] <- 0
  }
  return(M)
}

diag1 <- function(M, k = 0) {
  if (k == 0) {
    M[upper.tri(M, diag = FALSE)] <- 0
    M[lower.tri(M, diag = FALSE)] <- 0
  } else {
    M[col(M) >= row(M) + k + 1] <- 0
  }
  return(M)
}

crearMatriz <- function(){
  return (matrix(data = floor(runif(9, min=1, max=20)), nrow = 3, ncol = 3))
  
}


con=0
A = crearMatriz()
con=norm(A,"I")*norm(inv(A),"I")

while(con<1000 ){
  A = crearMatriz()
  con=norm(A,"I")*norm(inv(A),"I")
}
A
sol <- tril1(A)
sol
di <-diag1(A)
di