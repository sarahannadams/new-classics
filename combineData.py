import json
from functools import reduce
from collections import defaultdict

# function to merge json files
def merge(a, b, path=None):
	a = defaultdict(path)
	b = defaultdict(path)
	if path is None: path = []
	for key in b:
		if key in a:
			if isinstance(a[key], dict) and isinstance(b[key], dict):
				merge(a[key], b[key], path + [str(key)])
			elif a[key] == b[key]:
				# same value
				pass 
			else:
				raise Exception('Conflict at %s' % '.'.join(path + [str(key)]))
	else:
		a[key] = b[key]
	return a

with open('new_classics.json', 'r') as fp1:
	with open('subtitles.json', 'r') as fp2:		
		
		jsondata1=json.load(fp1)
		jsondata2=json.load(fp2)		
	
with open('allData_NewClassics.json', 'w') as f:
	json.dump(merge(jsondata1,jsondata2, path=None),f,sort_keys=True)



#import json
# 
# def merge(a, b):
#     for key in b:
#     	# if key is in both a and b
#         if key in a:
#         	# if the key is dict Object
#             if isinstance(a[key], dict) and isinstance(b[key], dict): 
#                 merge(a[key], b[key])
#             else:
#               a[key] =a[key]+ b[key]
#         # if the key is not in dict a , add it to dict a      
#         else: 
#             a.update(b)
#     return a
# 
# all_data = []
# 
# with open('new_classics.json', 'r') as fp1:
# 	with open('subtitles.json', 'r') as fp2:		
# 		
# 		jsondata1=json.load(fp1)
# 		jsondata2=json.load(fp2)		
# 	
# with open('allData_NewClassics.json', 'w') as f:
# 	json.dump(merge(jsondata1,jsondata2),f,sort_keys=True,encoding='utf-8', ensure_ascii=False)
	



# allData_NewClassics = {}
# 
# all_data.append(allData_NewClassics)	