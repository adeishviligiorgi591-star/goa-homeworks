#1) კომენტარების სახით ახსენით რა არის input() ფუნქცია და რისთვის გამოიყენება.
#input() ფუნქცია არის რომ მიიღოს მომხმარებლისგან ინფორმაცია


#2) მომხმარებელს შემოატანინეთ თავისი სახელი და დაბეჭდეთ, რა სახელი შემოიტანა.
name =input("enter your name: ")


#3) მომხმარებელს შემოატანინეთ თავისი საყვარელი ფერი და დაბეჭდეთ.
colour = input("enter your fav colour: ")


#4) კომენტარებით ახსენით, რა არის f-string და რატომ არის მისი გამოყენება მოსახერხებელი.

# f-string არის ცვლადებით ტექსტში მომხმარებელზე ინფორმაციის შემოტანა და მას სწორედ იმიტომ იყენებენ
#  რომ მომხმარებლის შესახებ ინფორმაცია გაიგოს და გამოიყენოს


#5) მომხმარებელს შემოატანინეთ თავისი ასაკი და f-string-ის გამოყენებით დაბეჭდეთ:
#I am {ასაკი} years old
age=input("enter your age: ")
print(f"I am {age} years old")


#6) მომხმარებელს შემოატანინეთ თავისი გვარი და f-string-ის გამოყენებით დაბეჭდეთ:
#Your surname is {გვარი}
surname= input("enter your surname: ")
print(f"your surname is{surname}")


#7) მომხმარებელს შემოატანინეთ თავისი საყვარელი ცხოველი და დაბეჭდეთ:
#My favorite animal is {ცხოველი}
#f-string-ის გამოყენებით.
animal = input("enter your fav animal: ")
print(f"my favourite animal is {animal}")


#8) მომხმარებელს შემოატანინეთ თავისი საყვარელი სპორტი და დაბეჭდეთ:
#I like {სპორტი}
#f-string-ის გამოყენებით.
sport=input("enter your favourite sport: ")
print(f"I like {sport}")


#9) მომხმარებელს შემოატანინეთ ქალაქის სახელი და ქვეყანა. შემდეგ f-string-ის გამოყენებით დაბეჭდეთ:
#I live in {ქალაქი}, {ქვეყანა}
country=input("enter your country: ")
city= input ("enter your city: ")
print(f"I live in {city},{country}")


#10) მომხმარებელს შემოატანინეთ თავისი სახელი, ასაკი და საყვარელი ფერი. შემდეგ f-string-ის გამოყენებით დაბეჭდეთ:
#My name is {სახელი}, I am {ასაკი} years old and my favorite color is {ფერი}
name = input("Enter your name: ")
age = input("Enter your age: ")
colour = input("Enter your colour: ")
print(f"My name is {name}, I am {age} and my favourite colour is {colour}")