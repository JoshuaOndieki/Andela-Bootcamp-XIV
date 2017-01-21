print("This program reverses you input")
reversed_string = []
string = str(input("type your word or sentence to get the reverse word : "))


def reverse_string(string_input):  # this function takes your input as argument
    split_string_to_list = list(string_input)  # split input into a list of letters
    length = len(string_input)-1  # get the length of input
    while 0 <= length:  # use while loop to append letters to a new list in reverse order
        reversed_string.append(split_string_to_list[length])  # append letter
        length -= 1  # reduce the letter index by one each time a letter is appended
# call the function join the letters into one string and convert your list to str
reverse_string(string)
reversed_string = " ".join(reversed_string)
reversed_string = str(reversed_string)
print("\nThe reverse of {} is : {}".format(string,reversed_string))  # print the reverse