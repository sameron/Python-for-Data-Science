import requests
from bs4 import BeautifulSoup
import textwrap

# Specify the webpage to scrape
site_to_scrape = input("Enter a webpage to scrape: ")

# send a request to the webpage
response = requests.get(site_to_scrape)

# parse the HTML content of the webpage
soup = BeautifulSoup(response.text, "html.parser")

# find all the <p> tags on the webpage
paragraphs = soup.find_all("p")

# print the content of each <p> tag to stdout
for p in paragraphs:
    print(textwrap.fill(p.text, width=160))
