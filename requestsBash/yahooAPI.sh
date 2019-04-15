#!/bin/bash

# x=$(curl -s "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&outputsize=compact&apikey=4I16NYFU17Q3KNKC" | jq '.["Time Series (Daily)"]?')
curl "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&outputsize=compact&apikey=4I16NYFU17Q3KNKC" > prices.json

cat ernst.json | jq '.' 
