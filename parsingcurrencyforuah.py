import requests
from bs4 import BeautifulSoup
import lxml
import json


def parsing_currency():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }

    url = 'https://minfin.com.ua/currency/'

    result = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(result.text, 'lxml')
    currency_result = {}
    table_currency = soup.find('table', class_='table-response mfm-table mfcur-table-lg mfcur-table-lg-currency has-no-tfoot').find('tbody').find_all('tr')

    for currency in table_currency:
        currency_title = currency.find('td', class_='mfcur-table-cur').find('a').text
        average_currency_buy_sell = currency.find('td', class_='mfm-text-nowrap').text
        average_currency_buy = average_currency_buy_sell.split()[0]
        average_currency_sell = average_currency_buy_sell.split()[-1]
        currency_result[currency_title] = {
            'currency_title': currency_title,
            'average_currency_buy': average_currency_buy,
            'average_currency_sell': average_currency_sell
            }

    with open('resultparsingcurrency.json', 'w', encoding='utf8') as file:
        json.dump(currency_result, file, indent=4, ensure_ascii=False)



def main():
    parsing_currency()

if __name__ == '__main__':
    main()
