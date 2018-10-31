# import csv

# url_list = []

# with open('new_classics.csv','r') as f:
# 	reader = csv.reader(f)
# 	headers = next(reader) #ignores the header
# 	for row in reader:
# 		print(row[3])


# for url in url_list:

from bs4 import BeautifulSoup
import requests, json, time, re

#giving URL to scrape, a friendly message to tell us it's working, and requests module to get that URL
url = "https://www.nyrb.com/collections/classics/products/the-word-of-the-speechless"
print("scraping!" + url)
nyrb_classics_book = requests.get(url)

#setting the variable for the HTML of the page
page_html = nyrb_classics_book.text

#parsing our HTML with BeautifulSoup to give a BeautifulSoup object
soup = BeautifulSoup(page_html, "html.parser")

#identifying the 1st parent div that holds the elements we want to scrape
all_info = soup.find_all("div", attrs={"class":"span8"})

#looping through to pull out the elements we want
for item in all_info:

	#subtitle is under the span element class=subtitle
	span_subtitle = item.find("span", attrs={"class": "subtitle"})
	subtitle = span_subtitle.text

	print(subtitle)

	#author and translation information is under the h2 element class=combined-authors
	h2_combined_authors = item.find("h2", attrs={"class": "combined-authors"})
	authors_translation = h2_combined_authors.text

	print(authors_translation.strip())

#identifying the 2nd parent div that holds the elements we want to scrape
all_info_2 = soup.find_all("div", attrs={"class":"description additional"})

#looping through to pull out the elements we want
for item in all_info_2:

	#isbn is under the span element class=variant-sku
	span_variant_sku = item.find("span", attrs={"class": "variant-sku"})
	isbn = span_variant_sku.text

	print(isbn.strip())

	#publication date is found wihtin additional info, which is under the span p element 
	p_addl_info = item.find("p")
	
	#created a regex to target just the publication date
	x = re.compile('([0-9]{4})')
	pub_date = x.findall(p_addl_info.text)

	print(str(pub_date[1]))