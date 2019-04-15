import unirest
import json

response = unirest.get("https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-movers?region=US&lang=en",
  headers={
    "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "9d62c4e83bmsh39b915f31d1b7d1p1a2472jsnefe5b6a2e52f"
  }
)

not_working = """https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-movers?region=US&lang=en&X-RapidAPI-Host=apidojo-yahoo-finance-v1.p.rapidapi.com&X-RapidAPI-Key=33c24add40mshec4f88fbe6795afp1c8e37jsnc0fcd9eabe11"""

print response.json()