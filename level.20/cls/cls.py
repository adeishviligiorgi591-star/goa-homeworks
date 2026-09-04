# 1)მოითხოვე შეიყვანოს თავისი სახელი და გვარი. დაბეჭდე შეყვანილი ტექსტი ჯერ სრულად
#  დიდ ასოებით, ხოლო შემდეგ სრულად პატარა ასოებით.
name_and_lastname=input("Enter name and last name: ")
print(name_and_lastname.upper())
print(name_and_lastname.lower())


# 2) შექმენი ცვლადი, რომელშიც შეინახავ ტექსტს პატარა ასოებით: "python is cool".
#  დაბეჭდე ეს ტექსტი ეკრანზე ისე, რომ მხოლოდ პირველი ასო იყოს დიდი, ხოლო დანარჩენი — პატარა.
sentence="python is cool"
print(sentence.capitalize())


#შექმენი ცვლადი: sentence = "I love cats, cats are my favorite animal.". შეცვალე ტექსტში
#  არსებული ყველა სიტყვა "cats" სიტყვით "dog" და დაბეჭდე მიღებული ახალი წინადადება.
sentence = "I love cats, cats are my favorite animal"
print(sentence.replace("cats","dogs"))


# 4) მოცემულია ტექსტი: text = "Python is the best programming language". 
# იპოვე და დაბეჭდე, მერამდენე პოზიციაზე (ინდექსზე) იწყება სიტყვა "best". ასევე შეამოწმე, 
# რას დააბრუნებს პროგრამა, თუ მოძებნი სიტყვას "Python".
text = "Python is the best programming language"
print(text.find("best"))
print(text.find("Python"))


# 5) შექმენი ცვლადი: text = "Banana, Apple, Banana, Orange, Banana". დაითვალე და 
# დაბეჭდე, რამდენჯერ გვხვდება სიტყვა "Banana" ამ ტექსტში.
text = "Banana, Apple, Banana, Orange, Banana"
print(text.count("Banana"))
