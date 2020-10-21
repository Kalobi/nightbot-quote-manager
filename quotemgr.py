import sys
import itertools as it
import requests


def fetch_quote(token, number):
    r = requests.get("https://twitch.center/customapi/quote", params={"token": token, "data": number})
    return r.text


def fetch_all_quotes(token):
    return list(it.takewhile(lambda quote: quote[0].isdigit(),
                             (fetch_quote(token, num) for num in it.count(1))))


if __name__ == "__main__":
    for quote in fetch_all_quotes(sys.argv[1]):
        print(quote)
