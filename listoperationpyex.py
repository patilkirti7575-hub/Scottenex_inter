thisdata=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","V","W","X","Y","Z"]
print(thisdata)
#length
print(len(thisdata))
#type
print(type(thisdata))

print(thisdata[2])

print(thisdata[-2])
#append
thisdata.append("apple")
print(thisdata)

#range
thisdata.pop(2)
print(thisdata)
for i in range(0,len(thisdata)):
    print(thisdata[i])

#copy
mylist=thisdata.copy()
print(mylist)

#reverse
mylist.reverse()
print(mylist)


mylist=thisdata[:]
print(mylist)

#insert
thisdata.insert(2,"Kirti")
print(thisdata)

#count
x=thisdata.count("oct")
print(x)

#count
thisdata.clear()
print(thisdata)


#extend
numbers=["1","2","3","4","5","6","7","8","9"]
thisdata.extend(numbers)
print(thisdata)

#sort
thisdata.sort()
print(thisdata)


