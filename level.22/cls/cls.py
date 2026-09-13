# level  22:
# 1) მოცემულია:
# text = "I like JavaScript"

# replace() მეთოდის გამოყენებით შეცვალე "JavaScript" → "Python".
text = "I like JavaScript"
print(text.replace("JavaScript", "Python"))

# 2) მომხმარებელს შემოატანინე სიტყვა და გამოიტანე:
# მთლიანად პატარა ასოებით;
# მთლიანად დიდი ასოებით.
# მოცემულია:
# text = "   Hello Python   "
text = "   Hello Python   "
print(text.lower())
print(text.upper())

# 3) strip() მეთოდის გამოყენებით მოაშორე ტექსტის დასაწყისში და ბოლოში არსებული ზედმეტი space-ები.
text = "   Hello Python   "
print(text.strip())
# 4) მოცემულია:
# text = "python is a programming language"

# title() მეთოდის გამოყენებით თითოეული სიტყვის პირველი ასო გახადე დიდი.
text = "python is a programming language"
print(text.title())
# 5) მოცემულია:
# words = ["Python", "is", "easy"]

# join() მეთოდის გამოყენებით მიიღე:

# Python is easy
words = ["Python", "is", "easy"]
word=" ".join(words)
print(word)
# 6) მოცემულია:
# words = ["2026", "09", "11"]

# join() მეთოდის გამოყენებით მიიღე:

# 2026-09-11
words = ["2026", "09", "11"]
word="-".join(words)
print(word)
# 7) მოცემულია:
# text = "Python"

# slicing-ის გამოყენებით გამოიტანე პირველი 3 სიმბოლო:
# Pyt
text = "Python"
print(text[:3])
# 8) მოცემულია:
# text = "Programming"

# slicing-ის გამოყენებით გამოიტანე ბოლო 3 სიმბოლო.
text = "Programming"
print(text[8:])