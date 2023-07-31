# -------------------------------------IMPORT-LIBRARIES-----------------------------------------#
from tkinter import *
from tkinter import messagebox


# -------------------------------------FUNCTIONS-OF-GUI-----------------------------------------#
def check_old_password_func(old_password_to_check)  -> bool:
    from data_encryptor import encrypt_data , decrypt_data
    with open('./database/login_password') as login_password_file :
        real_login_password = decrypt_data(login_password_file.read())
    if old_password_to_check == real_login_password :
        return True
    else :
        return False

def check_new_and_retype_password_func(new_password , retype_password ) -> bool :
    if new_password == retype_password :
        if new_password == "" and retype_password == "" :
            return False
        else :
            return True
    else :
        return False

def write_new_password(new_password) :
    def ask_question_to_write(new_password):
        from data_encryptor import encrypt_data , decrypt_data
        result_save_new_password_question = messagebox.askquestion("Save Password", f"Do you want to save new password?\nNew password: {new_password}")
        if result_save_new_password_question == "yes":
            try :
                with open('./database/login_password' , "w+t") as login_password_file :
                    login_password_file.write(encrypt_data(new_password))
                error_label = Label(root, text='New Password Saved Successfully' , fg='green' )
                error_label.place( x=18 , y=370 , width=335  ,height=40)
            except :
                error_label = Label(root, text='Some internal ERROR' , fg='red' )
                error_label.place( x=18 , y=370 , width=335  ,height=40)
        else:
                error_label = Label(root, text='Password not saved' , fg='red' )
                error_label.place( x=18 , y=370 , width=335  ,height=40)
    ask_question_to_write(new_password)


def save_new_password() -> None:
    old_password = old_password_entry.get()
    new_password = new_password_entry.get()
    retype_password = retype_password_entry.get()
    # 
    # CHECK OLD PASSWORD WHICH USER TYPE
    check_old_password = check_old_password_func(old_password)
    if check_old_password :
        # 
        # check_new_and_retype_password matched or not
        if check_new_and_retype_password_func(new_password , retype_password ) :
            write_new_password(new_password)
        else :
            error_label = Label(root, text='New password not matched' , fg='red' )
            error_label.place( x=18 , y=370 , width=335  ,height=40)
        
    else :
        error_label = Label(root, text='Please enter correct old password' , fg='red' )
        error_label.place( x=18 , y=370 , width=335  ,height=40)

def goto_dashboard():
    root.destroy()
    from dashboard import dashboard
    dashboard()

# -----------------------------------------UI-DESIGN-------------------------------------------#
def master_password_change_window():
    global root
    root = Tk()
    # GEOMETRY
    root.geometry('400x420')
    root.resizable(False,False)
    root.title('Change master password')
    # 
    # Title LABEL
    Label(root,text="Change Master Password" ,font=("Arial", 20 ,'bold') ,relief=SOLID).place(x=23,y=30 ,width=350 ,height=40)
    # 
    # -----------------------------INPUT_GUI_START_FROM_HERE--------------------------------------- #
    # FONT FOR ENTRIES
    entry_font =        ("Arial", 15 )     # ---------VARIABLE----------#
    # FONT FOR LABELS
    label_font = ("Arial", 15 ,'bold')     # ---------VARIABLE----------#
    # 
    # 
    # LABEL FOR ENTER OLD PASSWORD
    Label(root,text="Enter Old Password :" ,font=label_font ).place(x=10,y=90 ,width=230,height=30)
    # 
    # OLD PASSWORD ENTRY
    global old_password_entry
    old_password_entry = Entry(root ,font=entry_font  ,show='*' )
    old_password_entry .place(x=25 , y=120 , width=330  ,height=30)
    # 
    # LABEL FOR ENTER OLD PASSWORD
    Label(root,text="Enter New Password :" ,font=label_font ).place(x=10 , y=160 ,width=230,height=30)
    # 
    # OLD PASSWORD ENTRY
    global new_password_entry
    new_password_entry = Entry(root ,font=entry_font  ,show='*' )
    new_password_entry.place(x=25 , y=200 , width=330  ,height=30)
    # 
    # LABEL FOR ENTER OLD PASSWORD
    Label(root,text="Re-type Password :" ,font= label_font ).place(x=10,y=240 ,width=205,height=30)
    
    # OLD PASSWORD ENTRY
    global retype_password_entry
    retype_password_entry = Entry(root ,font=entry_font  ,show='*' )
    retype_password_entry .place(x=25 , y=280 , width=330  ,height=30)
    # 
    # ---------SAVE_BUTTON-------------- #
    Button(root , text="Save" ,relief=RIDGE ,borderwidth=5 , command=save_new_password , font=("Arial", 18) ).place( x=18 , y=320 , width=335  ,height=40 )
    # 
    # 
    # --------------------------------------------MENU-------------------------------------------
    # 
    # ROUGH--------------------------------------------------
    show_help= lambda : print("none")
    # END-rough--------------------------------------------------
    # 
    menubar =Menu(root)
    # 
    global log_out_validation
    log_out_validation = "Keep"
    # 
    # Create the File menu
    options_menu = Menu(menubar, tearoff=0)
    options_menu.add_command(label="Goto Dashboard", command=goto_dashboard)
    options_menu.add_separator()
    options_menu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="Options", menu=options_menu)

    # Create the Help menu
    menubar.add_command(label="Help", command=show_help)

    # Configure the root to use the menubar
    root.config(menu=menubar)
    # 
    root.mainloop()


if __name__ == "__main__":
    master_password_change_window()