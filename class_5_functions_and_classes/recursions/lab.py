# you get 2 numbers
# return different data types
# lists, dictionary, tuple, None



def return_list(n1, n2):
    return [n1, n2]

def return_tuple(n1, n2):
    return (n1, n2)

def main():
    first_num = int(input("Enter first num: "))
    second_num = int(input("Enter second num: "))
    print(return_list(first_num, second_num))
    print(return_tuple(first_num, second_num))

main()