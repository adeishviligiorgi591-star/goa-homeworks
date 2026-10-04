# 1) შექმენი სია:

# ["ვაშლი", "ბანანი", "ატამი"]

# და დაამატე "მსხალი" სიის ბოლოში.

fruit=["apple","banana","peach"]
fruit.append("მსხალი")
print(fruit)
# 2) შექმენი სია:

# ["Python", "JavaScript", "C++"]

# და "HTML" ჩასვი JavaScript-მდე.
languages=["Python", "JavaScript", "C++"]
languages.insert(1,"Html")
print(languages)
# 3) შექმენი სია:

# ["red", "blue", "green", "yellow"]

# ამოაგდე "green" მისი ინდექსის გამოყენებით.
color=["red", "blue", "green", "yellow"]
color.remove("green")
print(color)
# 4) 

# შექმენი სია:

# ["apple", "banana", "orange", "banana"]

# წაშალე "orange" 

fruits=["apple", "banana", "orange", "banana"]
fruits.remove("orange")
print(fruits)
# 5) მოცემულია:

# ["cat", "dog", "cat", "bird", "cat", "dog"]

# დაითვალე, რამდენჯერ გვხვდება "cat".
pets= ["cat", "dog", "cat", "bird", "cat", "dog"]
print(pets.count("cat"))

# 6) მოცემულია:

# ["BMW", "Mercedes", "Audi", "Toyota"]

# იპოვე "Audi"-ს ინდექსი.
cars=["BMW", "Mercedes", "Audi", "Toyota"]
print(cars.index("Audi"))
