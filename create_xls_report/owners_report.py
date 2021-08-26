from typing import List

import xlsxwriter

from create_xls_report.Exceptions import InsufficientDataException
from db.Models import Owners


def create_rep_file_owners(mass: List[Owners]):
    if len(mass)==0:
        raise InsufficientDataException

    workbook = xlsxwriter.Workbook('download_report/OwnerRep.xls')
    worksheet = workbook.add_worksheet(name="1")
    worksheet.write(0, 0, 'Name')
    worksheet.write(0, 1, "Last Name")
    worksheet.write(0, 2, "Patronymic")
    worksheet.write(0, 3, "Age")
    worksheet.write(0, 4, "Phone-number")
    counter = 1

    for i in mass:
        worksheet.write(counter, 0, str(i.FirstName))
        counter += 1

    counter = 1
    for i in mass:
        worksheet.write(counter, 1, str(i.LastName))
        counter += 1

    counter = 1

    for i in mass:
        worksheet.write(counter, 2, str(i.Patronymic))
        counter += 1

    counter = 1

    for i in mass:
        worksheet.write(counter, 3, str(i.Age))
        counter += 1

    counter = 1

    for i in mass:
        worksheet.write(counter, 4, str(i.PhoneNumber))
        counter += 1

    workbook.close()