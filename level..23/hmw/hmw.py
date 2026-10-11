# 2) მოცემულია:
# დაამატე "salad" ბოლოში.
# ჩასვი "cola" ინდექსზე 1.
# წაშალე "fries".
# დაითვალე "pizza"-ს რაოდენობა.
# იპოვე "burger"-ის ინდექსი.


food=["pizza", "burger", "pizza", "fries"]
food.append("salad")
food.insert(1,"cola")
food.remove("fries")
print(food)
print(food.count("pizza"))
print(food.index("burger"))




# 3) მოცემულია:

# ["apple", "banana", "orange", "apple", "kiwi"]

# გამოიყენეთ მხოლოდ ეს მეთოდები: .append(), .insert(), .pop(), .remove(), .count(), .index().

# საბოლოოდ სია უნდა გახდეს:

# ["apple", "grape", "banana", "apple", "kiwi", "melon"]

# და ასევე უნდა გაიგო:

# რამდენჯერ გვხვდება "apple"
# "banana" რომელ ინდექსზეა.
fruit=["apple", "banana", "orange", "apple", "kiwi"]
fruit.append("melon")
fruit.insert(1,"grape")   
fruit.pop(3)
print(fruit)
print(fruit.count("apple"))
print(fruit.index("banana"))


# 4) მოცემულია სია:
# ["pizza", "burger", "pizza", "pasta", "burger"]

# გააკეთე ისე, რომ:

# დაამატო "salad" ბოლოში
# "pasta" ჩასვა სიის დასაწყისში
# წაშალო ერთი "burger"
# გაიგო რამდენჯერ არის "pizza"
# იპოვო "salad"-ის ინდექსი
foods=["pizza", "burger", "pizza", "pasta", "burger"]
foods.append("salad")
foods.insert(0,"pasta")
foods.pop(2)
print(foods)
print(foods.count("pizza"))
print(foods.index("salad"))


# 5) მოცემულია:
# ["Minecraft", "FIFA", "GTA", "Minecraft", "Fortnite"]

# დაამატე "Roblox" ბოლოში
# ჩასვი "Valorant" ინდექსზე 2
# ამოაგდე "GTA" მისი ინდექსით
# წაშალე "Fortnite"
# დაითვალე "Minecraft"-ის რაოდენობა
# იპოვე "Roblox"-ის ინდექსი
games=["Minecraft", "FIFA", "GTA", "Minecraft", "Fortnite"]
games.append("Roblox")
games.insert(2,"valorant")
games.remove("Fortnite")
print(games.count("Minecraft"))
print(games.index("Roblox"))
# 6) ახსენით დღეს ნასწავლი ფუნქციები კომენტარების გამოყენებით, რა რას აკეთებს
#append- ლისთის ბოლოში ამატებს რასაც ჩაწერ
#pop- შლის ლისთიდან იმ ელემენტს რომელ ინდექზეც არის და მიუთოითებ
#count-ითვლის ლისთში რამდენია ელემენტი
#index-ითვლის რომელ ინდექზეა ელემენტი
#insert-ამატებს სადაც გინდა ოღონდ საჭიროა ინდეხსის და ელემენტის მითითება
#remove-შლის ელემენტს ლისთიდან
