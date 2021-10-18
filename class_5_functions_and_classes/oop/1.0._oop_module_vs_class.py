# module is designed to be executed
# module is a file
# class is some code
import os
print(os.system("echo hello"))

# we can also import a part of a module
from os import mkdir, rmdir
# mkdir("new")
# rmdir("new")

# from decimal module import Decimal Class
from decimal import Decimal
print (Decimal('13.5') + Decimal('19.4'))