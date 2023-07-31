# # -------------------------------------IMPORT_JSON_FILE_PATH-----------------------------------------#
# import json
# from file_path import json_file_path
# with open(json_file_path) as file:
#     data = json.load(file)

md_file_path = "D:\\Password_manager\\database\\main_data" 
lp_file_path = "D:\\Password_manager\\database\\login_password"

# -------------------------------------IMPORT-LIBRARIES-----------------------------------------#
from tkinter import *

# -------------------------------------FUNCTIONS-OF-GUI-----------------------------------------#

# --------------------------SHOW-PASSWORD--------------------------#
def showpassword():
    def toggle_password_visibility():
        """tHIS FUNCTION IS MADE TO SHOW OR HIDE PASSWORD"""

        # get variable value and proceed
        if toggle_password_visibility_variable.get():
            login_password_entry.config(show="")
        else:
            login_password_entry.config(show="*")
    

    # Create variable
    toggle_password_visibility_variable = BooleanVar()
    toggle_password_visibility_variable.set(False)

    # MAKE CHECKBUTTON
    is_ok = Checkbutton(text="Show Password", variable=toggle_password_visibility_variable,command=toggle_password_visibility)
    is_ok.place(x=25,y=90)
    
# -----------------------------LOGIN-------------------------------#
def login():
    user_passsowrd = login_password_entry.get()
    from data_encryptor import encrypt_data , decrypt_data
    global lp_file_path
    with open(lp_file_path) as file:
        master_password = decrypt_data(file.read())

    global login_validation
    if user_passsowrd == master_password :
        Label(root,text="Correct password ").place(x=70,y=180)
        login_validation = True
        root.destroy()
    elif user_passsowrd == "" :
        Label(root,text="Password is empty").place(x=70,y=180)
        login_validation = False
    else:
        Label(root,text="Encorrect password").place(x=70,y=180)
        login_validation = False


# -----------------------------------------UI-DESIGN-------------------------------------------#


def LoginWindow() -> "None":
    global root
    root  = Tk()
    root.title("Login")
    root.geometry('275x220')
    root.resizable(False,False)

    # Create global login_validation variable
    global login_validation
    login_validation  = False
    
    # Login Label
    Label(root,text='Enter Password :' , font=("Arial", 20)).place(x=20,y=20,height=30,width=210)
    
    #  Login Password Entry
    global login_password_entry
    login_password_entry = Entry(root,show='*')
    login_password_entry.place(x=25,y=60,height=25,width=210)
    
    # Show Password
    showpassword()
    
    # Login Button
    login_button = Button(root,text='Login', font=("Arial", 12,'bold'),command=login)
    login_button.place(x=70,y=130,height=40,width=100)



    root.mainloop()


    return login_validation



if __name__ == "__main__":
    result = LoginWindow()
    print(result)
