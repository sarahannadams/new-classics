from bs4 import BeautifulSoup
import requests, json, time

#setting up the list from which I am going to form my JSON (list of dictionaries) later
#book_list = []

#setting while loop for scraping all 9 pages of books
#while page <= 10

#giving URL to scrape, a friendly message to tell us it's working, and requests module to get that URL
url = "https://www.nyrb.com/collections/classics?page=0" #+ str(page)
print("scraping!" + url)
nyrb_classics = requests.get(url)

#identifying variable for the HTML of the page
page_html = nyrb_classics.text

#parsing our HTML with BeautifulSoup to give a BeautifulSoup object
soup = BeautifulSoup(page_html, "html.parser")

#identifying parent div that holds the elements we want to scrape
all_books = soup.find_all("div", attrs={"class": "productholder"})

print(all_books)
