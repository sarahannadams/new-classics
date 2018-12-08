import pandas as pd
import csv

#csv_header = 'id, title, book_page_url, subtitle, original_language, isbn, pub_date'
csv_out = open('allDataNoAuthor.csv', 'w', encoding='utf-8')

# csv_list = ['new_classics.csv', 'subtitles.csv', 'language_list.csv', 'new_classics_book_info.csv' ]

# csv_merge = open(csv_out, 'w')
# csv_merge.write(csv_header)
# csv_merge.write('\n')

# for file in csv_list:
# 	csv_in = open(file, 'r')
# 	csv_object = csv_in.DataFrame(data=file)

df1 = pd.read_csv('new_classics.csv', usecols=0,1,3)
df2 = pd.read_csv('subtitles.csv', usecols=1,2,3)
df3 = pd.read_csv('language_list.csv', )
df4 = pd.read_csv('new_classics_book_info.csv')

data = pd.concat([df1, df2], axis=1, join='inner')
	
	# for line in csv_in:
# 		if line.startswith(csv_header):
# 			continue
# 		csv_merge.write(line)
# 	csv_in.close()

csv_out.close()

# print('Verify consolidated CSV file : ' + csv_out)

