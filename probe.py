def get_age_difference(year1, year2):
    diff = year2 - year1
    stroka = 'The age difference is'
    strola1 = stroka + ' ' + str(diff)
    return strola1

print(get_age_difference(2001, 2018))