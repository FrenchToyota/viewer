from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import requests
import random
import time

# driver = webdriver.Chrome()


def get_proxies():
    proxies = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all").text
    with open("proxies.txt", "w") as f:
        f.write(proxies)
        f.write("\n")
    return proxies

def main():
    proxies = get_proxies()
    proxies = proxies.split("\n")
    print(proxies)
    print("lmaoo")

if __name__ == '__main__':
    main()