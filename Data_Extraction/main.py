
url="https://api.coingecko.com/api/v3/coins/bitcoin?localization=en&tickers=false&market_data=true&community_data=true&developer_data=true&sparkline=true"


import requests
import json
import numpy
import pandas 


def get_data(api):
      response=requests.get(f"{api}")
      if response.status_code==200:
        print("Successfully fetched the data")
        print(response)
        return response.json()
      else:
        print("There is an error")  


data={}



data=dict(get_data(url))


for element in data:
    if('dict' in str(type(data[element]))):
        print(element)
    


"""
#### Removing public_interesets_stats

"""


"""
## getting data for platforms,localization, description,links,image
"""



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




data.keys()


output=pandas.Series(data).to_frame().transpose()
output.to_csv("output.csv")
