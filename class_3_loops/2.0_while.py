# teach while loop
# teach break
# teach counters
# teach use of flags
# mix with if-else

# implement password lock out! auth (false), count=0, max_attempt = 3
# break when password input attempt > 3
# call 911!

password = 'secret'
ask_for_password = ''
while ask_for_password != password: # conditional expression
    # print some message back to the user
    ask_for_password = input("What is your password? ")

print('Bingo')