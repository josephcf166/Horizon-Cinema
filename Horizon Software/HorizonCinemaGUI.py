import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb

# TODO: ADD VIEW CINEMAS FRAME FOR BOTH MANAGER AND ADMIN VIEW


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

        for F in (LoginFrame, HomeFrame, ViewBookingStaffFrame, ViewAdminFrame, ViewFilmFrame, AddCinemasFrame, GenerateReportFrame, ViewFilmListingsFrame, CreateBookingFrame, CancelBookingFrame, ViewCinemaScreeningsFrame):
            frameName = F.__name__
            frame = F(self)
            self.frames[frameName] = frame

            #Placing each frame at the same size so that they are ready to be used with tkraise as appropriate
            frame.place(height=768, width=1366)

        self.showFrame("LoginFrame")

    # Function which will raise the given frame to the front of the GUI
    def showFrame(self, frameName):
        frame = self.frames[frameName]
        frame.tkraise()

class LoginFrame(ttk.Frame):
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



class HomeFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(4, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(5, weight=1)
        self.__createWidgets()

    def __createWidgets(self):
        horizon_cinema_label = ttk.Label(self, text="Horizon Cinemas", font=('Helvetica bold', 15))
        horizon_cinema_label.grid(column=0,row=1)
        current_user_label = ttk.Label(self, text="Staff Name [Staff Type]", font=('Helvetica bold', 15))
        current_user_label.grid(column=0,row=2)
        listings_button = ttk.Button(self, command=lambda : app.showFrame("ViewFilmListingsFrame"), text="View Film Listings")
        listings_button.grid(column=1, row=1, padx=10, pady=20, sticky=tk.W)
        create_booking_button = ttk.Button(self, command=lambda : app.showFrame("CreateBookingFrame"), text="Create Booking")
        create_booking_button.grid(column=2, row=1, padx=10, pady=20)
        cancel_booking_button = ttk.Button(self, command=lambda : app.showFrame("CancelBookingFrame"), text="Cancel Booking")
        cancel_booking_button.grid(column=3, row=1, padx=10, pady=20)
        generate_report_button = ttk.Button(self, command=lambda : app.showFrame("GenerateReportFrame"), text="Generate Report")
        generate_report_button.grid(column=4, row=1, padx=10, pady=20, sticky=tk.E)
        view_booking_staff_button = ttk.Button(self, command=lambda : app.showFrame("ViewBookingStaffFrame"), text="View Booking Staff")
        view_booking_staff_button.grid(column=1, row=2, padx=10, pady=20, sticky=tk.W)
        view_admin_button = ttk.Button(self, command=lambda : app.showFrame("ViewAdminFrame"), text="View Admin Staff")
        view_admin_button.grid(column=2, row=2, padx=10, pady=20)
        view_cinema_button = ttk.Button(self, command=lambda : app.showFrame("AddCinemasFrame"), text="Add Cinemas/City")
        view_cinema_button.grid(column=3, row=2, padx=10, pady=20)
        view_film_button = ttk.Button(self, command=lambda : app.showFrame("ViewFilmFrame"), text="View Film")
        view_film_button.grid(column=4, row=2, padx=10, pady=20, sticky=tk.E)
        view_screenings_button = ttk.Button(self, command=lambda : app.showFrame("ViewCinemaScreeningsFrame"), text="View Cinema Screenings")
        view_screenings_button.grid(column=1, row=3, padx=10, pady=20, sticky=tk.W)
        logout_button = ttk.Button(self, command=lambda : app.showFrame("LoginFrame"), text="Logout")
        logout_button.grid(column=3, columnspan=2, row=3, padx=10, pady=20, sticky=tk.E)

class ViewBookingStaffFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=10)
        self.columnconfigure(0, weight=1)
        self.__createHeaderWithWidgets()
        self.__createContentWithWidgets()
        
    
    def __createHeaderWithWidgets(self):
        header = ttk.Frame(self)
        header.grid(row=0)
        current_page_label = ttk.Label(header, text="View Booking Staff", font=('Helvetica bold', 20))
        current_page_label.grid(row=0, column= 0, padx=50, pady=20)
        staff_name_label = ttk.Label(header, text="Staff Name:")
        staff_name_label.grid(row=0, column=1, padx=0, pady=20)
        staff_cinema_label = ttk.Label(header, text=" Staff Name [Staff Cinema]")
        staff_cinema_label.grid(row=0, column=2, padx=10, pady=20)
        menu_button = ttk.Button(header, command= lambda : app.showFrame("HomeFrame"), text="Menu")
        menu_button.grid(row=0, column=3, padx=50, pady=20, sticky=tk.E)

    def __createContentWithWidgets(self):
        content = ttk.Frame(self)
        content.grid(row=1)
        email = tk.StringVar()
        password = tk.StringVar()
        cinemaName = tk.StringVar()
        searchEmail = tk.StringVar()
        email_label = ttk.Label(content, text="Booking Staff Email:")
        email_label.grid(row=0, column=0, pady=20, padx=10)
        booking_staff_email_entry = ttk.Entry(content, textvariable=email)
        booking_staff_email_entry.grid(row=0, column=1, columnspan=2, pady=20, padx=10)
        password_label = ttk.Label(content, text="Booking Staff Password:")
        password_label.grid(row=1, column=0, pady=20, padx=10)
        booking_staff_password_entry = ttk.Entry(content, textvariable=password)
        booking_staff_password_entry.grid(row=1, column=1, columnspan=2, pady=20, padx=10)
        cinema_name_label = ttk.Label(content, text="Booking Staff Cinema:")
        cinema_name_label.grid(row=2, column=0, pady=20, padx=10)
        booking_staff_cinema_name_entry = ttk.Entry(content, textvariable=cinemaName)
        booking_staff_cinema_name_entry.grid(row=2, column=1, columnspan=2, pady=20, padx=10)
        add_booking_staff_button = ttk.Button(content, text="Add Booking Staff")
        add_booking_staff_button.grid(row=4, column=0, pady=20, padx=10)
        edit_booking_staff_button = ttk.Button(content, text="Edit Booking Staff")
        edit_booking_staff_button.grid(row=4, column=1, pady=20, padx=10)
        remove_booking_staff_button = ttk.Button(content, text="Remove Booking Staff")
        remove_booking_staff_button.grid(row=4, column=2, pady=20, padx=10)
        horizontal_line_label = ttk.Label(content, text="-------------------------------------------------------------------------------------------")
        horizontal_line_label.grid(row=5, column=0, columnspan=3)
        search_label = ttk.Label(content, text="Search Details by Email:")
        search_label.grid(row=6, column=0, pady=30, padx=10)
        search_email_entry = ttk.Entry(content, textvariable=searchEmail)
        search_email_entry.grid(row=6, column=2, columnspan=2, pady=20, padx=10)
        search_email_button = ttk.Button(content, text="Search")
        search_email_button.grid(row=7, column=0, columnspan=3, pady=10, padx=10)

class ViewAdminFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=10)
        self.columnconfigure(0, weight=1)
        self.__createHeaderWithWidgets()
        self.__createContentWithWidgets()
        
    
    def __createHeaderWithWidgets(self):
        header = ttk.Frame(self)
        header.grid(row=0)
        current_page_label = ttk.Label(header, text="View Admin", font=('Helvetica bold', 20))
        current_page_label.grid(row=0, column= 0, padx=50, pady=20)
        staff_name_label = ttk.Label(header, text="Staff Name:")
        staff_name_label.grid(row=0, column=1, padx=0, pady=20)
        staff_cinema_label = ttk.Label(header, text=" Staff Name [Staff Cinema]")
        staff_cinema_label.grid(row=0, column=2, padx=10, pady=20)
        menu_button = ttk.Button(header, command= lambda : app.showFrame("HomeFrame"), text="Menu")
        menu_button.grid(row=0, column=3, padx=50, pady=20, sticky=tk.E)

    def __createContentWithWidgets(self):
        content = ttk.Frame(self)
        content.grid(row=1)
        email = tk.StringVar()
        password = tk.StringVar()
        searchEmail = tk.StringVar()
        email_label = ttk.Label(content, text="Admin Email:")
        email_label.grid(row=0, column=0, pady=20, padx=10)
        admin_email_entry = ttk.Entry(content, textvariable=email)
        admin_email_entry.grid(row=0, column=1, columnspan=2, pady=20, padx=10)
        password_label = ttk.Label(content, text="Admin Password:")
        password_label.grid(row=1, column=0, pady=20, padx=10)
        admin_password_entry = ttk.Entry(content, textvariable=password)
        admin_password_entry.grid(row=1, column=1, columnspan=2, pady=20, padx=10)
        add_admin_button = ttk.Button(content, text="Add Admin")
        add_admin_button.grid(row=4, column=0, pady=20, padx=10)
        edit_admin_button = ttk.Button(content, text="Edit Admin")
        edit_admin_button.grid(row=4, column=1, pady=20, padx=10)
        remove_admin_button = ttk.Button(content, text="Remove Admin")
        remove_admin_button.grid(row=4, column=2, pady=20, padx=10)
        horizontal_line_label = ttk.Label(content, text="-------------------------------------------------------------------------------------------")
        horizontal_line_label.grid(row=5, column=0, columnspan=3)
        search_label = ttk.Label(content, text="Search Details by Email:")
        search_label.grid(row=6, column=0, pady=30, padx=10)
        search_email_entry = ttk.Entry(content, textvariable=searchEmail)
        search_email_entry.grid(row=6, column=2, columnspan=2, pady=20, padx=10)
        search_email_button = ttk.Button(content, text="Search")
        search_email_button.grid(row=7, column=0, columnspan=3, pady=10, padx=10)

class ViewFilmFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=10)
        self.columnconfigure(0, weight=1)
        self.__createHeaderWithWidgets()
        self.__createContentWithWidgets()
        
    
    def __createHeaderWithWidgets(self):
        header = ttk.Frame(self)
        header.grid(row=0)
        current_page_label = ttk.Label(header, text="View Film", font=('Helvetica bold', 20))
        current_page_label.grid(row=0, column= 0, padx=50, pady=20)
        staff_name_label = ttk.Label(header, text="Staff Name:")
        staff_name_label.grid(row=0, column=1, padx=0, pady=20)
        staff_cinema_label = ttk.Label(header, text=" Staff Name [Staff Cinema]")
        staff_cinema_label.grid(row=0, column=2, padx=10, pady=20)
        menu_button = ttk.Button(header, command= lambda : app.showFrame("HomeFrame"), text="Menu")
        menu_button.grid(row=0, column=3, padx=50, pady=20, sticky=tk.E)

    def __createContentWithWidgets(self):
        content = ttk.Frame(self)
        content.grid(row=1)
        filmID = tk.StringVar()
        filmName = tk.StringVar()
        filmDescription = tk.StringVar()
        filmActors = tk.StringVar()
        filmGenre = tk.StringVar()
        filmAge = tk.StringVar()
        filmRating = tk.StringVar()
        searchTitle = tk.StringVar()
        filmID_label = ttk.Label(content, text="Film ID:")
        filmID_label.grid(row=0, column=0, pady=10, padx=10)
        filmID_entry = ttk.Entry(content, textvariable=filmID)
        filmID_entry.grid(row=0, column=1, columnspan=2, pady=10, padx=10)
        film_title_label = ttk.Label(content, text="Film Title:")
        film_title_label.grid(row=1, column=0, pady=10, padx=10)
        film_title_entry = ttk.Entry(content, textvariable=filmName)
        film_title_entry.grid(row=1, column=1, columnspan=2, pady=10, padx=10)
        film_description_label = ttk.Label(content, text="Film Description:")
        film_description_label.grid(row=2, column=0, pady=10, padx=10)
        film_description_entry = ttk.Entry(content, textvariable=filmDescription)
        film_description_entry.grid(row=2, column=1, columnspan=2, pady=10, padx=10)
        film_actors_label = ttk.Label(content, text="Film Actors:")
        film_actors_label.grid(row=3, column=0, pady=10, padx=10)
        film_actors_entry = ttk.Entry(content, textvariable=filmActors)
        film_actors_entry.grid(row=3, column=1, columnspan=2, pady=10, padx=10)
        film_genre_label = ttk.Label(content, text="Film Genre:")
        film_genre_label.grid(row=4, column=0, pady=10, padx=10)
        film_genre_entry = ttk.Entry(content, textvariable=filmGenre)
        film_genre_entry.grid(row=4, column=1, columnspan=2, pady=10, padx=10)
        film_age_label = ttk.Label(content, text="Film Age:")
        film_age_label.grid(row=5, column=0, pady=10, padx=10)
        film_age_entry = ttk.Entry(content, textvariable=filmAge)
        film_age_entry.grid(row=5, column=1, columnspan=2, pady=10, padx=10)
        film_rating_label = ttk.Label(content, text="Film Rating:")
        film_rating_label.grid(row=6, column=0, pady=10, padx=10)
        film_age_entry = ttk.Entry(content, textvariable=filmRating)
        film_age_entry.grid(row=6, column=1, columnspan=2, pady=10, padx=10)

        add_film_button = ttk.Button(content, text="Add Film")
        add_film_button.grid(row=7, column=0, pady=20, padx=10)
        edit_film_button = ttk.Button(content, text="Edit Film")
        edit_film_button.grid(row=7, column=1, pady=20, padx=10)
        remove_film_button = ttk.Button(content, text="Remove Film")
        remove_film_button.grid(row=7, column=2, pady=20, padx=10)
        horizontal_line_label = ttk.Label(content, text="-------------------------------------------------------------------------------------------")
        horizontal_line_label.grid(row=8, column=0, columnspan=3)
        search_label = ttk.Label(content, text="Search Film Details by Title:")
        search_label.grid(row=9, column=0, pady=10, padx=10)
        search_title_entry = ttk.Entry(content, textvariable=searchTitle)
        search_title_entry.grid(row=9, column=2, columnspan=2, pady=20, padx=10)
        search_title_button = ttk.Button(content, text="Search")
        search_title_button.grid(row=10, column=0, columnspan=3, pady=10, padx=10)
        text_fill_label = ttk.Label(content, text="""
        



        """)
        text_fill_label.grid(row=11, column=0, columnspan=3)

class AddCinemasFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=10)
        self.columnconfigure(0, weight=1)
        self.__createHeaderWithWidgets()
        self.__createContentWithWidgets()
        
    
    def __createHeaderWithWidgets(self):
        header = ttk.Frame(self)
        header.grid(row=0)
        current_page_label = ttk.Label(header, text="Add Cinema/City", font=('Helvetica bold', 20))
        current_page_label.grid(row=0, column= 0, padx=50, pady=20)
        staff_name_label = ttk.Label(header, text="Staff Name:")
        staff_name_label.grid(row=0, column=1, padx=0, pady=20)
        staff_cinema_label = ttk.Label(header, text=" Staff Name [Staff Cinema]")
        staff_cinema_label.grid(row=0, column=2, padx=10, pady=20)
        menu_button = ttk.Button(header, command= lambda : app.showFrame("HomeFrame"), text="Menu")
        menu_button.grid(row=0, column=3, padx=50, pady=20, sticky=tk.E)

    def __createContentWithWidgets(self):
        content = ttk.Frame(self)
        content.grid(row=1)
        cinemaCity = tk.StringVar()
        cinemaName = tk.StringVar()
        addCityName = tk.StringVar()
        morningPrice = tk.StringVar()
        afternoonPrice = tk.StringVar()
        eveningPrice = tk.StringVar()
        cinema_city_label = ttk.Label(content, text="Cinema City:")
        cinema_city_label.grid(row=0, column=0, pady=20, padx=10)
        cinema_city_entry = ttk.Entry(content, textvariable=cinemaCity)
        cinema_city_entry.grid(row=0, column=1, columnspan=2, pady=20, padx=10)
        cinema_name_label = ttk.Label(content, text="Cinema Name:")
        cinema_name_label.grid(row=1, column=0, pady=20, padx=10)
        cinema_name_entry = ttk.Entry(content, textvariable=cinemaName)
        cinema_name_entry.grid(row=1, column=1, columnspan=2, pady=20, padx=10)
        add_cinema_button = ttk.Button(content, text="Add Cinema")
        add_cinema_button.grid(row=2, column=0, columnspan=3, pady=20, padx=10)
        horizontal_line_label = ttk.Label(content, text="-------------------------------------------------------------------------------------------")
        horizontal_line_label.grid(row=3, column=0, columnspan=3)
        city_label = ttk.Label(content, text="City Name:")
        city_label.grid(row=4, column=0, pady=20, padx=10)
        city_entry = ttk.Entry(content, textvariable=addCityName)
        city_entry.grid(row=4, column=1, columnspan=2, pady=10, padx=10)
        city_morning_price_label = ttk.Label(content, text="Morning Price:")
        city_morning_price_label.grid(row=5, column=0, pady=10, padx=10)
        city_morning_price_entry = ttk.Entry(content, textvariable=morningPrice)
        city_morning_price_entry.grid(row=5, column=1, columnspan=2, pady=10, padx=10)
        city_afternoon_price_label = ttk.Label(content, text="Afternoon Price:")
        city_afternoon_price_label.grid(row=6, column=0, pady=10, padx=10)
        city_afternoon_price_entry = ttk.Entry(content, textvariable=afternoonPrice)
        city_afternoon_price_entry.grid(row=6, column=1, columnspan=2, pady=10, padx=10)
        city_evening_price_label = ttk.Label(content, text="Evening Price:")
        city_evening_price_label.grid(row=7, column=0, pady=10, padx=10)
        city_evening_price_entry = ttk.Entry(content, textvariable=eveningPrice)
        city_evening_price_entry.grid(row=7, column=1, columnspan=2, pady=10, padx=10)
        add_city_button = ttk.Button(content, text="Add City")
        add_city_button.grid(row=8, column=0, columnspan=3, pady=10, padx=10)

class GenerateReportFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=10)
        self.columnconfigure(0, weight=1)
        self.__createHeaderWithWidgets()
        self.__createContentWithWidgets()
        
    
    def __createHeaderWithWidgets(self):
        header = ttk.Frame(self)
        header.grid(row=0)
        current_page_label = ttk.Label(header, text="Generate Report", font=('Helvetica bold', 20))
        current_page_label.grid(row=0, column= 0, padx=50, pady=20)
        staff_name_label = ttk.Label(header, text="Staff Name:")
        staff_name_label.grid(row=0, column=1, padx=0, pady=20)
        staff_cinema_label = ttk.Label(header, text=" Staff Name [Staff Cinema]")
        staff_cinema_label.grid(row=0, column=2, padx=10, pady=20)
        menu_button = ttk.Button(header, command= lambda : app.showFrame("HomeFrame"), text="Menu")
        menu_button.grid(row=0, column=3, padx=50, pady=20, sticky=tk.E)

    def __createContentWithWidgets(self):
        content = ttk.Frame(self)
        content.grid(row=1)
        reportType = tk.StringVar()
        reportParameter = tk.StringVar()
        filler_label = ttk.Label(content, text="""
        
        
        
        
        
        """)
        filler_label.grid(row=0, column=0)
        report_information_label = ttk.Label(content, text="""
        Report ID 1: List of Staff and The Number of Bookings They Have Created for the Month. (Parameter = Desired Month)
        Report ID 2: Number of Bookings for a Screening. (Parameter: Screening ID)
        Report ID 3: Total Monthly Revenue for Each Cinema. (Parameter: N/A)
        Report ID 4: Film Generating the Most Revenue.
        """, font=('Helvetica bold', 10))
        report_information_label.grid(row=1, column=0, columnspan=3, sticky=tk.N)
        generate_report_label = ttk.Label(content, text="Enter Report ID:")
        generate_report_label.grid(row=2, column=0, pady=10, padx=10)
        generate_report_entry = ttk.Entry(content, textvariable=reportType)
        generate_report_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
        report_parameter_label = ttk.Label(content, text="Enter Report Parameter:")
        report_parameter_label.grid(row=3, column=0, pady=10, padx=10)
        report_parameter_entry = ttk.Entry(content, textvariable=reportParameter)
        report_parameter_entry.grid(row=3, column=1, columnspan=2, padx=10, pady=10)
        generate_report_button = ttk.Button(content, text="Generate Report")
        generate_report_button.grid(row=4, column=0, columnspan=3)
        report_listbox = tk.Listbox(self)
        report_listbox.place(height=200, width=200, x=500, y=200)
        report_listbox1 = tk.Listbox(self)
        report_listbox1.place(height=200, width=200, x=700, y=200)
        
        
class ViewFilmListingsFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=10)
        self.columnconfigure(0, weight=1)
        self.__createHeaderWithWidgets()
        self.__createContentWithWidgets()
        
    
    def __createHeaderWithWidgets(self):
        header = ttk.Frame(self)
        header.grid(row=0)
        current_page_label = ttk.Label(header, text="View Film Listings", font=('Helvetica bold', 20))
        current_page_label.grid(row=0, column= 0, padx=50, pady=20)
        staff_name_label = ttk.Label(header, text="Staff Name:")
        staff_name_label.grid(row=0, column=1, padx=0, pady=20)
        staff_cinema_label = ttk.Label(header, text=" Staff Name [Staff Cinema]")
        staff_cinema_label.grid(row=0, column=2, padx=10, pady=20)
        menu_button = ttk.Button(header, command= lambda : app.showFrame("HomeFrame"), text="Menu")
        menu_button.grid(row=0, column=3, padx=50, pady=20, sticky=tk.E)

    def __createContentWithWidgets(self):
        content = ttk.Frame(self)
        content.grid(row=1)
        filmName = tk.StringVar()
        cinemaName = tk.StringVar()
  
        film_name_label = ttk.Label(content, text="Film Name:")
        film_name_label.grid(row=0, column=0, padx=10, pady=10)
        film_name_entry = ttk.Entry(content, textvariable=filmName)
        film_name_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=10)
        cinema_name_label = ttk.Label(content, text="Cinema Name:")
        cinema_name_label.grid(row=1, column=0, padx=10, pady=10)
        cinema_name_entry = ttk.Entry(content, textvariable=cinemaName)
        cinema_name_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

        show_listings_button = ttk.Button(content, text="Show Listings")
        show_listings_button.grid(row=2, column=0, columnspan=3)
        text_fill_label = ttk.Label(content, text="""
        






        


        """)
        text_fill_label.grid(row=3, column=0, columnspan=3)
        listings_listbox = tk.Listbox(self)
        listings_listbox.place(height=300, width=200, x=200, y=400)
        listings_listbox1 = tk.Listbox(self)
        listings_listbox1.place(height=300, width=200, x=400, y=400)
        listings_listbox2 = tk.Listbox(self)
        listings_listbox2.place(height=300, width=500, x=600, y=400)

class CreateBookingFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=10)
        self.columnconfigure(0, weight=1)
        self.__createHeaderWithWidgets()
        self.__createContentWithWidgets()
        
    
    def __createHeaderWithWidgets(self):
        header = ttk.Frame(self)
        header.grid(row=0)
        current_page_label = ttk.Label(header, text="Create Booking", font=('Helvetica bold', 20))
        current_page_label.grid(row=0, column= 0, padx=50, pady=20)
        staff_name_label = ttk.Label(header, text="Staff Name:")
        staff_name_label.grid(row=0, column=1, padx=0, pady=20)
        staff_cinema_label = ttk.Label(header, text=" Staff Name [Staff Cinema]")
        staff_cinema_label.grid(row=0, column=2, padx=10, pady=20)
        menu_button = ttk.Button(header, command= lambda : app.showFrame("HomeFrame"), text="Menu")
        menu_button.grid(row=0, column=3, padx=50, pady=20, sticky=tk.E)

    def __createContentWithWidgets(self):
        content = ttk.Frame(self)
        content.grid(row=1)

        bookingDate = tk.StringVar()
        bookingFilm = tk.StringVar()
        bookingShowing = tk.StringVar()
        bookingSeatType = tk.IntVar()
        bookingNumOfTickets = tk.IntVar()
        bookingCustomerName = tk.StringVar()
        bookingCustomerPhone = tk.StringVar()
        bookingCustomerEmail = tk.StringVar
        bookingCardNum = tk.IntVar()
        bookingExpiry = tk.StringVar()
        bookingCVV = tk.IntVar()

        # TODO: WHEN GETTING OPTIONS FROM DATABASE/CLASSES
        # TODO: PUT RESULT OF FETCH IN LIST AND USE LIST AS OPTIONS
        # TODO: WHEN ONE COMBOBOX CHANGES UPDATE OTHER COMBO BOX OPTIONS ACCORDINGLY
        dates = ('15/05/2000', '15/02/2001', '20/07/1990') 
        select_date_label = ttk.Label(content, text="Select Date:")
        select_date_label.grid(row=0, column=0, padx=5, pady=(0, 40))
        select_date_combobox = ttk.Combobox(content, textvariable=bookingDate)
        select_date_combobox.grid(row=0, column=1, padx=5, pady=(0, 40))
        select_date_combobox['values'] = dates
        select_date_combobox['state'] = 'readonly'

        films = ('Film1', 'Film2', 'Film3')
        select_film_label = ttk.Label(content, text="Select Film:")
        select_film_label.grid(row=0, column=2, padx=10, pady=(0, 40))
        select_film_combobox = ttk.Combobox(content, textvariable=bookingFilm)
        select_film_combobox.grid(row=0, column=3, padx=5, pady=(0, 40))
        select_film_combobox['values'] = films
        select_film_combobox['state'] = 'readonly'

        showings = ('Showing1', 'Showing2', 'Showing3')
        select_showing_label = ttk.Label(content, text="Select Showing:")
        select_showing_label.grid(row=0, column=4, padx=10, pady=(0, 40))
        select_showing_combobox = ttk.Combobox(content, textvariable=bookingShowing)
        select_showing_combobox.grid(row=0, column=5, padx=5, pady=(0, 40))
        select_showing_combobox['values'] = showings
        select_showing_combobox['state'] = 'readonly'

        select_ticket_type_label = ttk.Label(content, text="Select Ticket Type:")
        select_ticket_type_label.grid(row=1, column=0, padx=5, pady=(0, 40))
        lower_hall_ticket_radio_button = ttk.Radiobutton(content, text="Lower Hall", value=1, variable=bookingSeatType)
        lower_hall_ticket_radio_button.grid(row=1, column=1, padx=5, pady=(0, 40))
        upper_hall_ticket_radio_button = ttk.Radiobutton(content, text="Upper Hall", value=2, variable=bookingSeatType)
        upper_hall_ticket_radio_button.grid(row=1, column=2, padx=5, pady=(0, 40))
        VIP_ticket_radio_button = ttk.Radiobutton(content, text="VIP", value=3, variable=bookingSeatType)
        VIP_ticket_radio_button.grid(row=1, column=3, padx=5, pady=(0, 40))

        booking_num_of_tickets_label = ttk.Label(content, text="Number of Tickets:")
        booking_num_of_tickets_label.grid(row=1, column=4, padx=5, pady=(0, 40))
        booking_num_of_ticekts_entry = ttk.Entry(content, textvariable=bookingNumOfTickets)
        booking_num_of_ticekts_entry.grid(row=1, column=5, padx=5, pady=(0, 40))

        check_availability_price_button = ttk.Button(content, text="Check Availability/Price")
        check_availability_price_button.grid(row=2, column=0, columnspan=6, padx=5, pady=(0, 80))

        customer_name_label = ttk.Label(content, text="Customer Name:")
        customer_name_label.grid(row=3, column=0,padx=5, pady=(0, 40))
        customer_name_entry = ttk.Entry(content, textvariable=bookingCustomerName)
        customer_name_entry.grid(row=3, column=1, padx=5, pady=(0, 40))

        customer_phone_label = ttk.Label(content, text="Customer Phone:")
        customer_phone_label.grid(row=3, column=2,padx=5, pady=(0, 40))
        customer_phone_entry = ttk.Entry(content, textvariable=bookingCustomerPhone)
        customer_phone_entry.grid(row=3, column=3, padx=5, pady=(0, 40))

        customer_email_label = ttk.Label(content, text="Customer Email:")
        customer_email_label.grid(row=3, column=4, padx=5, pady=(0, 40))
        customer_email_entry = ttk.Entry(content, textvariable=bookingCustomerEmail)
        customer_email_entry.grid(row=3, column=5, padx=5, pady=(0, 40))

        card_num_label = ttk.Label(content, text="Card #:")
        card_num_label.grid(row=4, column=0, padx=5, pady=(0, 40))
        card_num_entry = ttk.Entry(content, textvariable=bookingCardNum)
        card_num_entry.grid(row=4, column=1, padx=5, pady=(0, 40))

        card_exp_label = ttk.Label(content, text="Card Expiry:")
        card_exp_label.grid(row=5, column=0, padx=5, pady=(0, 40))
        card_exp_entry = ttk.Entry(content, textvariable=bookingExpiry)
        card_exp_entry.grid(row=5, column=1, padx=5, pady=(0, 40))

        cvv_label = ttk.Label(content, text="CVV:")
        cvv_label.grid(row=5, column=2, padx=5, pady=(0, 40))
        cvv_entry = ttk.Entry(content, textvariable=bookingCVV)
        cvv_entry.grid(row=5, column=3, padx=5, pady=(0, 40))

        create_booking_button = ttk.Button(content, text="Create Booking/Get Receipt")
        create_booking_button.grid(row=6, column=0, columnspan=6, padx=5, pady=(0, 80))

class CancelBookingFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=10)
        self.columnconfigure(0, weight=1)
        self.__createHeaderWithWidgets()
        self.__createContentWithWidgets()
        
    
    def __createHeaderWithWidgets(self):
        header = ttk.Frame(self)
        header.grid(row=0)
        current_page_label = ttk.Label(header, text="Cancel Booking", font=('Helvetica bold', 20))
        current_page_label.grid(row=0, column= 0, padx=50, pady=20)
        staff_name_label = ttk.Label(header, text="Staff Name:")
        staff_name_label.grid(row=0, column=1, padx=0, pady=20)
        staff_cinema_label = ttk.Label(header, text=" Staff Name [Staff Cinema]")
        staff_cinema_label.grid(row=0, column=2, padx=10, pady=20)
        menu_button = ttk.Button(header, command= lambda : app.showFrame("HomeFrame"), text="Menu")
        menu_button.grid(row=0, column=3, padx=50, pady=20, sticky=tk.E)

    def __createContentWithWidgets(self):
        content = ttk.Frame(self)
        content.grid(row=1)

        bookingID = tk.StringVar()

        booking_id_label = ttk.Label(content, text="Booking ID:")
        booking_id_label.grid(row=0, column=0, padx=5, pady=(0, 100))
        booking_id_entry = ttk.Entry(content, textvariable=bookingID)
        booking_id_entry.grid(row=0, column=1, padx=5, pady=(0, 100))

        cancel_booking_button = ttk.Button(content, text="Cancel Booking")
        cancel_booking_button.grid(row=1, column=0, columnspan=2)

class ViewCinemaScreeningsFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=10)
        self.columnconfigure(0, weight=1)
        self.__createHeaderWithWidgets()
        self.__createContentWithWidgets()
        
    
    def __createHeaderWithWidgets(self):
        header = ttk.Frame(self)
        header.grid(row=0)
        current_page_label = ttk.Label(header, text="View Screenings", font=('Helvetica bold', 20))
        current_page_label.grid(row=0, column= 0, padx=50, pady=20)
        staff_name_label = ttk.Label(header, text="Staff Name:")
        staff_name_label.grid(row=0, column=1, padx=0, pady=20)
        staff_cinema_label = ttk.Label(header, text=" Staff Name [Staff Cinema]")
        staff_cinema_label.grid(row=0, column=2, padx=10, pady=20)
        menu_button = ttk.Button(header, command= lambda : app.showFrame("HomeFrame"), text="Menu")
        menu_button.grid(row=0, column=3, padx=50, pady=20, sticky=tk.E)

    def __createContentWithWidgets(self):
        content = ttk.Frame(self)
        content.grid(row=1)
        




if __name__ == "__main__":
    app = App()
    app.mainloop()