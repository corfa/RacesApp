from tkinter import ttk, Entry, Button
from tkinter.ttk import Combobox

from sqlalchemy.orm import Session

from UI.tabs.exceptionsMess import ErrorText
from create_xls_report.horses_report import create_rep_file_horses
from create_xls_report.ipadrom_report import create_rep_file_ipadrom
from create_xls_report.jockeys_report import create_rep_file_jockeys
from create_xls_report.owners_report import create_rep_file_owners

from db.Exceptions import ValidDataException
from db.queries.horses import create_horse
from db.queries.reports import report_for_owners, report_for_jockeys, report_for_horses, report_for_ipadrom



class ReportTab(ttk.Frame):
    def __init__(self, master, ses: Session):
        super().__init__(master)
        self.ses = ses

        self.labelgetOwners = ttk.Label(self, text="owners with more than one horse")
        self.getOwners = Button(self, text="download owners report", command=self.download_owners)

        self.labelgetJockeys = ttk.Label(self, text="show the best jockeys:\n input rating")
        self.inpReting = ttk.Entry(self, width=15)
        self.getJockeys = Button(self, text="download jockeys report", command=self.download_jockeys)

        self.labelgetHorses = ttk.Label(self, text="show the best horses:\n input date")
        self.inpDateStart = ttk.Entry(self, width=15)
        self.inpDateFinish = ttk.Entry(self, width=15)
        self.getHorses = Button(self, text="download horses report", command=self.download_horses)

        self.labelgetIpadrom=ttk.Label(self,text="show the best jockeys for the last mouth")
        self.inpIpadrom=ttk.Entry(self, width=15)
        self.getIpadrom=Button(self,text="download ipadrom report", command=self.download_ipadrom)

        self.resultLebels = ttk.Label(self, text="")

        self.labelgetOwners.grid(column=0, row=0, padx=(40, 0))
        self.getOwners.grid(column=0, row=1, padx=(40, 0))

        self.labelgetJockeys.grid(column=1, row=0, padx=(40, 0))
        self.inpReting.grid(column=1, row=1, padx=(40, 0))
        self.getJockeys.grid(column=1, row=2, padx=(40, 0))

        self.labelgetHorses.grid(column=2, row=0, padx=(10, 0))
        self.inpDateStart.grid(column=2, row=1, padx=(40, 200))
        self.inpDateFinish.grid(column=2, row=1, padx=(40, 0))
        self.getHorses.grid(column=2, row=2, padx=(0, 0))

        self.labelgetIpadrom.grid(column=3, row=0, padx=(40, 0))
        self.inpIpadrom.grid(column=3, row=1, padx=(40, 0))
        self.getIpadrom.grid(column=3, row=2, padx=(40, 0))

        self.resultLebels.grid(column=300, row=300, padx=(50, 100))

    def pr(self):
        print(self.inpDateStart.get())


    def download_owners(self):
        massOwners = report_for_owners(self.ses)
        create_rep_file_owners(massOwners)

    def download_jockeys(self):
        massJockey = report_for_jockeys(self.ses, self.inpReting.get())
        create_rep_file_jockeys(massJockey)

    def download_horses(self):
        mass=report_for_horses(self.ses,str(self.inpDateStart.get()),str(self.inpDateFinish.get()))
        create_rep_file_horses(mass)

    def download_ipadrom(self):
        mass=report_for_ipadrom(self.ses,self.inpIpadrom.get())
        create_rep_file_ipadrom(mass)