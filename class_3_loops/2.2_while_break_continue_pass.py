counter = 0
while counter <= 5:
    counter = counter + 1
    if counter == 3:
        pass
        # break
        continue
        # bring this print only when explaining pass vs break
        print("passing {}".format(counter))
    else:
        print("The current number is: {}".format(counter))


