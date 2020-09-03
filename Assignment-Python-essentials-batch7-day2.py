print("List and its functions")
s=[1,2,3,4,5,6,7,8]
print("using append function and adding 9")
print(s.append(9)) #1st function
print(s)
print("using insert function and adding 7 at s(1) index")
print(s.insert(1,7)) #2nd function
print(s)
print("using remove function and removing 2")
print(s.remove(2)) #3rd function
print(s)
print("using pop function and ruling out the value at s(1) position")
print(s.pop(1)) #4rth function
print(s)
print("using clear function to print empty list")
print(s.clear())
print(s)
print("__________________________________________")
print("Dictionary_and_its_functions")
a={1:"a",2:"b",3:"c",4:"d",5:"e"}
print(a.pop(4)) #1st function
print(a)
print(a.update({8:"g"})) #2nd function
print(a)
print(a.keys()) #3rd function
print(a.values()) #4rth function
print(a.popitem()) #5th function
print(a)
print("___________________________________________")
print("Set and its functions")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y) #1st function
print(z)
t = x.intersection(y) #2nd function
print(t)
u=x.union(y) #3rd function
print(u)
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2) #4rth function
print(set1)
fruits = {"apple", "banana", "cherry"}
fruits.pop() #5th function
print(fruits)
print("__________________________________________")
print("Tuple and its functions")
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)
print(x)
x = thistuple.index(8)
print(x)
print("__________________________________________")
print("String and its functions")
t="aBcD"
u="hello123"
print(t.upper()) #1st function
print(t.lower()) #2nd function
print(u.title()) #3rd function
print(u.swapcase()) #4rth function
print(u.count("l")) #5th function
