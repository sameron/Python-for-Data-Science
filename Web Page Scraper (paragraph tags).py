import textwrap

import requests
from bs4 import BeautifulSoup


sitetoscrape = input("Enter a webpage to scrape: ")

# send a request to the webpage
response = requests.get(sitetoscrape)

# parse the HTML content of the webpage
soup = BeautifulSoup(response.text, "html.parser")

# find all the <p> tags on the webpage
paragraphs = soup.find_all("p")

# print the content of each <p> tag to the console
for p in paragraphs:
    print(textwrap.fill(p.text, width=160))
