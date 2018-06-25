import sys
import time
import datetime
import platform
import tkinter
from tkinter import *
import socket
from socket import gethostname, gethostbyname
import pyautogui
import subprocess
from tkinter import ttk
import pathlib
from tkinter import filedialog


root = tkinter.Tk()
root.title('Project-Manger Framework')
root.iconbitmap('icon.ico')
root.geometry('500x500')

day = datetime.datetime.now()
host = socket.gethostname()
system = platform.system()+platform.release()

date = tkinter.Label(root, text="Date : "+str(day)).pack()

pc_name = tkinter.Label(root, text="HOST : "+host).pack()

os = tkinter.Label(root, text="OS : "+system).pack()

label = tkinter.Label(root, text="Project name : ").pack(anchor=W)

proj_name = Entry(root, width=20, bg="white")
proj_name.pack(anchor=W)

label2 = tkinter.Label(root, text="Project Descrption : ").pack(anchor=W)

des = Entry(root, width=35, bg="white")
des.pack(anchor=W)

label3 = tkinter.Label(root, text="Project Programming Language : ").pack(anchor=W)

proj_pl = tkinter.IntVar()

pl1 = Radiobutton(root, text="Python", variable=proj_pl, value=1).pack(anchor=W)
pl2 = Radiobutton(root, text="Ruby", variable=proj_pl, value=2).pack(anchor=W)
pl3 = Radiobutton(root, text="Shell", variable=proj_pl, value=3).pack(anchor=W)
pl4 = Radiobutton(root, text="JavaScript", variable=proj_pl, value=4).pack(anchor=W)
pl5 = Radiobutton(root, text="Php", variable=proj_pl, value=5).pack(anchor=W)
pl6 = Radiobutton(root, text="C ++", variable=proj_pl, value=6).pack(anchor=W)
pl7 = Radiobutton(root, text="C #", variable=proj_pl, value=7).pack(anchor=W)
pl8 = Radiobutton(root, text="Web Development", variable=proj_pl, value=8).pack(anchor=W)

blank = tkinter.Label(root, text="").pack()




# Create button function
def create():
    name = proj_name.get()
    descr = des.get()
    code = proj_pl.get()

    proj_open = tkinter.Toplevel()
    proj_open.iconbitmap("icon.ico")
    proj_open.geometry("800x800")

    # open option
    def open_command():
        file = filedialog.askopenfile(parent=root,mode='rb',title='Select a file')
        if file != None:
            contents = file.read()
            text.insert('1.0',contents)
            file.close()
            print(str(file)+" Opend")

    blank4 = tkinter.Label(proj_open, text="Project Code").pack(anchor=W)

    text = Text(proj_open)
    text.pack(fill=X)

    # Save as command
    def save_as():
        t = text.get("1.0", "end-1c")
        savelocation = filedialog.asksaveasfilename(filetypes=[("Python file","*.py"),("Ruby file", "*.rb"),("JavaScript", "*.js"),
        ("C++", "*.cpp"),("C#", "*.cs"),("Shell", "*.sh"),("Php", "*.php"),("html", "*.html"),("CSS", "*.css")
        ],defaultextension='.py')
        if savelocation != None:
            file = open(savelocation, "w+")
            file.write(t)
            file.close()
            pyautogui.alert(text=name+" Saved Successfully", title="Save Status", button="ok")


    # Run commmand
    def run():
        print("Console Log / "+str(day))
        print("===============================")
        print("[*]"+name+" Programe is Runing[*]")
        for run in range(1,1001):
            print(name.upper()+" Runing ==> "+str(time.clock()), "Seconds")


    # debug command
    def debug():
        print("////////////////////////////////////////////")
        print("[!!]"+name.upper()+"is in Debug Mode[!!]")
        print("////////////////////////////////////////////")
        for num in range(1,21):
            print(num)
            time.sleep(2)
        print("############################################")

    # new project command
    def new():
        proj_open.destroy()

    # build project
    def build():
        print("[+]"+name+"Built Successfully at "+str(day)+"[+]")
        save()


    blank3 = tkinter.Label(proj_open, text="Project Console").pack(side=TOP, anchor=CENTER)

    # GUI console
    t1 = Text(proj_open)
    t1.pack(fill=Y)
    class PrintToT1(object):
     def write(self, s):
         t1.insert(END, s)
    sys.stdout = PrintToT1()


    # Save log files
    def slog():
        log = t1.get("1.0", "end-1c")
        savelog = filedialog.asksaveasfilename(filetypes=[("Console Log", "*.cl")],defaultextension='.cl')
        if savelog != None:
            file = open(savelog, "w+")
            file.write(log)
            file.close()
            pyautogui.alert(text=name+" Log Saved Successfully", title="Project Console", button="ok")

    # Open Log files
    def olog():
        file = filedialog.askopenfile(parent=root,mode='rb',title='Select a file')
        if file != None:
            contents = file.read()
            t1.insert('1.0',contents)
            file.close()
            pyautogui.alert(text=str(file)+"\n Opend In Project Console", title="Project Console", button="ok")


    # Exit from project manager framework
    def all():
        proj_open.destroy()
        root.destroy()

     # Save current project command
    def save():
        t = text.get("1.0", "end-1c")
        file = open(tag, "w+")
        file.write(t)
        file.close()
        pyautogui.alert(text=tag+" Saved Successfully", title="Save Status", button="ok")

    # Directory listing ...
    def list():
        currentDirectory = pathlib.Path('.')
        for currentFile in currentDirectory.iterdir():
            print(currentFile)
            print("-----------------------")


    # Menu Controller
    menu_open = Menu(proj_open)
    proj_open.config(menu=menu_open)
    option = Menu(menu_open)
    compile = Menu(menu_open)
    console = Menu(menu_open)

    # Options Menu
    menu_open.add_cascade(label="Options", menu=option)
    option.add_command(label="New Project", command=new)
    option.add_command(label="Open Project", command=open_command)
    option.add_command(label="Save Project", command=save)
    option.add_command(label="Save Project As", command=save_as)
    option.add_command(label="Quit", command=all)


    # Code options (run, debug, etc ..)
    menu_open.add_cascade(label="Code", menu=compile)
    compile.add_command(label="Run", command=run)
    compile.add_command(label="Debug", command=debug)
    compile.add_command(label="Build", command=build)

    # Console Menu
    menu_open.add_cascade(label="Console", menu=console)
    console.add_command(label="Open Log", command=olog)
    console.add_command(label="Save Log", command=slog)
    console.add_command(label="Directorys", command=list)


    # Directory listing ...
    list()


    # File Building
    if code == 1:
        pb.start()
        proj_open.title("Project-Manger Framework -- [ "+name+".py ]")
        file = open(name+".py", "w")
        file.close()
        type = open(name+"_descrption.txt", "w")
        type.write("Made with Project-Manger\n")
        type.write("==============================\n")
        type.write(descr)
        type.close()
        tag = name+".py"
    elif code == 2:
        pb.start()
        proj_open.title("Project-Manger Framework -- [ "+name+".rb ]")
        file = open(name+".rb", "w")
        type = open(name+"_descrption.txt", "w")
        type.write("Made with Project-Manger\n")
        type.write("==============================\n")
        type.write(descr)
        type.close()
        file.close()
        tag = name+".rb"
    elif code == 3:
        pb.start()
        proj_open.title("Project-Manger Framework -- [ "+name+".sh ]")
        file = open(name+".sh", "w")
        file.close()
        type = open(name+"_descrption.txt", "w")
        type.write("Made with Project-Manger\n")
        type.write("==============================\n")
        type.write(descr)
        type.close()
        tag = name+".sh"
    elif code == 4:
        pb.start()
        proj_open.title("Project-Manger Framework -- [ "+name+".js ]")
        file = open(name+".js", "w")
        file.close()
        type = open(name+"_descrption.txt", "w")
        type.write("Made with Project-Manger\n")
        type.write("==============================\n")
        type.write(descr)
        type.close()
        tag = name+".js"
    elif code == 5:
        pb.start()
        proj_open.title("Project-Manger Framework -- [ "+name+".php ]")
        file = open(name+".php", "w")
        file.close()
        type = open(name+"_descrption.txt", "w")
        type.write("Made with Project-Manger\n")
        type.write("==============================\n")
        type.write(descr)
        type.close()
        tag = name+".php"
    elif code == 6:
        pb.start()
        proj_open.title("Project-Manger Framework -- [ "+name+".cpp ]")
        file = open(name+".cpp", "w")
        file.close()
        type = open(name+"_descrption.txt", "w")
        type.write("Made with Project-Manger\n")
        type.write("==============================\n")
        type.write(descr)
        type.close()
        tag = name+".cpp"
    elif code == 7:
        pb.start()
        proj_open.title("Project-Manger Framework -- [ "+name+".cs ]")
        file = open(name+".cs", "w")
        file.close()
        type = open(name+"_descrption.txt", "w")
        type.write("Made with Project-Manger\n")
        type.write("==============================\n")
        type.write(descr)
        type.close()
        tag = name+".cs"
    elif code == 8:
        pb.start()
        proj_open.title("Project-Manger Framework -- [ Web Development ("+name+".html"+") ]")
        file = open(name+".html", "w")
        file.close()
        file2 = open(name+".js", "w")
        file2.close()
        file3 = open(name+"_style.css", "w")
        file3.close()
        file4 = open(name+".php", "w")
        file4.close()
        type = open(name+"_descrption.txt", "w")
        type.write("Made with Project-Manger\n")
        type.write("==============================\n")
        type.write(descr)
        type.close()
        tag = name+".html"
    else:
        proj_open.title("Project-Manger Framework -- [ Unknown Project ]")
        print()
        print("[!!]No Project to open[!!]")



create_btn = tkinter.Button(root, text="Create Project", command=create).pack(anchor=W)

blank2 = tkinter.Label(root, text="").pack()

# Progressbar  tracker
pb = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
pb.pack()

# open editor command
def editor():
    create()

# About option
def about():
    pyautogui.alert(text="Project-Manger by Yousef Hosam\n            Project-Manger v1.0", title="About", button="Close")


# import option
def imp():
    file = filedialog.askopenfile(parent=root,mode='rb',title='Select a file')
    if file != None:
        contents = file.read()
        text.insert('1.0',contents)
        file.close()
        print(str(file)+" Project Imported Successfully")
        proj_open.title(str(file)+" -- Project Manger Framework")

# Programe Menu
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
help = Menu(menu)
menu.add_cascade(label="Options", menu=filemenu)
menu.add_cascade(label="Help", menu=help)
help.add_command(label="About", command=about)
filemenu.add_command(label="Import Project", command=imp)
filemenu.add_command(label="Open Editor", command=editor)
filemenu.add_command(label="Quit", command=root.destroy)


root.mainloop()
