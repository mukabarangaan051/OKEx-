import requests

url = "https://www.okex.com/api/futures/v3/instruments?instType=FUTURES&uccy=USD&state=LIVE"

response = requests.get(url)
data = response.json()

for instrument in data["data"]:
    if instrument["underlying"] == "BTC":
        print("Symbol:", instrument["instId"])
        print("Last price:", instrument["last"])
        print("Mark price:", instrument["markPx"])
        print("Index price:", instrument["idxPx"])
        print("Open interest:", instrument["oi"])
        print("Volume (24h):", instrument["volCcy"])
        print("---------------------------------")
