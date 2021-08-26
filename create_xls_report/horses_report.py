from typing import List

import xlsxwriter

from create_xls_report.Exceptions import InsufficientDataException
from db.Models import Jockeys


def create_rep_file_horses(mass: List):
    if len(mass)==0:
        raise InsufficientDataException
    workbook = xlsxwriter.Workbook('download_report/HorsesRep.xls')
    worksheet = workbook.add_worksheet(name="1")
    worksheet.write(0, 0, 'NickName')
    worksheet.write(0, 1, "Gender")
    worksheet.write(0, 2, "DateOfBrinth")
    worksheet.write(0, 3, "Owner Id")
    worksheet.write(0, 4, "Match name")
    worksheet.write(0, 5, "Hippodrome")
    worksheet.write(0, 6, "Date")
    worksheet.write(0, 7, "Taken place")

    counter = 1

    for i in mass:
        worksheet.write(counter, 0, i["First_horse"]["NickName"])
        worksheet.write(counter, 1, i["First_horse"]["Gender"])
        worksheet.write(counter, 2, i["First_horse"]["DateOfBrinth"])
        worksheet.write(counter, 3, i["First_horse"]["OwnerId"])
        worksheet.write(counter, 4, i["MatchName"])
        worksheet.write(counter, 5, i["Place"])
        worksheet.write(counter, 6, i["Date"])
        worksheet.write(counter, 7, i["First_horse"]["Place"])

        counter += 1

    for i in mass:
        worksheet.write(counter, 0, i["Second_Horse"]["NickName"])
        worksheet.write(counter, 1, i["Second_Horse"]["Gender"])
        worksheet.write(counter, 2, i["Second_Horse"]["DateOfBrinth"])
        worksheet.write(counter, 3, i["Second_Horse"]["OwnerId"])
        worksheet.write(counter, 4, i["MatchName"])
        worksheet.write(counter, 5, i["Place"])
        worksheet.write(counter, 6, i["Date"])
        worksheet.write(counter, 7, i["Second_Horse"]["Place"])
        counter += 1
    workbook.close()
