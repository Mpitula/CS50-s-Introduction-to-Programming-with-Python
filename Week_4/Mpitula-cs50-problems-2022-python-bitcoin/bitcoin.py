import requests
import sys

try:
    if len(sys.argv) != 2:
        sys.exit("comand-Line is not a number")

    bitcoins = float(sys.argv[1])

    url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=9ae7399fd0ab7b6b4d30e6955a31a28b1cfd9b7f95729b457675caa0a2eab997"
    response = requests.get(url)
    data = response.json()

    price = float(data["data"]["priceUsd"])

    cost = bitcoins * price

    print(f"${cost:,.4f}")
except requests.RequestException:
    sys.exit("comand-Line is not a number")
except (KeyError, ValueError):
    sys.exit("comand-Line is not a number")
