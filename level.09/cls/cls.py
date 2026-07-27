#1) მომხმარებელს შემოატანინე თავისი ასაკი, შემდეგ შეამოწმე თავისი ასაკია მეტია ან ტოლია 18ზე, კონსოლში გამოვიდეს "სრულწლოვანი ხართ".
age=int(input("Enter your age: "))
if age>=18:
    print("you are adult")


#2) მომხმარებელს შემოატანინე ორი რიცხვი (num1, num2), შეამოწმე თუ num1 მეტია num2ზე გამოვიდეს "პირველი რიცხვი მეტია",
num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))
if num1>num2:
    print("first number is bigger")

#3) მომხმარებელს კიღხე რა არის სწორი რიცხვი. თუ რიცხვი უდრის 777 დაბეჭდოს "რიცხვი გამოცნობილია"
number=int(input("Enter your number: "))
if number==777:
    print("you got right number")
   

#4) მომხმარებელს შემოატანინე თავისი სიმაღლე, თუ სიმაღლე მეტია ან უდრის 1.70ზე დაბეჭდოს "შენ მაღალი ხარ" 
height=int(input("Enter your height: "))
if height>=1.70:
    print("you are tall")