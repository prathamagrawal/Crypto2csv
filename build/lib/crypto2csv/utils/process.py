import pandas
from .api_call import get_data


def process(coin,date):
    url=str("https://api.coingecko.com/api/v3/coins/"+str(coin)+"/history?date="+str(date))
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