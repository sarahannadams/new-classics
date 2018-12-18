## SOME NEW CLASSICS
Created by [Alice Griffin](https://twitter.com/AliceLGriff) + [Sarah Ann Adams](https://twitter.com/_sarahannadams) for [Pratt Institute School of Information](https://www.pratt.edu/academics/information/) course [Programming for Cultural Heritage](http://pfch.nyc/). 
### About

Countless lists of “100 Classics to Read” (or similar) exist for those works which have been defined as [“capital L” Literature](http://www.electricka.com/etaf/muses/literature/literature_popups/whats_literature.htm), works that stand the test of time. When one thinks about reading “the classics” as it pertains to literature, certain books and authors come to mind, many of which are books from white and/or eurocentric voices. How the link between what is considered “good literature” and the prevailing default toward white and eurocentric storytelling be addressed so that more space can be made for broader and more varied voices?

This project “Some New Classics” takes a close look at the  [NYRB Classics](https://www.nyrb.com/collections/classics)- an imprint specializing in “[reissuing volumes that have fallen out of print or been otherwise neglected](https://www.nytimes.com/2018/04/09/style/new-york-review-books-classics.html).” This project seeks to understand the cultural makeup of this collection, and whether or not it is a collection that, by its existence, disrupts and decentralizes the current cultural and geographic overall homogeneity of “the classics.” Through primarily the use of python, this project seeks to retrieve, organize, and disseminate information about the NYRB Classics with respect to original language of the works and location of birth and death of the authors. To accomplish these tasks, we will scrape information from the NYRB Classics website, as well as use OpenRefine to reconcile scraped data to wikidata items for both author information and language family information.

Visualizations and further information can be found at [bit.ly/some_new_classics](http://bit.ly/some_new_classics).

***
### Workflow
* The script '**01_scrape_classics.py**' looped through each of the nine pages of www.nyrb.com/collections/classics and extracted book title, book author, book URL, and book Image URL. For each item in this list, we also assigned a numeric ID to each book . This information was written to the file '**02_classics.json**'.
* The script '**03_classics_to_csv.py**' converted '**02_classics.json**' to '**04_classics.csv**'. 
* The script '**05_scrape_classics_urls.py**' pulled in  each URL from '**04_classics.csv**', and scraped the author statement (e.g., "by Margarita Liberaki, translated from the Greek by Karen Van Dyck"), ISBN, and NYRB publish date from each URL. This information was written to the file '**06_classics_info.json**', which includes the IDs for each book.
* The script '**05_scrape_classics_urls.py**' pulled in  each URL from '**04_classics.csv**', and scraped the author statement (e.g., "by Margarita Liberaki, translated from the Greek by Karen Van Dyck"), ISBN, and NYRB publish date from each URL. This information was written to the file '**06_classics_info.json**', which includes the IDs for each book.  
* The script '**07_classics_info_to_csv.py**' converted '**06_classics_info.json**' to '**08_classics_info.csv**'. 
* The script '**09_original_languages.py**' loads the information from '**06_classics_info.json**'  and targets the author statement for each book, which includes translation information, to assign a language for each book. If the string "translated by" was not included in the author statement, the language of the book was set to "English". This information was written to the file '**10_language_list.json**'.
* The script '**11_language_list_to_csv.py**' converted '**10_language_list.json**' to '**12_language_list.csv**'. 
* Through looking at the data, we learned that the book titles retrieved using the script '**01_scrape_classics.py**' did not include book subtitles. Using the book URLs from '**04_classics.csv**'  again, the script '**13_subtitle_ scrape.py**' scraped each book URL for subtitle information and wrote the information to the file '**14_subtitles.json**'.
* Through looking at the data, we learned that the book titles retrieved using the script '**01_scrape_classics.py**' did not include book subtitles. Using the book URLs from '**04_classics.csv**'  again, the script '**13_subtitle_ scrape.py**' scraped each book URL for subtitle information and wrote the information to the file '**14_subtitles.json**'.
* Google sheets  was used to target just the author name  from the  '_author_translation_note_' column of '**08_classics_info.csv**', retaining the associated book ID. If a book was written by more than one author, additional rows were added for each additional author. This information was downloaded as '**17_author_names.csv**'.
* '17_author_names.csv' was loaded into OpenRefine to reconcile authors with wikidata. Once reconciled, the author's wikidata ID, birth city, birth country, birth city coordinates, death city, death country, death city coordinates were also retrieved from wikidata. If an author, their birth location, and/or their death location did not exist in wikidata, wikidata items (or statements, if the author existed in wikidata) were added. The primary source of information for these wikidata additions was based on NYRB author biographies (e.g., [https://www.nyrb.com/collections/simone-weil](https://www.nyrb.com/collections/simone-weil). If the birth or death city was not known, coordinates for the country were used, which were retrieved from the GeoHacks coordinate URL provided at the top right of the country's wikipedia page. If birth or death country was not known, the applicable location information is 'unknown'. If an author is still living, all death location information is 'n/a'.  This dataset was downloaded from OpenRefine as '**18_author_geospatial_data.csv**' and as '**19_author_geospatial_data.json**'.
* The unique languages from '**12_language_list.csv**' (23 languages in total)  were loaded into OpenRefine. Languages were reconciled with wikidata items, and the "subclass of" property for each language was pulled (e.g., Catalan is a subclass of Occitano-Romance languages, which is a subclass of Gallo-Romance languages, etc.) This process was repeated until the "subclass of" equaled 'Human Language' or other superclasses of "Human Language'. This information was downloaded from OpenRefine as '**20_language_hierarchy_raw.csv**'. Utilizing  the wikipedia page on [nostratic languages](https://en.wikipedia.org/wiki/Nostratic_languages) and other wikipedia pages on languages for reference, the information from '**20_language_hierarchy_raw.csv**' was cleaned up to create a harmonized hierarchy of the languages. 
* ESRI Storymaps was used to create the sliding panel visualization of the birth and death locations of the authors. This can  be seen on the [visualization page](https://sites.google.com/view/some-new-classics/visualizations). The formatted data used to create this visualization can be found in '**21_author_birth_for_viz.csv**' and '**22_author_death_viz.csv**'. The birth and death maps only show one instance of each author; there were a handful of authors who wrote multiple works that were published as NYRB classics. 
* The chart function of google sheets charts was used to create visualizations of the birth locations of the languages of the books, and languages of the books categorized by language category. These can be seen on the [visualization page](https://sites.google.com/view/some-new-classics/visualizations). The formatted data used to create these four visualizations can be found in '**23_book_languages_for_viz.csv**', and '**24_book_languages_categorized for viz.csv**'. 
* '**25_combineData.py**' is the python script that was used to combine our disparate datasets into the preliminary finalized dataset '**26_combinedData_NewClassics.json**'.

