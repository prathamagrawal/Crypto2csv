import requests
import json
import numpy
import pandas
from datetime import date, timedelta


def get_data(api):
      response=requests.get(f"{api}")
      if response.status_code==200:
        return response.json()
      else:
        print("There is an error")  


def detailed_data(coin):
    url="https://api.coingecko.com/api/v3/coins/"+coin+"?localization=en&tickers=false&market_data=true&community_data=true&developer_data=true&sparkline=true"
    data={}
    data=dict(get_data(url))


    for element in data:
        if('dict' in str(type(data[element])) and element != 'market_data'):
            temp=dict(data[element])
            if("en" in list(temp.keys())):
                data[element]=temp['en']
            elif("homepage" in list(temp.keys())):
                data[element]=temp['homepage']
            elif ("thumb" in list(temp.keys())):
                data[element]=temp['thumb']

    m=dict(data['market_data'])

    for element in m:
        if('dict' in str(type(m[element]))and element !="sparkline_7d"):
            temp=dict(m[element])
            if("usd" in list(temp.keys())):
                data[element]=temp['usd']
        elif('dict' in str(type(m[element])) and element =="sparkline_7d"):
            temp=dict(m[element])
            data["sparkline_7d"]=list(temp.values())
        else:
            data[element]=m[element]
        
    del data['market_data']
    del data['community_data']


    l= ["public_interest_stats","developer_data"]
    for x in l:
        t=data[x]
        for i in t:
            data[i]=t[i]
        del data[x]

    output=pandas.Series(data).to_frame().transpose()
    return output

def date_processing(start,end):
    sdate = date(2019,3,22)   # start date
    edate = date(2019,4,9)   # end date
    dates=list(pandas.date_range(sdate,edate-timedelta(days=1),freq='d'))
    dates=[item.strftime("%d-%m-%Y") for item in dates]
    return dates

def process(coin,date):
    url="https://api.coingecko.com/api/v3/coins/"+coin+"/history?date="+date
    data={}
    data=dict(get_data(url))

    for element in data:
        if('dict' in str(type(data[element])) and element != 'market_data'):
            temp=dict(data[element])
            if("en" in list(temp.keys())):
                data[element]=temp['en']
            elif("homepage" in list(temp.keys())):
                data[element]=temp['homepage']
            elif ("thumb" in list(temp.keys())):
                data[element]=temp['thumb']

    m=dict(data['market_data'])

    for element in m:
        if('dict' in str(type(m[element]))and element !="sparkline_7d"):
            temp=dict(m[element])
            if("usd" in list(temp.keys())):
                data[element]=temp['usd']
        elif('dict' in str(type(m[element])) and element =="sparkline_7d"):
            temp=dict(m[element])
            data["sparkline_7d"]=list(temp.values())
        else:
            data[element]=m[element]
        
    del data['market_data']
    del data['public_interest_stats']
    del data['community_data']


    t=data["developer_data"]
    for i in t:
        data[i]=t[i]
    del data["developer_data"]

    output=pandas.Series(data).to_frame().transpose()
    return output

def date_date(coin,start,end):
    dates=date_processing(start,end)
    output=process(coin,dates[0])    
    if(len(dates)>1):
        for i in range(1,len(dates)):
            output=output.append(process(coin,dates[i]))
    output['Date']=dates
    output.set_index("Date",inplace=True)
    return output

output=date_date("bitcoin","aa","Asd")
output.to_csv("bitcoin.csv")
    