import re
from DatabaseAccess import *
from datetime import *

conn = getConn()
cur = getCursor()

class LoginModel:
    def __init__(self):
        self.__email = ""
        self.__password = ""

    def getEmail(self):
        return self.__email

    def getPassword(self):
        return self.__password

    def setEmail(self, email):
        if self.validateEmailSyntax(email):
            self.__email = email
            return 1
        else:
            return 0

    def setPassword(self, password):
        if self.validatePasswordSyntax(password):
            self.__password = password
            return 1
        else:
            return 0

    def validateEmailSyntax(self, email):
        if len(email) > 0:
            pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if re.fullmatch(pattern, email):
                return 1
            else:
                return 0
        else: 
            return 0

    def validatePasswordSyntax(self, password):
        if len(password) > 0:
            pattern = r'[A-Za-z0-9 ]{5,}'
            if re.fullmatch(pattern, password):
                return 1
            else:
                return 0
        else:
            return 0

    def checkAccountInDB(self, email, password):
        query = 'SELECT email, password FROM Users WHERE email = ? AND password = ?'
        cur.execute(query, (email, password))
        record = cur.fetchall()
        if len(record) > 0:
            print("Account found")
            return 1
        else:
            print("Account not found")
            return 0

    def getAccountUserType(self, email, password):
        query = 'SELECT user_type FROM Users WHERE email = ? AND password = ?'
        cur.execute(query, (email, password))
        record = cur.fetchone()
        userType = int(''.join(map(str, record)))
        print(userType)
        return userType
    
    def getAccountCinema(self, email, password):
        query = 'SELECT user_cinema FROM Users WHERE email = ? AND password = ?'
        cur.execute(query, (email, password))
        record = cur.fetchone()
        if record != None:
            userCinema = ''.join(map(str, record))
            print(userCinema)
            return userCinema
        else:
            userCinema = None
            return userCinema

class ViewFilmListingsModel:
    def __init__(self):
        self.__filmName = ""
        self.__cinemaName = ""

    def validateFilmNameSyntax(self, filmName):
        if len(filmName) > 0:
            pattern = r'[A-Za-z0-9 ]{0,50}' #Letters/numbers and up to 50 char
            if re.fullmatch(pattern, filmName):
                return 1
            else:
                return 0
        else:
            return 0
    
    def validateCinemaNameSyntax(self, cinemaName):
        if len(cinemaName) > 0:
            pattern = r'[A-Za-z ]{0,50}' #Letters and up to 50 char
            if re.fullmatch(pattern, cinemaName):
                return 1
            else:
                return 0
        else:
            return 0

    def checkForScreenings(self, filmName, cinemaName):
        query = 'SELECT film_name, cinema_name FROM FilmScreenings WHERE film_name = ? AND cinema_name = ?'
        cur.execute(query, (filmName, cinemaName))
        record = cur.fetchall()
        if len(record) > 0:
            print("Screenings found.")
            return 1
        else:
            print("Screenings not found.")
            return 0

    def returnScreeningsInfo(self, filmName, cinemaName):
        query = 'SELECT screening_time, screening_date, screening_screen FROM FilmScreenings WHERE film_name = ? AND cinema_name = ? ORDER BY screening_date, screening_time ASC'
        cur.execute(query, (filmName, cinemaName))
        screeningsInfo = cur.fetchall()
        print(screeningsInfo)
        return screeningsInfo

class CreateBookingModel:
    def __init__(self):
        self.__seatType = ""
        self.__seatNumbers = ""
        self.__customerName = ""
        self.__cinemaName = ""
    
    def validateCinemaNameSyntax(self, cinemaName):
        if len(cinemaName) > 0:
            pattern = r'[A-Za-z ]{0,50}' #Letters and up to 50 char
            if re.fullmatch(pattern, cinemaName):
                return 1
            else:
                return 0
        else:
            return 0
    
    def validateFilmNameSyntax(self, filmName):
        if len(filmName) > 0:
            pattern = r'[A-Za-z0-9 ]{0,50}' #Letters/numbers and up to 50 char
            if re.fullmatch(pattern, filmName):
                return 1
            else:
                return 0
        else:
            return 0
   
    def checkForFilms(self, cinemaName):
        query = 'SELECT DISTINCT film_name FROM FilmScreenings WHERE cinema_name = ?'
        cur.execute(query, (cinemaName,))
        record = cur.fetchall()
        if len(record) > 0:
            print("Films found.")
            return 1
        else:
            print("Films not found.")
            return 0

    #function to return a fetch of all films in a given cinema to be put in combobox   
    def returnFilms(self, cinemaName):
        query = 'SELECT DISTINCT film_name FROM FilmScreenings WHERE cinema_name = ?'
        cur.execute(query, (cinemaName,)) #NOTE: have to have the execute layed out like this when only using 1 parameter
        films = cur.fetchall()            # very wierd but have to have (cinemaName, ) and not just cinemaName
        return films
    
    def checkForDates(self, filmName, cinemaName):
        query = 'SELECT screening_date FROM FilmScreenings WHERE film_name = ? AND cinema_name = ?'
        cur.execute(query, (filmName,cinemaName))
        record = cur.fetchall()
        if len(record) > 0:
            print('Dates found.')
            return 1
        else:
            print('No dates found.')
            return 0
        
    def returnDates(self, filmName, cinemaName):
        query = 'SELECT DISTINCT screening_date FROM FilmScreenings WHERE film_name = ? AND cinema_name = ?'
        cur.execute(query, (filmName,cinemaName)) 
        dates = cur.fetchall()
        return dates
    
    def checkForShowings(self, filmDate, filmName, cinemaName):
        query = 'SELECT screening_time FROM FilmScreenings WHERE film_name = ? AND cinema_name = ? AND screening_date = ?'
        cur.execute(query, (filmName, cinemaName, filmDate))
        records = cur.fetchall()
        if len(records) > 0:
            print('Showings found.')
            return 1
        else:
            print('No showings found')
            return 0
    
    def returnShowings(self, filmDate, filmName, cinemaName):
        query = 'SELECT DISTINCT screening_time FROM FilmScreenings WHERE film_name = ? AND cinema_name = ? AND screening_date = ?'
        cur.execute(query, (filmName, cinemaName, filmDate))
        showings = cur.fetchall()
        return showings

    def checkForTickets(self, showing, filmDate, filmName, cinemaName):
        query = 'SELECT lower_hall_tickets_left, upper_hall_tickets_left, VIP_tickets_left FROM FilmScreenings WHERE screening_time = ? AND film_name = ? AND cinema_name = ? AND screening_date = ?'
        cur.execute(query, (showing, filmName, cinemaName, filmDate))
        records = cur.fetchall()
        if len(records) > 0:
            print('Tickets found.')
            return 1
        else:
            print('No tickets found.')
            return 0
        
    def returnTickets(self, showing, filmDate, filmName, cinemaName):
        query = 'SELECT lower_hall_tickets_left, upper_hall_tickets_left, VIP_tickets_left FROM FilmScreenings WHERE screening_time = ? AND film_name = ? AND cinema_name = ? AND screening_date = ?'
        cur.execute(query, (showing, filmName, cinemaName, filmDate))
        tickets = cur.fetchall()
        return tickets
    
    def getPrices(self, cinemaName):
        query = 'SELECT city_name FROM Cinemas WHERE cinema_name = ?'
        cur.execute(query, (cinemaName, ))
        city = cur.fetchone()
        query = 'SELECT morning_price, afternoon_price, evening_price FROM Cities WHERE city_name = ?'
        cur.execute(query, (city[0], ))
        prices = cur.fetchone()
        return prices

    def getScreeningID(self, time, date, name, cinema):
        query = 'SELECT screeningID FROM FilmScreenings WHERE screening_time = ? AND screening_date = ? AND film_name = ? AND cinema_name = ?'
        cur.execute(query, (time, date, name, cinema))
        screeningID = cur.fetchone()
        return screeningID[0]

    def createBooking(self, bookingID, seatType, seatNums, price, numOfTickets, screeningID):
        cur.execute("SELECT bookingID FROM Bookings")
        bookings = cur.fetchall()
        query = '''INSERT INTO Bookings (bookingID, seat_type, seat_numbers, price, number_of_tickets, screeningID)
        VALUES (?, ?, ? ,?, ?, ?)'''
        cur.execute(query, (bookingID, seatType, seatNums, price, numOfTickets, screeningID))
        cur.execute("SELECT bookingID FROM Bookings")
        bookings1 = cur.fetchall()
        if len(bookings1) - len(bookings) == 1:
            print("booking added to database")
            #removing seats booked from database
            if seatType == 1:
                query = "SELECT lower_hall_tickets_left FROM FilmScreenings WHERE screeningID = ?"
                cur.execute(query, (screeningID,))
                tickets = cur.fetchone()
                ticketsRemaining = tickets[0] - numOfTickets
                query = "UPDATE FilmScreenings SET lower_hall_tickets_left = ? WHERE screeningID = ? "
                cur.execute(query, (ticketsRemaining, screeningID))
                conn.commit()
            if seatType == 2:
                query = "SELECT upper_hall_tickets_left FROM FilmScreenings WHERE screeningID = ?"
                cur.execute(query, (screeningID,))
                tickets = cur.fetchone()
                ticketsRemaining = tickets[0] - numOfTickets
                query = "UPDATE FilmScreenings SET upper_hall_tickets_left = ? WHERE screeningID = ? "
                cur.execute(query, (ticketsRemaining, screeningID))
                conn.commit()
            if seatType == 3:
                query = "SELECT VIP_tickets_left FROM FilmScreenings WHERE screeningID = ?"
                cur.execute(query, (screeningID,))
                tickets = cur.fetchone()
                ticketsRemaining = tickets[0] - numOfTickets
                query = "UPDATE FilmScreenings SET VIP_tickets_left = ? WHERE screeningID = ? "
                cur.execute(query, (ticketsRemaining, screeningID))
                conn.commit()
            return 1
        else:
            return 0
        
    def getScreeningScreen(self, screeningID):
        query = "SELECT screening_screen FROM FilmScreenings WHERE screeningID = ?"
        cur.execute(query, (screeningID,))
        screeningScreen = cur.fetchone()
        return screeningScreen[0]
class GenerateReportModel:
    def __init__(self):
        self.__reportType = ""
        self.__reportParameter = ""

    def validateReportTypeSyntax(self, reportType):
        if len(reportType) > 0:
            pattern = r'[1-4]' #Numbers, up to 4, increase if you wish to have more reports
            if re.fullmatch(pattern, reportType):
                return 1
            else:
                return 0
        else:
            return 0

    def validateReportParameterSyntax(self, reportType, reportParameter):
        if reportType == 3 and len(reportParameter) == 0:
            return 1
        if len(reportParameter) > 0:
            pattern = r'[1-4]' #Numbers, up to 4, increase if you wish to have more reports
            if re.fullmatch(pattern, reportType):
                return 1
            else:
                return 0
        else:
            return 0

    def checkReportReturnsInfo(self, reportType, reportParameter):
        #TODO: Make all of these functional, maybe change reports to something easier
        if reportType == 1:
            pass
        if reportType == 2:
            #Getting all bookings for given screening ID to check if any bookings have been made
            query = "SELECT bookingID FROM Bookings WHERE screeningID = ?"
            cur.execute(query, (reportParameter, ))
            result = cur.fetchall()
            print(result)
            if len(result) > 0:
                print("Found results.")
                return 1
            else:
                return 0
        if reportType == 3:
            pass
        if reportType == 4:
            pass
    
    def returnReportInfo(self, reportType, reportParameter):
        #TODO: Make all of these functional, maybe change reports to something easier
        if reportType == 1:
            pass
        if reportType == 2:
            #Getting the count of bookings under a given screening ID
            query = "SELECT screeningID, COUNT(*) FROM Bookings WHERE screeningID = ?"
            cur.execute(query, (reportParameter, ))
            reportInfo = cur.fetchall()
            return reportInfo
        if reportType == 3:
            pass
        if reportType == 4:
            pass




class CancelBookingModel():
    def checkBookingID(self, bookingID):
        query = "SELECT * FROM Bookings WHERE bookingID = ?"
        cur.execute(query, (bookingID,))
        records = cur.fetchall()
        if len(records) > 0:
            return 1
        else: 
            return 0

    def checkCancelTime(self, screeningID):
        query = "SELECT screening_date FROM FilmScreenings WHERE screeningID = ?"
        cur.execute(query, (screeningID,))
        dates = cur.fetchone()
        holder = date.today()
        today = holder.strftime("%d/%m/%Y")
        today = datetime.strptime(today, "%d/%m/%Y")
        bookingDate = datetime.strptime(dates[0], "%d/%m/%Y")
        difference = bookingDate - today
        if int(difference.days) >= 1:
            return 1
        else:
            return 0
    
    def getBooking(self, bookingID):
        query = "SELECT * FROM Bookings WHERE bookingID = ?"
        cur.execute(query, (bookingID,))
        bookingInfo = cur.fetchone()
        return bookingInfo

    def removeBooking(self, bookingID):
        query = "SELECT * FROM Bookings WHERE bookingID = ?"
        cur.execute(query, (bookingID,))
        bookingsBefore = cur.fetchall()
        query = "DELETE FROM Bookings WHERE bookingID = ?"
        cur.execute(query, (bookingID,))
        conn.commit
        query = "SELECT * FROM Bookings WHERE bookingID = ?"
        cur.execute(query, (bookingID,))
        bookingsAfter = cur.fetchall()
        if  len(bookingsBefore) - len(bookingsAfter) == 1:
            return 1
        else: 
            return 0

    def updateTickets(self, numOfTickets, seatType, screeningID):
        print(numOfTickets, seatType, screeningID)
        if seatType == "1":
            query = "SELECT lower_hall_tickets_left FROM FilmScreenings WHERE screeningID = ?"
            cur.execute(query, (screeningID,))
            tickets = cur.fetchone()
            ticketsRemaining = tickets[0] + numOfTickets
            query = "UPDATE FilmScreenings SET lower_hall_tickets_left = ? WHERE screeningID = ? "
            cur.execute(query, (ticketsRemaining, screeningID))
            conn.commit()
            return 1
        elif seatType == "2":
            query = "SELECT upper_hall_tickets_left FROM FilmScreenings WHERE screeningID = ?"
            cur.execute(query, (screeningID,))
            tickets = cur.fetchone()
            ticketsRemaining = tickets[0] + numOfTickets
            query = "UPDATE FilmScreenings SET upper_hall_tickets_left = ? WHERE screeningID = ? "
            cur.execute(query, (ticketsRemaining, screeningID))
            conn.commit()
            return 1
        elif seatType == "3":
            query = "SELECT VIP_tickets_left FROM FilmScreenings WHERE screeningID = ?"
            cur.execute(query, (screeningID,))
            tickets = cur.fetchone()
            ticketsRemaining = tickets[0] + numOfTickets
            query = "UPDATE FilmScreenings SET VIP_tickets_left = ? WHERE screeningID = ? "
            cur.execute(query, (ticketsRemaining, screeningID))
            conn.commit()
            return 1
        else:
            return 0
