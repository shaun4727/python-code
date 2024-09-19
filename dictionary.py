#mutable
myDictionary = {"name": "Max","age":28, "city":"New York"}

del myDictionary['name']
myDictionary["email"] = "max@gmail.com"
print(myDictionary);

# copy
myDictionary_cpy = myDictionary.copy();
myDictionary_cpy["email"] = "cpy@gmail.com";
print(myDictionary_cpy)

# merge
my_dict = {"name":"Marry", "age": 27,"city": "Dhaka"}

myDictionary.update(my_dict);

print(myDictionary);

# we can use tuple also
mytuple = (8,7)
dictionary = {mytuple: 15}
print(dictionary[mytuple])