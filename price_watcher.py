#!/usr/bin/python

# Based on the script by 
# Ajinkya Sonawane via Medium.com

import requests
from bs4 import BeautifulSoup
import smtplib

def check_price(URL, threshold_amt):
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    # find() is used to find the element from the parsed HTML code
    # get_text() is used to fetch the text of the found elemen
    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id="priceblock_saleprice").get_text()[1:].strip().replace(',','')
    Fprice = float(price)
    if Fprice < threshold_amt:
        alert_me()


def alert_me(URL,title, price):
    server = smtplib.SMTP('smtp.gmail.com',587)
    
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('YOUR_EMAIL','GOOGLE_APP_PASSWORD')
    
    subject = 'Price fell down for '+title
    body = 'Buy it now here: '+URL
    msg = f"Subject:{subject}\n\n{body}"
    
    server.sendmail('YOUR_EMAIL','TO_EMAIL',msg)
    print('Email alert sent')
    server.quit()

def main():
    args = sys.argv[1:]
    # TODO save args as URL and threshold_amt
    # Also: this while loop may be replaced by putting script in crontab
    while True:
        check_price(args[0], args[1])        
        time.sleep(360)


if __name__ == "__main__":
    main()
