import tkinter as tk
from doctest import master
from tkinter import ttk

from UI.tabs.HorseTab import HorseTab
from UI.tabs.JockeyTab import JockeyTab
from UI.tabs.MatchTab import MatchTab
from UI.tabs.Match_resultTab import Match_resultTab
from UI.tabs.OwnerTab import OwnerTab
from UI.tabs.ReportTab import ReportTab
from db.DataBase import DataBase


class RacesApp(tk.Tk):
    def __init__(self, db: DataBase):
        self.db = db
        self.db.check_connection()

        tk.Tk.__init__(self)
        notebook = ttk.Notebook(master)
        notebook.pack(expand=1, fill='both')
        horseTab = HorseTab(notebook, db.make_session())
        ownerTab = OwnerTab(notebook, db.make_session())
        jockeyTab = JockeyTab(notebook, db.make_session())
        matchTab = MatchTab(notebook, db.make_session())
        reportTab = ReportTab(notebook, db.make_session())
        match_resultTab = Match_resultTab(notebook, db.make_session())
        notebook.add(ownerTab, text='Owners')
        notebook.add(horseTab, text="Horse")
        notebook.add(jockeyTab, text="Jockey")
        notebook.add(matchTab, text="Match")
        notebook.add(match_resultTab, text="Match result")
        notebook.add(reportTab, text="Report")
