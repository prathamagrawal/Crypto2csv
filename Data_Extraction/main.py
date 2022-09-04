url="https://api.coingecko.com/api/v3/coins/bitcoin?localization=en&tickers=false&market_data=true&community_data=true&developer_data=true&sparkline=true"

import requests
import json
import numpy
import pandas 


def get_data(api):
      response=requests.get(f"{api}")
      if response.status_code==200:
        return response.json()



data={}


data=dict(get_data(url))
    


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
    elif('dict' in str(type(data[element])) and element == 'community_data'):
        temp=dict(data[element])
        for item in temp:
            data['community_data'+str(item)]=temp[item]
    elif('dict' in str(type(data[element])) and element == 'developer_data'):
        temp=dict(data[element])
        for item in temp:
            data['developer_data'+str(item)]=temp[item]
    elif('dict' in str(type(data[element])) and element == 'public_interest_stats'):
        temp=dict(data[element])
        for item in temp:
            data['public_interest_stats'+str(item)]=temp[item]



            
del data['community_data']
del data['developer_data']
del data['public_interest_stats']


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



output=pandas.Series(data).to_frame().transpose()
output.to_csv("output.csv")


output


