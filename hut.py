import pickle
my_list = [1,2,3,4,5]
my_dict = {'name':'bala'}
my_str = 'Hundai'
f = open('news.txt','w')
pickle.dump(my_list,f)
pickle.dump(my_dict,f)
f.close

#$import pickle
#f = open('news.txt','r')
#my_list = pickle.load(f)
