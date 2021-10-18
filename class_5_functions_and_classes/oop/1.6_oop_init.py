class UnderstandInit(object):
    # init is not required
    def __init__(self):
        # add all validations here
        # very important
        # check network
        # check looking for file
        # check for proper formatting
        print('initiating')
        self.value = 0

    def increment(self):
        self.value = self.value + 1

ui = UnderstandInit()
ui.increment()
ui.increment()

print (ui.value)