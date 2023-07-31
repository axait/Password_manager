import login
from dashboard import dashboard
from tkinter import messagebox as msg

login_validation : bool = login.LoginWindow()

if login_validation :
    logout_validation = dashboard()
    if logout_validation == "logout" :
        login_validation = login.LoginWindow()
        if login_validation :
            logout_validation = dashboard()
            if logout_validation == "logout" :
                login_validation = login.LoginWindow()
                if login_validation :
                    logout_validation = dashboard()
                    if logout_validation == "logout" :
                        login_validation = login.LoginWindow()
                        if login_validation :
                            logout_validation = dashboard()
                            if logout_validation == "logout" :
                                login_validation = login.LoginWindow()
                                if login_validation :
                                    logout_validation = dashboard()
    else :
        exit()
















# if login_validation :
#     logout_validation = dashboard()

#     while logout_validation == "logout":
#         print("loop")
#         if logout_validation == "logout":
#             login_validation = login.LoginWindow()
#             if login_validation :
#                 logout_validation = dashboard()
#         else:
#             logout_validation = dashboard()
# else:
#     ...
#     # msg.showinfo("Invalid login", "Please enter correct password")