# # -------------------------------------IMPORT_JSON_FILE_PATH-----------------------------------------#
# import json
# from file_path import json_file_path
# with open(json_file_path) as file:
#     data = json.load(file)

md_file_path = "D:\\Password_manager\\database\\main_data" 
lp_file_path = "D:\\Password_manager\\database\\login_password"

# -------------------------------------IMPORT-LIBRARIES-----------------------------------------#
from tkinter import *
from dashboard import show_help
# -------------------------------------NECCESSARY-FUNCTIONS-----------------------------------------#

def change_master_password(): 
    from change_master_password import master_password_change_window
    root.destroy()
    master_password_change_window()


# -------------------------------------FUNCTIONS-OF-GUI-----------------------------------------#

def view_data():

    # Create the main window
    global root
    root = Tk()
    root.title("Tkinter Example")    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set the window size to match the screen size
    root.geometry(f"{screen_width}x{screen_height}")

    # Adjust the height of the Text widget
    list_height = 50  # Change this value to set the height (number of visible lines) of the Text widget
    passwords_list = Text(root, wrap='none')  # Disable word wrapping
    passwords_list.pack(fill=BOTH, expand=True, anchor=N)

    # Create vertical scrollbar and associate it with the Text widget
    scrollbar_y = Scrollbar(root, command=passwords_list.yview)
    scrollbar_y.pack(side='right', fill=Y)
    passwords_list['yscrollcommand'] = scrollbar_y.set

    # Create horizontal scrollbar and associate it with the Text widget
    scrollbar_x = Scrollbar(root, command=passwords_list.xview, orient='horizontal')
    scrollbar_x.pack(side='bottom', fill=X)
    passwords_list['xscrollcommand'] = scrollbar_x.set

    global md_file_path
    with open(md_file_path, "r") as file:
        from data_encryptor import decrypt_data
        for line in file:
            index, url, email, password = line.strip().split('     ')
            passwords_list.insert(END, f"Index: {index} URL: {decrypt_data(url)}      Email/username: {decrypt_data(email)}      Password: {decrypt_data(password)}\n")


    # --------------------------------------------MENU------------------------------------------- #
        # Create the menu 
    menubar =Menu(root)

    # --------------------------------------------MENU-------------------------------------------
    global log_out_validation
    log_out_validation = "Keep"

    # Create the File menu
    file_menu = Menu(menubar, tearoff=0)
    file_menu.add_command(label="change_master_password", command=change_master_password)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="Options", menu=file_menu)

    # Create the Help menu
    menubar.add_command(label="Help", command=show_help)

    # Configure the root to use the menubar
    root.config(menu=menubar)
    root.mainloop()



# -----------------------------------------UI-DESIGN-------------------------------------------#

if __name__ == "__main__":
    view_data()