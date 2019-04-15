import json
import requests
import pandas as pd

def get_rapidAPI():
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-movers?region=US&lang=en"
    params = {  "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com",
                "X-RapidAPI-Key": "90d1e64ae4mshcb265f14be79861p196724jsn40a7d5c76938"}
                
    resp = requests.get(url, headers=params).json() 
    res = resp["result"]
    gainers, losers, active = res[0]["quotes"], res[1]["quotes"], res[2]["quotes"]
    g = pd.DataFrame(gainers)
    l = pd.DataFrame(losers)
    a = pd.DataFrame(active)
    return g, l, a

def get_AlphaVantage(ticker):
    url = "https://www.alphavantage.co/query"
    params = {  "function": "TIME_SERIES_DAILY",
                "symbol": ticker,
                "outputsize": "compact",
                "apikey": "4I16NYFU17Q3KNKC"}
    response = requests.get(url, params).json()
    keys   = list(response.keys())
    series = keys[1]
    result = response[series]
    return pd.DataFrame.from_dict(result, orient="index")

def get_eodOptions(ticker, api_token = "5c958084138e54.81660498"):
    dfPrices = get_AlphaVantage(ticker)
    stock_price = dfPrices["4. close"].iat[-1]
    url  = "https://eodhistoricaldata.com/api/options/" + ticker
    params = {"api_token" : api_token}
    dictionary = requests.get(url, params).json() 
    keys = list(dictionary.keys())
    data = keys[2]
    resp = dictionary[data]
    lst1 = [x for x in resp]
    put_lst, call_lst = list(), list()
    for x in lst1:
        put,call = x["options"]["PUT"], x["options"]["CALL"]
        cols = ["change","changePercent","contractName","contractSize","currency",
        "delta","lastTradeDateTime","rho","theta","gamma","intrinsicValue",
        "theoretical","timeValue","updatedAt","vega"]
        puts,calls = pd.DataFrame.from_dict(put), pd.DataFrame.from_dict(call)
        puts.drop(cols,axis=1,inplace=True)
        calls.drop(cols,axis=1,inplace=True)
        puts["spot"]  = float(stock_price)
        calls["spot"] = float(stock_price)
        put_lst.append(puts)
        call_lst.append(calls)
    puts, calls = pd.concat(put_lst), pd.concat(call_lst)
    return puts.append(calls, ignore_index=True)

def output_to_excel(ticker):
    df1 = get_AlphaVantage(ticker)
    df2 = get_eodOptions(ticker)
    dfG, dfL, dfA = get_rapidAPI()
    with pd.ExcelWriter("MarketData.xlsx") as writer:
        df1.to_excel(writer, sheet_name=f"{ticker}_Prices")
        df2.to_excel(writer, sheet_name="Options_Info")
        dfG.to_excel(writer, sheet_name="Gainers")
        dfL.to_excel(writer, sheet_name="Losers")
        dfA.to_excel(writer, sheet_name="Most_Active")

 
output_to_excel("AAPL")