try:
    x = 10/2
except:
    bad_flag = True
    print("not good")

else:
    bad_flag = False
    print(x)
    print("all good")

finally:
    if bad_flag == True:
        print("not great")
    else:
        print("great")

raise Exception("Incorrect")