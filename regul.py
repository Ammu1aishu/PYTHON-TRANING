import re
import sys

values = raw_input("enter the user input:")

#print re.findall ('\d',values)
#print re.findall ('\w',values)
#print re.findall ('\d+',values)
print re.findall ('\d+\w+',values)
	
	
