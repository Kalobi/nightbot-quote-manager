import sys
import requests


def fetch_quote(token, number):
    r = requests.get("https://twitch.center/customapi/quote", params={"token": token, "data": number})
    print(r)


if __name__ == "__main__":
    fetch_quote(sys.argv[1], 33)
