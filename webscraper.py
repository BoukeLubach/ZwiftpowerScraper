import re
import sys
import json
import pathlib
import requests
from bs4 import BeautifulSoup
from selenium import webdriver   # for webdriver
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
import csv

def get_zp_data():
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(options=option)
    path = "https://www.zwiftpower.com/profile.php?z=851007out=profile_851007.html"
    # driver = webdriver.Firefox()
    driver.get(path)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    return soup

def export_data_to_text(html):
    with open('url.txt', 'w', encoding='utf-8') as f_out:
        f_out.write(soup.prettify())

def export_to_html(html_table, filename):
    with open(filename, "w", encoding='utf-8') as file:
        file.write(str(html_table))

def html_table_to_csv(soup):
    table = soup.find("table")

    output_rows = []
    for table_row in table.findAll('tr'):
        columns = table_row.findAll('td')
        output_row = []
        for column in columns:
            column_text = column.text.replace('\n', '')
            output_row.append(column_text)

        output_rows.append(output_row)

        print(output_row)

    with open('output.csv', 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(output_rows)


# Load data from website
soup = get_zp_data()

#get results table from soupdata
results_div = soup.find("div", {"id": "profile_results_wrapper"})

# #store table as separate HTML file (reduce nr. of website requests)
table = results_div.find("table")
export_to_html(table, "table.html")


get data from table and convert table to csv data
soup = BeautifulSoup(open("table.html"), "html.parser")
html_table_to_csv(soup)

