login = input("Login: ")
passwd = input(" Password: ")
correct_login = "admin"
correct_password = "python123"
if passwd == correct_password and login == correct_login :
    print("Welcome admin")
else :
    print("Wrong login or password")
