from tkinter import ttk, Entry, Button
from tkinter.ttk import Combobox

from sqlalchemy.orm import Session

from UI.tabs.exceptionsMess import ErrorText
from db.Exceptions import ValidDataException
from db.Models import Owners, Horses
from db.queries.horses import create_horse
from db.queries.update import up_data


class HorseTab(ttk.Frame):
    def __init__(self, master, ses: Session):
        super().__init__(master)
        self.ses = ses
        self.ButtSubmit = Button(self, text="add Horse", command=self.InpInDB)

        self.labelNickname = ttk.Label(self, text="Nickname")
        self.inpNickname = Entry(self, width=15)

        self.labelGender = ttk.Label(self, text="Gender")
        self.inpGender = Combobox(self)
        self.inpGender['values'] = ("Mal", "Fem")
        self.inpGender.current(0)

        self.labelDateOfBirth = ttk.Label(self, text="Date Of Birth")
        self.inpDateOfBirth = Entry(self, width=15)

        self.labelOwnerId = ttk.Label(self, text="Owner Id")
        self.inpOwnerId = Entry(self, width=15)

        self.labelIdForUpdate = ttk.Label(self, text="input id")
        self.inpIdForUpdate = Entry(self, width=15)

        self.labelColumnForUpdate = ttk.Label(self, text="input column")
        self.inpColumnForUpdate = Entry(self, width=15)

        self.labelValueForUpdate = ttk.Label(self, text="input Value")
        self.inpValueForUpdate = Entry(self, width=15)

        self.ButtUpdate = Button(self, text="update Data", command=self.updateHorse)

        self.labelIdForUpdate.grid(column=0, row=2, padx=(20, 20))
        self.inpIdForUpdate.grid(column=0, row=3, padx=(20, 20))

        self.labelColumnForUpdate.grid(column=1, row=2, padx=(20, 20))
        self.inpColumnForUpdate.grid(column=1, row=3, padx=(20, 20))

        self.labelValueForUpdate.grid(column=2, row=2, padx=(20, 20))
        self.inpValueForUpdate.grid(column=2, row=3, padx=(20, 20))

        self.ButtUpdate.grid(column=3, row=3, padx=(20, 20))

        self.ButtSubmit.grid(column=5, row=1, padx=(20, 0))

        self.inpOwnerId.grid(column=3, row=1, padx=(20, 0))
        self.labelOwnerId.grid(column=3, row=0, padx=(20, 0))

        self.inpDateOfBirth.grid(column=2, row=1, padx=(20, 0))
        self.labelDateOfBirth.grid(column=2, row=0, padx=(20, 0))

        self.inpGender.grid(column=1, row=1, padx=(20, 0))
        self.labelGender.grid(column=1, row=0, padx=(20, 0))

        self.inpNickname.grid(column=0, row=1)
        self.labelNickname.grid(column=0, row=0)

    def updateHorse(self):
        try:
            up_data(self.ses, Horses, self.inpIdForUpdate.get(), self.inpColumnForUpdate.get(),
                    self.inpValueForUpdate.get())
        except:
            ErrorText("Error")
            raise ValidDataException

    def InpInDB(self):
        Nickname = self.inpNickname.get()
        Gender = self.inpGender.get()
        DateOfBirth = self.inpDateOfBirth.get()
        OwnerId = self.inpOwnerId.get()

        testbodyforHorse = dict(Nickname=Nickname, Gender=Gender, DateOfBirth=DateOfBirth, OwnerId=OwnerId, )
        try:
            create_horse(self.ses, testbodyforHorse)
            self.ses.commit()
        except:
            ErrorText("not valid Data")
            raise ValidDataException
