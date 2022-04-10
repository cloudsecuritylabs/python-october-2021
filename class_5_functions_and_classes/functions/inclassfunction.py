# function

# function
def get_name():
    name = input("What is your name? ")
    age = input("What is your age? ")
    # tuple_to_return = (name, age) # list
    dictionary = { name : age}
    return dictionary

get_name_var = get_name()
print(type(get_name_var))
print(get_name_var)

# if __name__ == '__main__':
#     main()
