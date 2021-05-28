username = 'Tim11'
password = '1234'

while True:
    print("What is your username? ")
    usrnm = input()
    if usrnm == username:
        print("Thanks " + username)
        break

while True:
    print("What is your password?  " + username)
    passtry = input()
    if passtry == password:
        break
print("Access granted " + username + " how many hours did you work?")
hours = input()

print("Congrats " + username + ", you worked " + hours + "hours today!")