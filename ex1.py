mystr=raw_input("enter string")
mywords=mystr.split("_")
print mywords
mywords.reverse()
print mywords
mycomp="_".join(mywords)
print mycomp


