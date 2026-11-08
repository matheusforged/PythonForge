import datetime

data = datetime.date(2026, 11, 8)
print(data)

data_hora = datetime.datetime(2026, 11, 8)
print(data_hora)

hora = datetime.time(15, 50, 00)
print(hora)

from datetime import datetime 
date_string = "2023-05-01" 
date_obj = datetime.strptime(date_string, "%Y-%d-%m")

print(date_obj)