euro_pro_stunde = int(input("Euro pro Stunde: "))

result_day = 8 * euro_pro_stunde 
result_month =  result_day * 20 
result_year = result_month * 12
print('Du verdienst ', euro_pro_stunde,'$ pro Stunde.'), print("An einem Tag verdienst du ", result_day, '$'),print('Pro Monat', result_month, '$'),print('Pro Jahr', result_year, '$')
input("Taste drucken")