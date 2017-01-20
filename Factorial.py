"""Find the factorial of number e.g factorial(5) = 5*4*3*2*1 = 120"""
def factorial(number):
    factorial_of_number=number
    number= number-1
    while number>0:
        factorial_of_number=factorial_of_number*number
        number-=1
    return factorial_of_number