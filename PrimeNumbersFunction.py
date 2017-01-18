prime_numbers_list = []
lower_limit = input("Enter the lower value")
upper_limit =input("Enter the upper value")
lower_limit = int(lower_limit)
upper_limit = int(upper_limit)
def prime_numbers(lower_limit , upper_limit):
    #loop through every number in the range lower_limit-upper_limit
    for number in range(lower_limit , upper_limit+1):
        if number>1:  # check whether the number is greater than one
            for i in range(2,number):
                if number%i==0:  # if else the number is not a prime, break loop
                    break
                else:  # else the number is a prime number append to list and break the prime check loop
                    prime_numbers_list.append(number)
                    break
    return prime_numbers_list

print(prime_numbers(lower_limit,upper_limit))