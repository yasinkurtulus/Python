names=["yasin","bilal","halit"]
print(names[0])
names.insert(1,"ahmet")
print(names)
names.append("memet")
var="ali"
names.append(2)
names.append(var)
print(names)
names.extend(["mali",57,True])
print(names)
names.reverse()
print(names)
print(names.pop(5))
names.remove("ali")
print(names)
#nested list
vegetables=["spinach","kale","tomatoes","celery","potatoes"]
fruit=["strawberries","nectainers","apples"]
dirty_dozen=[fruit,vegetables]
print(dirty_dozen)
print(dirty_dozen[0][1])
lists=[11,11,11]
lists.remove(11)
print(lists)
