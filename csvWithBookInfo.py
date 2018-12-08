

csv_header = 'id, title, book_page_url, subtitle, original_language, isbn, pub_date'
csv_out = 'allDataNoAuthor.csv'

csv_list = ['new_classics.csv', 'subtitles.csv', 'language_list.csv', 'new_classics_book_info.csv' ]

csv_merge = open(csv_out, 'w')
csv_merge.write(csv_header)
csv_merge.write('\n')

for file in csv_list:
	csv_in = open(file, 'r')
	for line in csv_in:
		if line.startswith(csv_header):
			continue
		csv_merge.write(line)
	csv_in.close()
csv_merge.close()

# print('Verify consolidated CSV file : ' + csv_out)