from tkinter import ttk, Entry, Button
from sqlalchemy.orm import Session

from UI.tabs.exceptionsMess import ErrorText
from db.Exceptions import ValidDataException
from db.Models import Jockeys

from db.queries.jockeys import create_jockey
from db.queries.update import up_data


class JockeyTab(ttk.Frame):
    def __init__(self, master, ses: Session):
        super().__init__(master)
        self.ses = ses
        self.ButtSubmit = Button(self, text="add Jockey", command=self.InpInDB)

        self.labelFirstName = ttk.Label(self, text="First Name")
        self.inpFirstName = Entry(self, width=15)

        self.labelLastName = ttk.Label(self, text="Last Name")
        self.inpLastName = Entry(self, width=15)

        self.labelPatronymic = ttk.Label(self, text="Patronymic")
        self.inpPatronymic = Entry(self, width=15)

        self.labelAge = ttk.Label(self, text="Age")
        self.inpAge = Entry(self, width=15)

        self.labelPhoneNumber = ttk.Label(self, text="Phone Number")
        self.inpPhoneNumber = Entry(self, width=15)

        self.labelRating = ttk.Label(self, text="Rating")
        self.inpRating = Entry(self, width=15)

        self.labelIdForUpdate = ttk.Label(self, text="input id")
        self.inpIdForUpdate = Entry(self, width=15)

        self.labelColumnForUpdate = ttk.Label(self, text="input column")
        self.inpColumnForUpdate = Entry(self, width=15)

        self.labelValueForUpdate = ttk.Label(self, text="input Value")
        self.inpValueForUpdate = Entry(self, width=15)

        self.ButtUpdate = Button(self, text="update Data", command=self.updateJockeys)

        self.labelIdForUpdate.grid(column=0, row=2, padx=(20, 20))
        self.inpIdForUpdate.grid(column=0, row=3, padx=(20, 20))

        self.labelColumnForUpdate.grid(column=1, row=2, padx=(20, 20))
        self.inpColumnForUpdate.grid(column=1, row=3, padx=(20, 20))

        self.labelValueForUpdate.grid(column=2, row=2, padx=(20, 20))
        self.inpValueForUpdate.grid(column=2, row=3, padx=(20, 20))

        self.ButtUpdate.grid(column=3, row=3, padx=(20, 20))

        self.ButtSubmit.grid(column=6, row=1, padx=(20, 0))

        self.inpRating.grid(column=5, row=1, padx=(20, 0))
        self.labelRating.grid(column=5, row=0, padx=(20, 0))

        self.inpPhoneNumber.grid(column=4, row=1, padx=(20, 0))
        self.labelPhoneNumber.grid(column=4, row=0, padx=(20, 0))

        self.inpAge.grid(column=3, row=1, padx=(20, 0))
        self.labelAge.grid(column=3, row=0, padx=(20, 0))

        self.inpPatronymic.grid(column=2, row=1, padx=(20, 0))
        self.labelPatronymic.grid(column=2, row=0, padx=(20, 0))

        self.inpLastName.grid(column=1, row=1, padx=(20, 0))
        self.labelLastName.grid(column=1, row=0, padx=(20, 0))

        self.inpFirstName.grid(column=0, row=1)
        self.labelFirstName.grid(column=0, row=0)

    def updateJockeys(self):
        try:
            up_data(self.ses, Jockeys, self.inpIdForUpdate.get(), self.inpColumnForUpdate.get(),
                self.inpValueForUpdate.get())
        except:
            ErrorText("Error")
            raise ValidDataException
    def InpInDB(self):
        FirstName = self.inpFirstName.get()
        LastName = self.inpLastName.get()
        Patronymic = self.inpPatronymic.get()
        Age = self.inpAge.get()
        PhoneNumber = self.inpPhoneNumber.get()
        Rating = float(self.inpRating.get())

        testbodyforJockey = dict(FirstName=FirstName, LastName=LastName, Patronymic=Patronymic, Age=Age,
                                 PhoneNumber=PhoneNumber, rating=Rating)
        try:
            create_jockey(self.ses, testbodyforJockey)
            self.ses.commit()
        except:
            ErrorText("not valid Data")
            raise ValidDataException
