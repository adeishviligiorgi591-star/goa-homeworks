#1. მომხმარებელს შეაყვანინე ასაკი და შეამოწმე, არის თუ არა ის 18 წლის ან მეტი.
age=int(input("Enter your age: "))
print(age>=18)


#2. მომხმარებელს შეაყვანინე ორი რიცხვი და შეამოწმე, არის თუ არა ორივე რიცხვი 10-ზე მეტი `and`-ის გამოყენებით.
num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))
print(num1>10 and num2>10)


#3. მომხმარებელს შეაყვანინე ორი რიცხვი და შეამოწმე, არის თუ არა რომელიმე მათგანი 100-ზე მეტი `or`-ის გამოყენებით.
num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))
print(num1>100 or num2>100)


#4. შექმენი ცვლადი `is_weekend = True`. გამოიყენე `not` და დაბეჭდე მისი საპირისპირო მნიშვნელობა.
is_weekend=True
print(not is_weekend)


#5. მომხმარებელს შეაყვანინე ასაკი და შეამოწმე, არის თუ არა ის 16 წლის ან მეტი და 60 წლის ან ნაკლები. გამოიყენე `and`.
age=int(input("Enter your age: "))
print(age>=16 and age<=60)


#6. შექმენი ორი Boolean ცვლადი:  და `has_invitation`. შეამოწმე, შეუძლია თუ არა ადამიანს ღონისძიებაზე შესვლა, თუ მას ბილეთი ან მოწვევა აქვს. გამოიყენე `or`.
has_invitation=True
has_ticket=False
print(has_invitation or has_ticket)


#7. მომხმარებელს შეაყვანინე ორი რიცხვი და შეამოწმე, არის თუ არა პირველი რიცხვი მეორეზე მეტი და მეორე რიცხვი 10-ზე მეტი. გამოიყენე `and`.
num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))
print(num1>num2 and num2>10)


#8. შექმენი პროგრამა, რომელიც მომხმარებელს ეკითხება ასაკს და ამოწმებს, არის თუ არა ის 13 წლის ან მეტი და 18 წლის ან ნაკლები. გამოიყენე `and`.
age=int(input("Enter your age: "))
print(age>=13 and age<=18)

