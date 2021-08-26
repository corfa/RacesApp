from tkinter import ttk, Entry, Button

from sqlalchemy.orm import Session

from UI.tabs.exceptionsMess import ErrorText
from db.Exceptions import ValidDataException
from db.Models import Matches_results

from db.queries.matches import create_match
from db.queries.matches_result import create_match_result
from db.queries.update import up_data


class Match_resultTab(ttk.Frame):
    def __init__(self, master, ses: Session):
        super().__init__(master)
        self.ses = ses
        self.ButtSubmit = Button(self, text="add Match result", command=self.InpInDB)

        self.labelMatchId = ttk.Label(self, text="Match id")
        self.inpMatchId = Entry(self, width=15)

        self.labelfirstPlace_jockey = ttk.Label(self, text="first Place jockey id")
        self.inpfirstPlace_jockey = Entry(self, width=15)

        self.labelSecondPlace_jockey = ttk.Label(self, text="second Place jockey id")
        self.inpSecondPlace_jockey = Entry(self, width=15)

        self.labelThirdPlace_jockey = ttk.Label(self, text="third Place jockey id")
        self.inpThirdPlace_jockey = Entry(self, width=15)

        self.labelfirstPlace_horse = ttk.Label(self, text="first Place horse id")
        self.inpfirstPlace_horse = Entry(self, width=15)

        self.labelSecondPlace_horse = ttk.Label(self, text="second Place horse id")
        self.inpSecondPlace_horse = Entry(self, width=15)

        self.labelThirdPlace_horse = ttk.Label(self, text="third Place horse id")
        self.inpThirdPlace_horse = Entry(self, width=15)

        self.labelIdForUpdate = ttk.Label(self, text="input id")
        self.inpIdForUpdate = Entry(self, width=15)

        self.labelColumnForUpdate = ttk.Label(self, text="input column")
        self.inpColumnForUpdate = Entry(self, width=15)

        self.labelValueForUpdate = ttk.Label(self, text="input Value")
        self.inpValueForUpdate = Entry(self, width=15)

        self.ButtUpdate = Button(self, text="update Data", command=self.updateMath_results)

        self.labelIdForUpdate.grid(column=0, row=2, padx=(20, 20))
        self.inpIdForUpdate.grid(column=0, row=3, padx=(20, 20))

        self.labelColumnForUpdate.grid(column=1, row=2, padx=(20, 20))
        self.inpColumnForUpdate.grid(column=1, row=3, padx=(20, 20))

        self.labelValueForUpdate.grid(column=2, row=2, padx=(20, 20))
        self.inpValueForUpdate.grid(column=2, row=3, padx=(20, 20))

        self.ButtUpdate.grid(column=3, row=3, padx=(20, 20))

        self.ButtSubmit.grid(column=7, row=1, padx=(20, 0))

        self.inpThirdPlace_horse.grid(column=6, row=1, padx=(20, 0))
        self.labelThirdPlace_horse.grid(column=6, row=0, padx=(20, 0))

        self.inpSecondPlace_horse.grid(column=5, row=1, padx=(20, 0))
        self.labelSecondPlace_horse.grid(column=5, row=0, padx=(20, 0))

        self.inpfirstPlace_horse.grid(column=4, row=1, padx=(20, 0))
        self.labelfirstPlace_horse.grid(column=4, row=0, padx=(20, 0))

        self.inpThirdPlace_jockey.grid(column=3, row=1, padx=(20, 0))
        self.labelThirdPlace_jockey.grid(column=3, row=0, padx=(20, 0))

        self.inpSecondPlace_jockey.grid(column=2, row=1, padx=(20, 0))
        self.labelSecondPlace_jockey.grid(column=2, row=0, padx=(20, 0))

        self.inpfirstPlace_jockey.grid(column=1, row=1, padx=(20, 0))
        self.labelfirstPlace_jockey.grid(column=1, row=0, padx=(20, 0))

        self.inpMatchId.grid(column=0, row=1)
        self.labelMatchId.grid(column=0, row=0)

    def updateMath_results(self):
        try:
            up_data(self.ses, Matches_results, self.inpIdForUpdate.get(), self.inpColumnForUpdate.get(),
                    self.inpValueForUpdate.get())
        except:
            ErrorText("Error")
            raise ValidDataException

    def InpInDB(self):

        MathId = self.inpMatchId.get()

        firstPlace_jockey = self.inpfirstPlace_jockey.get()
        SecondPlace_jockey = self.inpSecondPlace_jockey.get()
        ThirdPlace_jockey = self.inpThirdPlace_jockey.get()

        firstPlace_horse = self.inpfirstPlace_horse.get()
        SecondPlace_horse = self.inpSecondPlace_horse.get()
        ThirdPlace_horse = self.inpThirdPlace_horse.get()

        testbodyforMatch = dict(match_id=MathId, firstPlace_jockey=firstPlace_jockey,
                                SecondPlace_jockey=SecondPlace_jockey,
                                ThirdPlace_jockey=ThirdPlace_jockey, firstPlace_horse=firstPlace_horse,
                                SecondPlace_horse=SecondPlace_horse, ThirdPlace_horse=ThirdPlace_horse)
        try:
            create_match_result(self.ses, testbodyforMatch)
            self.ses.commit()
        except:
            ErrorText("not valid Data")
            raise ValidDataException
