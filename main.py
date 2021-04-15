from datetime import datetime
from datetime import timedelta

timestring = '2021-02-23 08:30:00'
logdate = datetime.strptime(timestring, '%Y-%m-%d %H:%M:%S') - timedelta(hours=-17)
print(logdate)

timestring = '2021-02-23 11:20:00'
logdate = datetime.strptime(timestring, '%Y-%m-%d %H:%M:%S') - timedelta(hours=-1)
print(logdate)
