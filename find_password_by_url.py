# # -------------------------------------IMPORT_JSON_FILE_PATH-----------------------------------------#
# import json
# from file_path import json_file_path
# with open(json_file_path) as file:
#     data = json.load(file)

from file_path import md_file_path,lp_file_path

# -------------------------------------IMPORT-LIBRARIES-----------------------------------------#
from tkinter import *
from dashboard import show_help
import data_encryptor
# -------------------------------------NECCESSARY-FUNCTIONS-----------------------------------------#


def find_password_by_url():
    target_url = url_entry.get()
    global md_file_path
    with open(md_file_path, "r") as file:
        data = file.readlines()
        for line in data:
            split_line = line.split('     ')
            index = split_line[0]
            url = split_line[1]
            email = split_line[2]
            password = split_line[3]
            password = password[0:-1]
            url = data_encryptor.decrypt_data(url)
            email = data_encryptor.decrypt_data(email)
            password = data_encryptor.decrypt_data(password)
            if url == target_url:
                index , url,email,password = index , url,email,password
            else:
                index , url,email,password = 'None','None','None','None'

        from data_encryptor import decrypt_data
        text_text.delete(0.1,END)
        text_text.insert(END, f"Index: {index}\nURL: {url}\nEmail/username: {email}\nPassword: {password}\n")

# -------------------------------------FUNCTIONS-OF-GUI-----------------------------------------#


def find_password_by_url_window():
    # Create the main window
    global root , url_entry,text_text
    root = Tk()
    root.title("Fing password by url")
    root.geometry("600x500")
    Label(root , text="Enter url :" , font=("Arial" , 20 , "bold")).place(x=20 , y=5 , width=130 , height=40)

    url_entry = Entry(root)
    url_entry.place(x=25 , y=55 , width=400 , height=30)

    Button(root,text="Get" , relief=SOLID , command=find_password_by_url ).place(x=435 , y=55 , width=100 , height=30)

    Label(root , text="Output :" , font=("Arial" , 20 , "bold")).place(x=20 , y=95 , width=130 , height=40)

    text_text = Text(root, wrap=None)
    text_text.place(x=25 , y=145 , width=550 , height=300)

        # Create vertical scrollbar and associate it with the Text widget
    scrollbar_y = Scrollbar(root, command=text_text.yview)
    scrollbar_y.pack(side='right', fill=Y)
    text_text['yscrollcommand'] = scrollbar_y.set

    # Create horizontal scrollbar and associate it with the Text widget
    scrollbar_x = Scrollbar(root, command=text_text.xview, orient='horizontal')
    scrollbar_x.pack(side='bottom', fill=X)
    text_text['xscrollcommand'] = scrollbar_x.set



    
    root.mainloop()
    

# -----------------------------------------UI-DESIGN-------------------------------------------#

if __name__ == "__main__":
    find_password_by_url_window()