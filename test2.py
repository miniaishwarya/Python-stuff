mylist = ["apple", "banana", "cherry"]
myit = iter(mylist)
myit2 =iter(myit)

print(next(myit))
print(next(myit))

c = mylist.copy()
print(c)