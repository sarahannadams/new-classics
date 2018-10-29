from bs4 import BeautifulSoup
import requests, json, time

#setting up the list from which I am going to form my JSON (list of dictionaries) later
book_list = []

#where the page number of URL starts
page=0

#setting while loop for scraping all 9 pages of books
while page <= 9:

	#giving URL to scrape, a friendly message to tell us it's working, and requests module to get that URL
	url = "https://www.nyrb.com/collections/classics?page=" + str(page)
	print("scraping!" + url)
	nyrb_classics = requests.get(url)

	#identifying variable for the HTML of the page
	page_html = nyrb_classics.text

	#parsing our HTML with BeautifulSoup to give a BeautifulSoup object
	soup = BeautifulSoup(page_html, "html.parser")

	#identifying parent div that holds the elements we want to scrape
	all_books = soup.find_all("div", attrs={"class": "productholder"})

	for book in all_books:

		h4_title = book.find("h4", attrs={"class": "title"})
		title = h4_title.text

		#print("Title: ",title)

		span_author = book.find("span", attrs={"class": "author"})
		author = span_author.text

		#print("Author: ",author)

		a_link = book.find("a")
		rel_link = a_link["href"]
		bookpage_link = "https://www.nyrb.com" + rel_link

		#print(bookpage_link)

		img_src = book.find("img")
		img_link = img_src["src"]
		bookcover_link = "https:" + img_link

		#print(bookcover_link)
		
		new_classics = {}
		
		new_classics["title"] = title
		new_classics["author"] = author
		new_classics["book page link"] = bookpage_link
		new_classics["image link"] = bookcover_link
		
		book_list.append(new_classics)
	
	time.sleep(3)
	
	page = page + 1

	json.dump(book_list, open("new_classics.json", "w"), indent=2)
