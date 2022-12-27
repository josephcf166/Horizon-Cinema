from HorizonModel import *

class LoginController:
    def __init__(self, model, view):
        self.model = model 
        self.view = view

    def login(self, email, password):
        try:
            if self.model.validateEmailSyntax(email):
                if self.model.validatePasswordSyntax(password):
                    if self.model.checkAccountInDB(email, password):
                        print("Account found.")
                        userType = self.model.getAccountUserType(email, password)
                        accountCinema = self.model.getAccountCinema(email, password)
                        self.view.loginSuccess(f'Logged in as {email}.', userType, accountCinema)
                    else:
                        print("Could not find account.")
                        self.view.loginFailed('Could not find account.')
                else:
                    print("Password syntax incorrect.")
                    self.view.loginFailed('Password syntax incorrect.')
            else:
                print("Email syntax incorrect.")
                self.view.loginFailed('Email syntax incorrect.')
        except ValueError as error:
            self.view.loginFailed(error)

class ViewFilmListingsController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def searchListings(self, filmName, cinemaName):
        try:
            if self.model.validateFilmNameSyntax(filmName):
                if self.model.validateCinemaNameSyntax(cinemaName):
                    if self.model.checkForScreenings(filmName, cinemaName):
                        screeningInfo = self.model.returnScreeningsInfo(filmName, cinemaName)
                        self.view.searchSuccess('Displaying Screenings for ' + str(filmName) + ' at ' + str(cinemaName) + '.', screeningInfo)
                    else:
                        self.view.searchFailed('No screenings found.')
                else:
                    self.view.searchFailed('Cinema name syntax incorrect.')
            else:
                print("Film name syntax incorrect.")
                self.view.searchFailed('Film name syntax incorrect.')
        except ValueError as error:
            pass


class CreateBookingController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    #function to fetch films to show in combobox
    def searchFilm(self, cinemaName):
        try:
            if self.model.validateCinemaNameSyntax(cinemaName):
                if self.model.checkForFilms(cinemaName):
                    films = self.model.returnFilms(cinemaName)
                    self.view.searchSuccess('Displaying films at ' + str(cinemaName) + '.', films)
                else:
                    #self.view.searchFailed('No films found.')
                    print("no films")
            else:
                self.view.searchFailed('Cinema name syntax incorrect.')
        except ValueError as error:
            pass
