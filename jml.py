import json
my_list = [1,2,3,4,5]
my_dict = {'name':'aishu'}
my_str = 'asm tech'
f = open('news.txt','w')
json.dump(my_list,f)
json.dump(my_dict,f)
f.close

