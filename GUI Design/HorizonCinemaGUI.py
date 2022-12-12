import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Horizon Cinema Booking System")
        self.geometry("1366x768")
        self.resizable(0,0)
        self.style = ttk.Style(self)
        self.configure(bg="#181818")
        self.style.configure('TLabel', font=('Helvetica bold', 15), background="#181818", foreground="#b3b3b3")
        self.style.configure('TButton', font=("Helvetica bold", 10),foreground="#121212", height=40, width=25)
        self.style.configure('TFrame', font=('Helvetica bold', 15), background="#181818", foreground="#b3b3b3")
        try:
            self.attributes('-toolwindow', True)
        except tk.TclError:
            print("Windows Only")

        # Creating all the frames, inserting them into a dictionary for access later
        self.frames = {}

        for F in (BookingStaffLoginFrame, HomeFrame, SelectLoginTypePage, AdminLoginFrame, ManagerLoginFrame):
            frameName = F.__name__
            frame = F(self)
            self.frames[frameName] = frame

            #Placing each frame so that they are ready to be used with tkraise as appropriate
            frame.place(height=768, width=1366)

        self.showFrame("SelectLoginTypePage")

    # Function which will raise the given frame to the front of the GUI
    def showFrame(self, frameName):
        frame = self.frames[frameName]
        frame.tkraise()

class BookingStaffLoginFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(5, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.__createWidgets()

    def __createWidgets(self):
        email = tk.StringVar()
        password = tk.StringVar()
        login_title_label = ttk.Label(self, text="Login", font=('Helvetica bold', 26), foreground="white")
        login_title_label.grid(columnspan=3, row=0, padx=5, pady=5)
        email_label = ttk.Label(self, text="Username:")
        email_label.grid(column=0, row=1, padx=5, pady=5, sticky=tk.E)
        email_entry = ttk.Entry(self, textvariable=email)
        email_entry.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)
        password_label = ttk.Label(self, text="Password:")
        password_label.grid(column=0, row=2, padx=5, pady=5, sticky=tk.E)
        password_entry = ttk.Entry(self, textvariable=password, show="*")
        password_entry.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)
        login_button = ttk.Button(self, text="Login", command=lambda : self.validateLogin(email, password, email_entry, password_entry))
        login_button.grid(columnspan=2, row=3, padx=10, pady=10)
    
    def validateLogin(self, email, password, email_entry, password_entry):
        email_entry.configure(foreground="red")
        password_entry.configure(foreground="red")
        failed_login_label = ttk.Label(self, text="Forgotten your password? Please call over an admin to mediate this issue.", font=("Helvetica bold itallic", 8)).grid(columnspan=2, row=4, padx=10, pady=10)
        app.showFrame("HomeFrame")

class AdminLoginFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(5, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.__createWidgets()

    def __createWidgets(self):
        email = tk.StringVar()
        password = tk.StringVar()
        login_title_label = ttk.Label(self, text="Login", font=('Helvetica bold', 26), foreground="white")
        login_title_label.grid(columnspan=3, row=0, padx=5, pady=5)
        email_label = ttk.Label(self, text="Username:")
        email_label.grid(column=0, row=1, padx=5, pady=5, sticky=tk.E)
        email_entry = ttk.Entry(self, textvariable=email)
        email_entry.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)
        password_label = ttk.Label(self, text="Password:")
        password_label.grid(column=0, row=2, padx=5, pady=5, sticky=tk.E)
        password_entry = ttk.Entry(self, textvariable=password, show="*")
        password_entry.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)
        login_button = ttk.Button(self, text="Login", command=lambda : self.validateLogin(email, password, email_entry, password_entry))
        login_button.grid(columnspan=2, row=3, padx=10, pady=10)
    
    def validateLogin(self, email, password, email_entry, password_entry):
        email_entry.configure(foreground="red")
        password_entry.configure(foreground="red")
        failed_login_label = ttk.Label(self, text="Forgotten your password? Please call over an admin to mediate this issue.", font=("Helvetica bold itallic", 8)).grid(columnspan=2, row=4, padx=10, pady=10)
        app.showFrame("HomeFrame")

class ManagerLoginFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(5, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.__createWidgets()

    def __createWidgets(self):
        email = tk.StringVar()
        password = tk.StringVar()
        login_title_label = ttk.Label(self, text="Login", font=('Helvetica bold', 26), foreground="white")
        login_title_label.grid(columnspan=3, row=0, padx=5, pady=5)
        email_label = ttk.Label(self, text="Username:")
        email_label.grid(column=0, row=1, padx=5, pady=5, sticky=tk.E)
        email_entry = ttk.Entry(self, textvariable=email)
        email_entry.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)
        password_label = ttk.Label(self, text="Password:")
        password_label.grid(column=0, row=2, padx=5, pady=5, sticky=tk.E)
        password_entry = ttk.Entry(self, textvariable=password, show="*")
        password_entry.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)
        login_button = ttk.Button(self, text="Login", command=lambda : self.validateLogin(email, password, email_entry, password_entry))
        login_button.grid(columnspan=2, row=3, padx=10, pady=10)
    
    def validateLogin(self, email, password, email_entry, password_entry):
        email_entry.configure(foreground="red")
        password_entry.configure(foreground="red")
        failed_login_label = ttk.Label(self, text="Incorrect details, perhaps you meant to login as admin/booking staff? If not please contact your software provider.", font=("Helvetica bold itallic", 8)).grid(columnspan=2, row=4, padx=10, pady=10)
        app.showFrame("HomeFrame")

class HomeFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(5, weight=1)
        self.__createWidgets()

    def __createWidgets(self):
        horizon_cinema_label = ttk.Label(self, text="Horizon Cinemas", font=('Helvetica bold', 15))
        horizon_cinema_label.grid(column=0,row=1)
        current_user_label = ttk.Label(self, text="Staff Name [Staff Type]", font=('Helvetica bold', 15))
        current_user_label.grid(column=0,row=2)
        listings_button = ttk.Button(self, text="View Film Listings")
        listings_button.grid(column=1, row=1, padx=10, pady=20, sticky=tk.W)
        create_booking_button = ttk.Button(self, text="Create Booking")
        create_booking_button.grid(column=2, row=1, padx=10, pady=20)
        cancel_booking_button = ttk.Button(self, text="Cancel Booking")
        cancel_booking_button.grid(column=3, row=1, padx=10, pady=20)
        generate_report_button = ttk.Button(self, text="Generate Report")
        generate_report_button.grid(column=4, row=1, padx=10, pady=20, sticky=tk.E)
        view_booking_staff_button = ttk.Button(self, text="View Booking Staff")
        view_booking_staff_button.grid(column=1, row=2, padx=10, pady=20, sticky=tk.W)
        view_admin_button = ttk.Button(self, text="View Admin Staff")
        view_admin_button.grid(column=2, row=2, padx=10, pady=20)
        view_cinema_button = ttk.Button(self, text="View Cinemas")
        view_cinema_button.grid(column=3, row=2, padx=10, pady=20)
        view_film_button = ttk.Button(self, text="View Film")
        view_film_button.grid(column=4, row=2, padx=10, pady=20, sticky=tk.E)

class SelectLoginTypePage(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(5, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)
        self.__createWidgets()

    def __createWidgets(self):
        title_label = ttk.Label(self, text="Please Select User Type:", font=('Helvetica bold', 15))
        title_label.grid(column=1,row=1)
        booking_staff_login_button = ttk.Button(self, command=lambda : app.showFrame("BookingStaffLoginFrame"), text="Booking Staff")
        booking_staff_login_button.grid(column=1, row=2, padx=10, pady=20)
        admin_login_button = ttk.Button(self, command=lambda : app.showFrame("AdminLoginFrame"), text="Admin")
        admin_login_button.grid(column=1, row=3, padx=10, pady=20)
        manager_login_button = ttk.Button(self, command=lambda : app.showFrame("ManagerLoginFrame"), text="Manager")
        manager_login_button.grid(column=1, row=4, padx=10, pady=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()