n=input("enter range")
list_num=[]
for i in range(n) :
  inp=input("enter the number")
  list_num.append(inp)
print max(list_num)
print list_num
list1=[]
for inp in list_num:
  if inp<max(list_num):
   list1.append(inp)
print max(list1)

