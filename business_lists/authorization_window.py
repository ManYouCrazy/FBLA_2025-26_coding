
import tkinter as tk
from functions import login, open_json

class auth_window():

    def __init__(self,root):
        # user data
        self.userdata_file_data = open_json('business_lists/userdata.json')

        #class vars for accsessing
        self.logged_in = tk.BooleanVar()
        self.logged_in.set(False)
        self.username = ""

        # main window
        self.window = tk.Toplevel(root)
        self.window.wm_geometry("400x200")
        self.window.title("Authorization")

        # create empty frame
        self.frame_login = tk.Frame(self.window)
        self.frame_auth = tk.Frame(self.window)

        #login frame widgets
        self.lbl_username = tk.Label(self.frame_login, text='Username:',font="Courier")
        self.ent_username = tk.Entry(self.frame_login, bd=3)
        self.lbl_password = tk.Label(self.frame_login,text="Password:",font="Courier")
        self.ent_password = tk.Entry(self.frame_login, bd=3,show="*")
        self.btn_login = tk.Button(self.frame_login, text="Log in",command=self.button_pressed)
        self.btn_censor = tk.Button(self.frame_login, text="Hide Password",command=self.censor_text)


        #auth frame widgets
        self.lbl_auth_password = tk.Label(self.frame_auth,text="",font="Courier")
        self.btn_back_auth = tk.Button(self.frame_auth, text="Try again",command=self.back_auth)

#functions
    def button_pressed(self):
        self.lbl_auth_password.config(text=login(self.userdata_file_data,self.ent_username.get(),self.ent_password.get())[0])
        self.frame_auth.tkraise()
        if(login(self.userdata_file_data,self.ent_username.get(),self.ent_password.get())[1] == 1):
            self.auth_label.pack_forget()
            self.logged_in.set(True)
            self.username = self.ent_username.get()
            self.window.destroy()

    def censor_text(self):
        if (self.ent_password.cget("show") == ""):
            self.ent_password.config(show="*")
        else:
            self.ent_password.config(show="")

    def back_auth(self):
        self.frame_login.tkraise()

    def run(self):
        self.frame_login.grid(row=0,column=0,sticky="news")
        self.frame_auth.grid(row=0,column=0,sticky="news")
        self.frame_login.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.frame_auth.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.frame_login.tkraise()

        self.auth_label = tk.Label(self.root, text="Log in before continuing")
        self.auth_label.pack()

        self.lbl_username.grid(row=0,column=0)
        self.ent_username.grid(pady=5,row=1,column=0)
        self.lbl_password.grid(row=0,column=1)
        self.ent_password.grid(pady=5,row=1,column=1)
        self.btn_login.grid(row=2,column=0)
        self.btn_censor.grid(row=2,column=1)
        self.lbl_auth_password.pack()
        self.btn_back_auth.pack()
