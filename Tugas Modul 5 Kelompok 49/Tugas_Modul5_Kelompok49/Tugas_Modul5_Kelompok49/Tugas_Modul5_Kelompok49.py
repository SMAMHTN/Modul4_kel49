import data_user
email = input("email\t\t: ")
password = input("Password\t: ")
print()
login = data_user.data(email,password)
login.out_login()

