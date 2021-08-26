from typing import List

import xlsxwriter

from create_xls_report.Exceptions import InsufficientDataException
from db.Models import Jockeys


def sorted(max1: Jockeys, max2: Jockeys, max3: Jockeys):
    if max3.rating > max2.rating > max1.rating:
        max3, max1 = max1, max3

    elif max2.rating > max1.rating > max3.rating:
        max2, max1 = max1, max2

    elif max1.rating > max3.rating > max2.rating:
        max3, max2 = max2, max3

    elif max2.rating > max3.rating > max1.rating:
        max2, max1 = max1, max2
        max2, max3 = max3, max2
    elif max3.rating > max1.rating > max2.rating:
        max3, max1 = max1, max3
        max3, max2 = max2, max3
    elif max2.rating > max3.rating > max1.rating:
        max2, max1, = max1, max2
        max3, max2 = max2, max3

    return max1, max2, max3


def create_rep_file_ipadrom(mass: List[Jockeys]):
    if len(mass)==0:
        print("too few participants to generate a report")
        raise InsufficientDataException
    if len(mass) < 3:

       return 0

    first, second, therd = sorted(mass[0], mass[1], mass[2])

    for i in mass:
        if i.rating > first.rating:
            second = first
            first = i
        elif i.rating > second.rating:
            therd = second
            second = i
        elif i.rating > therd.rating:
            therd = i


    res_mass=[first,second,therd]

    workbook = xlsxwriter.Workbook('download_report/IpadromRep.xls')
    worksheet = workbook.add_worksheet(name="1")
    worksheet.write(0, 0, 'Name')
    worksheet.write(0, 1, "Last Name")
    worksheet.write(0, 2, "Patronymic")
    worksheet.write(0, 3, "Age")
    worksheet.write(0, 4, "Phone-number")
    worksheet.write(0, 5, "Rating")
    counter = 1
    for i in res_mass:
        worksheet.write(counter, 0, str(i.FirstName))
        counter += 1

    counter = 1
    for i in res_mass:
        worksheet.write(counter, 1, str(i.LastName))
        counter += 1

    counter = 1

    for i in res_mass:
        worksheet.write(counter, 2, str(i.Patronymic))
        counter += 1

    counter = 1

    for i in res_mass:
        worksheet.write(counter, 3, str(i.Age))
        counter += 1

    counter = 1

    for i in res_mass:
        worksheet.write(counter, 4, str(i.PhoneNumber))
        counter += 1

    counter = 1

    for i in res_mass:
        worksheet.write(counter, 5, str(i.rating))
        counter += 1

    workbook.close()