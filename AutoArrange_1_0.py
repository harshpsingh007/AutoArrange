import os
import shutil
from tkinter import *
from tkinter import messagebox

master = Tk()
master.title("Auto Arrange")
master.minsize(width=500, height=300)

# Lable 1 == WELCOME TEXT
lbl1 = Label(master, text="WELCOME TO AUTO ARRANGE",
            font=("Courier", 30, 'bold'))
lbl1.grid(row=1, column=1,pady=10)

# LABLE 2 == iNSTRUCTION TO ENTER PATH
lbl2 = Label(master, text="Enter the complete path of your Folder in which you want to Run Auto Arrange", font=(
    "Courier", 14, "italic"))
lbl2.grid(row=2, column=1,pady=5)

# Entry == PLACE TO ADD PATH OF THE FOLDER
folderpath = Entry(master, font=("Courier", 20, "italic"), width=55)
folderpath.focus()
folderpath.grid(row=3, column=1)


def action():
    dict_extention = {
        'audio_extention': ['.mp3', '.m4a', '.wav', '.cda', '.aif', '.mid', '.midi', '.mpa', '.ogg', '.wpl', '.wma'],
        'video_extention': ['.mp4', '.mkv', '.MKV', '.flv', '.webm', '.vob', '.gif', '.avi', '.wmv', '.mpeg', '.3gp'],
        'document_extention': ['.txt', '.pdf', '.doc', '.html', '.ppt'],
        'image_extention': ['.jpg', '.gif', '.png', '.jpeg', '.ico', '.ps', '.psd', '.tif', '.tiff', '.bmp', '.ai'],
        'programming_extentions': ['.py', '.js', '.java', '.swift', '.class', '.c', '.html''.xml', '.css', '.php', '.rss', '.xhtml', '.asp', '.aspx', '.cer', '.cfm', '.cgi', '.pl', '.htm', '.jsp', '.part'],
        'compressed_extentions': ['.7z', '.arj', '.deb', '.pkg', '.rar', '.rpm', '.tar', '.gz', '.z', '.zip'],
        'executabelFile_extentions': ['.apk', '.bat', '.bin ', '.pl', '.com ', '.exe', '.wsf', '.msi', '.jar', '.gadget'],
        'font_extentions': ['.fnt', '.otf', '.fon', '.ttf'],

    }

    old_folder_path = folderpath.get()

    def file_finder(folder_path, file_extentions):
        files = []
        try:
            for files_in_folder in os.listdir(folder_path):
                for extentions in file_extentions:
                    if files_in_folder.endswith(extentions):
                        files.append(files_in_folder)
            return files
        except:
            messagebox.showerror(
                "Path Not Found", "The path is not given or is not available.")

    new_folder_path_list = []
    for type, extentions in dict_extention.items():
        new_folder_name = (str(type.split("_")[0])).capitalize() + "Files"
        new_folder_path = os.path.join(old_folder_path, new_folder_name)
        new_folder_path_list.append(new_folder_path)
        try:
            os.mkdir(new_folder_path)
        except:
            continue

        for file in file_finder(old_folder_path, extentions):
            old_file_path = os.path.join(old_folder_path, file)
            new_file_path = os.path.join(new_folder_path, file)
            shutil.move(old_file_path, new_file_path)

    for i in new_folder_path_list:
        if len(os.listdir(i)) == 0:
            os.rmdir(i)
        else:
            pass
    folderpath.delete(0, END)


# BUTTON == TO SUBMIT AND START THE ACTION
btn = Button(master, command=action, text="SUBMIT & START", width=40,
            border=10, font=("Courier", 15, "bold"), activebackground="#2568cc")
btn.grid(row=4, column=1,pady=20)

lbl3 = Label(master,text="NOTE - If something went wrong,Please try again it will definately solve the issue",
    font=("Courier",10,"italic"))
lbl3.grid(row=10,column=1,pady=50)
master.mainloop()

# action()
