import requests
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent
from art import *
import collections
collections.Callable = collections.abc.Callable


def main():
    tprint("#Vigen")
    ua = UserAgent().chrome
    parse_url = input("Url: ")
    tprint("ImGAY")
    ses = requests.session()
    headers = {
        'user-agent': str(ua)
    }
    resp = ses.get(url=parse_url, headers=headers)
    soup = BS(resp.text, "html.parser")
    td_all = soup.findAll('td')
    list = []
    for a in td_all:
        list.append(a.text.strip())
    for i in range(len(list)):
        if (i % 7 == 0):
            print(list[i] + ":" + list[i+1])

        if list[i] == "VPN":
            break

    aue = 64
    while True:
        parse_url = parse_url.replace('#list', f'&start={aue}#list')
        resp = ses.get(url=parse_url, headers=headers)
        soup = BS(resp.text, "html.parser")
        td_all = soup.findAll('td')
        list = []
        for a in td_all:
            list.append(a.text.strip())
        for i in range(len(list)):
            if (i % 7 == 0):
                print(list[i] + ":" + list[i + 1])

            if list[i] == "VPN":
                break
        aue += 64


if __name__ == "__main__":
    main()