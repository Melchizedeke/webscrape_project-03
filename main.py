# Basic Libraries Import
import requests
from bs4 import BeautifulSoup

# Making a request to the website
res = requests.get("https://www.abebooks.com/collections/mc/first-editions/53jKjLpLq5krU0qFS5tvnO?cm_sp=ccbrowse-_-p0-_-collections")
site_text = res.text
soup = BeautifulSoup(site_text, "html.parser")

# Getting every book's information and saving it in a collections list uaing the `find_all()` method.
collections = soup.find_all(class_="collection-item")

# Loop through the collections lust and save items in a library
book_details = []

for item in collections:
    book_details.append({
        "Book_Title":item.find(class_="title").getText(),
        "Book_Author":item.find(class_="authors").getText(),
        "Pub-Year":item.find(class_="published-year").getText(),
        "Price($)":item.find(class_="price").find('span').getText()
    })

print(book_details)