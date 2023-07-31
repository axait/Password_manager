# # -------------------------------------IMPORT_JSON_FILE_PATH-----------------------------------------#
# import json
# from file_path import json_file_path
# with open(json_file_path) as file:
#     data = json.load(file)

md_file_path = "D:\\Password_manager\\database\\main_data" 
lp_file_path = "D:\\Password_manager\\database\\login_password"

# -------------------------------------IMPORT-LIBRARIES-----------------------------------------#
from tkinter import *
from tkinter import messagebox

# -------------------------------------FUNCTIONS-OF-GUI-----------------------------------------#
def generate_password() -> str :
    import random,string
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(12))
    password_entry.delete(0,END)
    password_entry.insert(0,password)

def is_valid_email(email) -> bool:
    # Check if the email contains the '@' and '.' symbols
    if '@' not in email or '.' not in email:
        return False

    # Split the email into local part and domain part
    local_part, domain_part = email.split('@', 1)

    # Check if the local part and domain part are not empty
    if not local_part or not domain_part:
        return False

    # Check if the domain part contains a dot ('.')
    if '.' not in domain_part:
        return False

    # Check that the part after the last dot has length 2 or 3
    domain_parts = domain_part.split('.')
    if not domain_parts[-1] or len(domain_parts[-1]) not in [2, 3]:
        return False

    # Check that the local part has a length larger than 4
    if len(local_part) <= 4:
        return False

    return True


def check_blank_input(url,email,password) -> bool:
    """THIS FUNCTION CHECK THAT ANY INPUT IS EMPTY OR NOT 
    AND PRINT MESSAGE IN WINDOW IF ANY FIELD IS EMPTY  😎
    """
    if url == '' or email == '' or password == '' :
        global error_label 

        if url == '' and email == '' and password == '' :
            error_label =  Label(root,text="Don't leave all field empty" , fg="red")
            error_label.place(x=105,y=205 ,width=300)

        elif url == '' and email == '' :
            error_label =  Label(root,text="Don't leave url and email fields empty" , fg="red")
            error_label.place(x=105,y=205 ,width=300)

        elif url == '' and password == '' :
            error_label =  Label(root,text="Don't leave url and password fields empty" , fg="red")
            error_label.place(x=105,y=205 ,width=300)

        elif  email == '' and password == '' :
            error_label =  Label(root,text="Don't leave email and password fields empty" , fg="red")
            error_label.place(x=105,y=205 ,width=300)

        elif url == "":
            error_label = Label(root,text="Don't leave url empty" , fg="red")
            error_label.place(x=105,y=205 ,width=300)

        elif email == "":
            error_label = Label(root,text="Don't leave email empty" , fg="red")
            error_label.place(x=105,y=205 ,width=300)

        elif password == "":
            error_label = Label(root,text="Don't leave password empty" , fg="red")
            error_label.place(x=105,y=205 ,width=300)
    else:
        return True

def read_last_line_index(filename) -> int :
    global md_file_path
    with open(md_file_path, "r") as file:
        lines = file.readlines()
        last_line = lines[-1].strip()
        index = int(last_line[0])+1
        return index

def add_password() -> None :
    # Get values from entry
    url = url_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    # CHECK THAT ANY FIELD NOT EMPTY
    if check_blank_input(url,email,password):

        # EMAIL VALID OR NOT
        if is_valid_email(email):
            result_save_data_question = messagebox.askquestion("Save Password", f"Do you want to save data?\nUrl : {url}\nemail : {email}\npassword : {password}")
            
            if result_save_data_question == "yes":

                # Data save process START
                root.clipboard_append(password)
                global md_file_path
                with open(md_file_path, "a") as file:
                    from data_encryptor import encrypt_data
                    index = read_last_line_index(md_file_path)
                    url = encrypt_data(url)
                    email = encrypt_data(email)
                    password = encrypt_data(password)
                    file.write(f"{index}     {url}     {email}     {password}\n")
                # Data save process END

                # SHOW MESSAGE THAT DATA IS SAVED
                error_label = Label(root,text="Data has been saved" , fg="green")
                error_label.place(x=105,y=205 ,width=300)
            # SHOW MESSAGE THAT DATA IS SAVED
            else:
                error_label = Label(root,text="Data has not been saved" , fg="red")
                error_label.place(x=85,y=205 ,width=300)
            
            # EMAIL NOT VALID ERROR
        else:
            error_label = Label(root,text="Email is not valid" , fg="red")
            error_label.place(x=85,y=205 ,width=300)
    else:
        ...

def log_out():
    global log_out_validation
    log_out_validation = "logout"
    root.destroy()

def change_master_password():
    from change_master_password import master_password_change_window
    root.destroy()
    master_password_change_window()

def show_help():
    messagebox.showinfo("Help", f"How can I help you")

def view_all_data():
    from data_viewer import view_data
    view_data()

def findPasswordByUrl():
    from find_password_by_url import find_password_by_url_window
    find_password_by_url_window()
# -----------------------------------------UI-DESIGN-------------------------------------------#
def dashboard():
    global root
    root = Tk()
    root.resizable(False,False)
    root.title("Dashboard")
    root.geometry('470x250')

    # LABEL
    url_label = Label(root,text='URL :',font=("Arial", 15))
    url_label.place(x=15,y=20,width=100,height=40)

    email_label = Label(root,text='Email :',font=("Arial", 15))
    email_label.place(x=15,y=70,width=100,height=40)

    password_label = Label(root,text='Password :',font=("Arial", 15))
    password_label.place(x=15,y=120,width=100,height=40)

    # ENTRIES
    global url_entry
    url_entry = Entry(root)
    url_entry.place(x=125,y=20,width=300,height=30)
    
    global email_entry
    email_entry = Entry(root)
    email_entry.place(x=125,y=75,width=300,height=30)

    global password_entry
    password_entry = Entry(root)
    password_entry.place(x=125,y=125,width=210,height=30)

    # password generate button
    generate_password_button = Button(root,text="Generate",relief=SOLID , command=generate_password)
    generate_password_button.place(x=345,y=125,height=30,width=80)
    
    # Add password button
    add_password_button = Button(root,text="ADD",relief=SOLID , command=add_password)
    add_password_button.place(x=30,y=170,height=30,width=400)

# --------------------------------------------MENU------------------------------------------- #
        # Create the menu 
    menubar =Menu(root)

# --------------------------------------------MENU-------------------------------------------
    global log_out_validation
    log_out_validation = "Keep"

    # Create the File menu
    file_menu = Menu(menubar, tearoff=0)
    file_menu.add_command(label="View all data", command=view_all_data)
    file_menu.add_command(label="Find password by URL", command=findPasswordByUrl)
    # file_menu.add_command(label="Update entry", command=change_master_password)
    # file_menu.add_command(label="Delete entry", command=change_master_password)
    file_menu.add_separator()
    file_menu.add_command(label="Change master password", command=change_master_password)
    file_menu.add_separator()
    file_menu.add_command(label="Log out", command=log_out)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="Options", menu=file_menu)

    # Create the Help menu
    menubar.add_command(label="Help", command=show_help)

    # Configure the root to use the menubar
    root.config(menu=menubar)


    root.mainloop()
    return log_out_validation

if __name__ == "__main__":
    dashboard()