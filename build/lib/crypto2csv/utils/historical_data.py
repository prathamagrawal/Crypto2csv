import pandas
from .process import process
from .get_dates import get_dates


def historical_data(coin,start,end):
    dates=get_dates(start,end)
    output=process(coin,dates[0])    
    if(len(dates)>1):
        for i in range(1,len(dates)):
            output=output.append(process(coin,dates[i]))
    output['Date']=dates
    output.set_index("Date",inplace=True)
    return output