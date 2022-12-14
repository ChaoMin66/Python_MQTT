# To get user input without showing on command
# None of this are working

# 1. =============================================
import sys
import msvcrt

passwor = ''
while True:
    x = msvcrt.getch()
    if x == '\r':
        break
    sys.stdout.write('*')
    passwor +=x
    input("123: ")
print('\n'+passwor)

# 2. =============================================
import getpass
password = getpass.getpass('Password: ')
print(password)