import pandas
from datetime import date, timedelta,datetime

def get_dates(start,end):
    sdate = datetime.strptime(start, '%d-%m-%Y').date()
    edate = datetime.strptime(end, '%d-%m-%Y').date()
    dates=list(pandas.date_range(sdate,edate-timedelta(days=1),freq='d'))
    dates=[item.strftime("%d-%m-%Y") for item in dates]
    return dates

