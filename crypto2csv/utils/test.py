from api_call import get_data
from get_dates import get_dates

dates=get_dates('20-06-2022','02-08-2022')
url=str("https://api.coingecko.com/api/v3/coins/bitcoin/history?date=")

for item in dates:
    print(get_data(url+str(item)))
    print()
    print("-"*50)

#print(get_data(url))