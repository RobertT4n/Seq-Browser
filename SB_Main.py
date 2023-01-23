import sqlite3
from bs4 import BeautifulSoup
import requests

# Make a request to the webpage
url = "https://www.example.com"
page = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(page.content, "html.parser")

# Find specific elements on the page
element = soup.find("div", class_="example-class")

# Extract the text from the element
text = element.get_text()

# Print the text
print(text)
