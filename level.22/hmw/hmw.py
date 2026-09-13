# Level 22:
# 1) მომხმარებელს შემოაყვანინე ტექსტი. strip() მეთოდით ჩამოაშორე ზედმეტი ჰარები,
#  ხოლო lower() მეთოდით გადაიყვანე ყველა ასო პატარაში. დაბეჭდე საბოლოო ტექსტი.
text=input("Enter your text: ")
print(text.strip())
print(text.lower())


# 2) მომხმარებელს შემოაყვანინე პაროლი. isalnum() მეთოდით შეამოწმე, 
# შედგება თუ არა იგი მხოლოდ ასოებისგან ან/და ციფრებისგან, ხოლო
#  isupper() მეთოდით შეამოწმე, არის თუ არა ყველა ასო დიდი. დაბეჭდე ორივე შემოწმების შედეგი (True/False).
password=input("Enter your password: ")
print(password.isalnum())
print(password.isupper())


# 3) შექმენი ცვლადი text = "Python Programming". startswith("Py") მეთოდით შეამოწმე, იწყება
#  თუ არა ტექსტი "Py"-თი, ხოლო find("Gram") მეთოდით იპოვე "Gram"-ის დაწყების ინდექსი. დაბეჭდე ორივე შედეგი.
text = "Python Programming"
print(text.startswith("Py"))
print(text.find("gram"))


# 4) მომხმარებელს შემოაყვანინე ტექსტი. replace() მეთოდით ყველა ჰარი (space) ჩაანაცვლე დეფისით 
# ("-"), ხოლო upper() მეთოდით გადაიყვანე ყველა ასო დიდში. დაბეჭდე მიღებული ტექსტი.
text=input("Enter your text: ")
print(text.replace(" ", "-"))
print(text.upper())


# 5) შექმენი ცვლადი raw_data = "  html,css,javascript  ". ჯერ strip() მეთოდით აშორე
#  ჰარები, ხოლო შემდეგ split(",") მეთოდით დაყავი ეს ტექსტი სიად. დაბეჭდე მიღებული სია.
raw_data = "  html,css,javascript  "
print(raw_data.strip())
print(raw_data.split(","))


# 6) შექმენი სია words = ["hello", "world", "python"]. uppercase მეთოდების და join-ის
#  გამოყენებით, შეაერთე ეს სიტყვები ტირეთი ("-") ისე, რომ თითოეული სიტყვის პირველი
#  ასო იყოს დიდი (გამოიყენე title() ან capitalize()). დაბეჭდე შედეგი.
words = ["hello", "world", "python"]
word="-".join(words)
print(word.title())


# 7) შექმენი ცვლადი message = "  Hello World  ". lstrip() მეთოდით მოაშორე
#  ჰარები მხოლოდ მარცხნიდან, ხოლო [::-1] Slicing-ის გამოყენებით ამოატრიალე მთლიანი ტექსტი უკუღმა. დაბეჭდე შედეგი.
message = "  Hello World  "
print(message.lstrip())
print(text[::-1])


# 8) მომხმარებელს შემოაყვანინე ტექსტი. isdigit() მეთოდით შეამოწმე, არის თუ 
# არა შეყვანილი ტექსტი მხოლოდ ციფრები. თუ არის, slicing-ით [:3] დაბეჭდე პირველი 3 ციფრი.
number=input("Enter your num: ")
if number.isdigit():
    print(number[:3])



# 9) შექმენი ცვლადი text = "Learning Python Is Fun". lower() მეთოდით გადაიყვანე
#  მთლიანი ტექსტი პატარა ასოებში, split() მეთოდით დაყავი სიტყვებად და დაბეჭდე მიღებული სია.
text = "Learning Python Is Fun"
print(text.lower())
print(text.split(","))


# 10) შექმენი ცვლადი word = "Database". slicing-ით [-3:] ამოიღე ბოლო 3 სიმბოლო და
#  upper() მეთოდით გადაიყვანე დიდ ასოებში. დაბეჭდე მიღებული შედეგი.
word = "Database"
words=word[-3:].upper()
print(words)

