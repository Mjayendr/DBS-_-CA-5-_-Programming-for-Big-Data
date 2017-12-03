# This is a program for calculator functions in R
# Author - Jay Monpara
#Student ID - 10360474
#Email - 10360474@mydbs.ie

#write 'add' function
#(1)
add <- function(x,y) {
  return(x+y)
}

#test add function
add(2,3)
add(10,-7)
add(0.5,45)

#(2)
#write 'Subtract' function

subtract <- function(x,y) {
  return (x-y)
}

#test subtract function
subtract(80,30)
subtract(8,15)
subtract(-0.5, -0.3)

#(3)
# write 'multiply'function

multiply <- function(x, y) {
  return (x * y)
}
#test multiply function
multiply(5,9)
multiply(3, 2)
multiply(0.2, -20)


#(4)
#write ' divide' function
divide <- function(x,y) {
  return(x / y)
}

# test divide function
divide(6,2)
divide(0, 5)
divide(-0.10, 0.2)

#(5)
#write 'square' function
square <- function(x) {
  return (x ^ 2)
}

# test square function
square(2)
square(0.5)
square(-4)

#(6)
# write ' square root' function
square_root <- function(x) {
  return (sqrt(x))
}

#test square_root function

square_root(25)
square_root(4)
square_root(0.36)

#(7)
#write 'factorial' function

fact <- function(x) {
  factorial(x)
}

#test fact function
fact(5)
fact(0)

#(8)
# write 'log' function
log <- function(x){
  return (log10(x))
}

# test log function
log(10)
log(100)

#(9)
#wrtie 'x power y' function
xpowery <- function(x,y) {
  return (x^y)
}

# test xpowery function
xpowery(2,3)
xpowery(10,2)

#(10)
#write 'percent' function
percent <- function (x,y){
  return ((x * y) / 100)
}

#test percent function
percent(100,20)
percent(20,30)


