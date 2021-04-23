import requests,json
import pandas as pd

cryps = 50 #the number of cryptocurrencies to display

userage = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

r = requests.get("https://api.coinmarketcap.com/data-api/v3/map/all?listing_status=active,untracked", headers=userage)

data = r.json()
rank = []
symbol = []
name = []
histo = []
for x in range(cryps):
    rank.append(data['data']['cryptoCurrencyMap'][x]['rank'])
    symbol.append(data['data']['cryptoCurrencyMap'][x]['symbol'])
    name.append(data['data']['cryptoCurrencyMap'][x]['name'])
    histo.append(data['data']['cryptoCurrencyMap'][x]['first_historical_data'])

cryps = {'Crypto Rank':rank,'Symbol':symbol,'Name':name,'First Historical Data':histo}

print(pd.DataFrame(cryps))
