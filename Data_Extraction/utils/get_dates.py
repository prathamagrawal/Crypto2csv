import pandas
from datetime import date, timedelta

def get_dates(start,end):
    sdate = date(2019,3,22)   # start date
    edate = date(2019,4,9)   # end date
    dates=list(pandas.date_range(sdate,edate-timedelta(days=1),freq='d'))
    dates=[item.strftime("%d-%m-%Y") for item in dates]
    return dates