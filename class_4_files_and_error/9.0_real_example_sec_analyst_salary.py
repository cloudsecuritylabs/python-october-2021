#https://ischoolonline.berkeley.edu/blog/cybersecurity-salary/

# read the file
file = open("salary_space_sep_final1.csv", "r")
# print(file.read())

state = input("Enter a state: ")
state=state.capitalize()
print(state)

for salary_info in file.readlines():
    salary_info = salary_info.capitalize()
    # print(salary_info)
    if salary_info.startswith(state):
        print(salary_info)
        splitted = salary_info.split(" ")
        print(splitted[3])



# ask user to enter a State
# want to print salary for a cyber security analyst for the state


























#
#
#
#
# with open("salary_space_sep_final1.csv", "r") as file:
#     salary_info_by_state = file.readlines()
#
#
#
# while True:
#     state = input("Which state? ")
#     if state == "exit":
#         break
#     for salary in salary_info_by_state:
#         if salary.startswith(state):
#             detailed_salary =salary.split(" ")
#             print(detailed_salary[3].rstrip())
#
#
