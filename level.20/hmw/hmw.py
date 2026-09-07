#level 20:
#1.მომხმარებელს სთხოვე შეიყვანოს თავისი საყვარელი წიგნის დასახელება. დაბეჭდე ეს ტექსტი ჯერ პირველი და ბოლო ასოს გამოყენებით (ინდექსებით).
book=input("Enter your favourite book: ")
print(book[0])
print(book[-1])


#2.შექმენი ცვლადი user_city = "tbilisi". დაბეჭდე ეს ქალაქი ისე, რომ პირველი ასო იყოს დიდი.
user_city = "tbilisi"
print(user_city.capitalize())


#3.მომხმარებელს სთხოვე შეიყვანოს თავისი საყვარელი ფრაზა. დაბეჭდე ეს შეტყობინება სრულად დიდ ასოებში.
words=input("შეიყვანეთ თქვენი საყვარელი ფრაზა: ")
print(words.upper())


#4.მოცემულია ტექსტი: text = "learning python is very interesting and rewarding". დაითვალე და დაბეჭდე, რამდენჯერ გვხვდება ასო "e" ამ ტექსტში.
text = "learning python is very interesting and rewarding"
print(text.count("e"))


#5.შექმენი ცვლადი sentence = "I like offline games.". შეცვალე სიტყვა "offline" სიტყვით "online" და დაბეჭდე მიღებული ახალი წინადადება.
sentence = "I like offline games"
print(sentence.replace("offline","online"))


#6.მოცემულია ტექსტი: text = "Welcome to the Python course". იპოვე და დაბეჭდე, მერამდენე ინდექსზე იწყება სიტყვა "Python".
text = "Welcome to the Python course"
print(text.find("Python"))


#7.შექმენი ცვლადი word = "Developer". ამოჭერი და დაბეჭდე ამ სიტყვის პირველი 5 ასო.
word = "Developer"
print(word[:5])


#8.შექმენი ცვლადი promo_code = "SALE2024". გარდაქმენი ეს ტექსტი სრულად პატარა ასოებად და დაბეჭდე შედეგი.
promo_code = "SALE2024"
print(promo_code.lower())