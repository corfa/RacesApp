from tkinter import ttk, Entry, Button


from sqlalchemy.orm import Session

from UI.tabs.exceptionsMess import ErrorText
from db.Exceptions import ValidDataException
from db.Models import Matches

from db.queries.matches import create_match
from db.queries.update import up_data


class MatchTab(ttk.Frame):
    def __init__(self, master, ses: Session):
        super().__init__(master)
        self.ses = ses
        self.ButtSubmit = Button(self, text="add Match", command=self.InpInDB)

        self.labelName = ttk.Label(self, text="Name")
        self.inpName = Entry(self, width=15)

        self.labelPlace = ttk.Label(self, text="Hippodrome")
        self.inpPlace = Entry(self, width=15)

        self.labelDate = ttk.Label(self, text="Date")
        self.inpDate = Entry(self, width=15)

        self.labelIdForUpdate = ttk.Label(self, text="input id")
        self.inpIdForUpdate = Entry(self, width=15)

        self.labelColumnForUpdate = ttk.Label(self, text="input column")
        self.inpColumnForUpdate = Entry(self, width=15)

        self.labelValueForUpdate = ttk.Label(self, text="input Value")
        self.inpValueForUpdate = Entry(self, width=15)

        self.ButtUpdate = Button(self, text="update Data", command=self.updateMath)

        self.labelIdForUpdate.grid(column=0, row=2, padx=(20, 20))
        self.inpIdForUpdate.grid(column=0, row=3, padx=(20, 20))

        self.labelColumnForUpdate.grid(column=1, row=2, padx=(20, 20))
        self.inpColumnForUpdate.grid(column=1, row=3, padx=(20, 20))

        self.labelValueForUpdate.grid(column=2, row=2, padx=(20, 20))
        self.inpValueForUpdate.grid(column=2, row=3, padx=(20, 20))

        self.ButtUpdate.grid(column=3, row=3, padx=(20, 20))

        self.ButtSubmit.grid(column=5, row=1, padx=(20, 0))

        self.inpDate.grid(column=2, row=1, padx=(20, 0))
        self.labelDate.grid(column=2, row=0, padx=(20, 0))

        self.inpPlace.grid(column=1, row=1, padx=(20, 0))
        self.labelPlace.grid(column=1, row=0, padx=(20, 0))

        self.inpName.grid(column=0, row=1)
        self.labelName.grid(column=0, row=0)

    def updateMath(self):
        try:
            up_data(self.ses, Matches, self.inpIdForUpdate.get(), self.inpColumnForUpdate.get(),
                    self.inpValueForUpdate.get())
        except:
            ErrorText("Error")
            raise ValidDataException

    def InpInDB(self):

        Name = self.inpName.get()
        Place = self.inpPlace.get()
        Date = self.inpDate.get()

        testbodyforMatch = dict(name=Name, place=Place, date=Date)
        try:
            create_match(self.ses, testbodyforMatch)
            self.ses.commit()
        except:
            ErrorText("not valid Data")
            raise ValidDataException
