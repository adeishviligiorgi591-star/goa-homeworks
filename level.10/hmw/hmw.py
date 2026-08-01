#1. მომხმარებელს შეაყვანინე ასაკი. თუ ასაკი 18 ან მეტია, დაბეჭდე Adult, სხვა შემთხვევაში Child.
age=int(input("Enter your age: "))
if age>=18:
    print("Adult")
else:
    print("child")


#2. მომხმარებელს შეაყვანინე რიცხვი. თუ რიცხვი დადებითია, დაბეჭდე Positive, თუ ნულის ტოლია — Zero, სხვა შემთხვევაში — Negative.
num=int(input("Enter your num: "))
if num>0:
    print("positive")
elif num==0:
    print("zero")
else:
    print("negative")


#3. მომხმარებელს შეაყვანინე ქულა. თუ ქულა 90 ან მეტია, დაბეჭდე Grade A, თუ 70 ან მეტია — Grade B, თუ 50 ან მეტია — Grade C, სხვა შემთხვევაში — Failed.
score=int(input("Enter your score: "))
if score>=90:
    print("Grade A")
elif score>=70 and score<90:
    print("Grade B")
elif score>=50 and score<70:
    print("Grade C")
else:
    print("Failed")


#4. მომხმარებელს შეაყვანინე ტემპერატურა. თუ ტემპერატურა 30 ან მეტია, დაბეჭდე Hot, თუ 15 ან მეტია — Warm, სხვა შემთხვევაში — Cold.
temperature=int(input("Enter your temperature: "))
if temperature>=30:
    print("Hot")
elif temperature>=15 and temperature<30:
    print("warm")
else:
    print("Cold")


#5. მომხმარებელს შეაყვანინე თანხა. თუ თანხა 100 ან მეტია, დაბეჭდე Expensive, თუ 50 ან მეტია — Medium, სხვა შემთხვევაში — Cheap.
cash=int(input("Enter your cash: "))
if cash>=100:
    print("Expensive")
elif cash>=50 and cash<100:
    print("Medium")
else:
    print("Cheap")


#6. მომხმარებელს შეაყვანინე საათი (0-23). თუ საათი 12-ზე ნაკლებია, დაბეჭდე Morning, თუ 18-ზე ნაკლებია — Afternoon, სხვა შემთხვევაში — Evening.
time=int(input("Enter your time: "))
if time<12:
    print("Morning")
elif time<18 and time>12:
    print("Afternoon")
else:
    print("Evening")


#7. მომხმარებელს შეაყვანინე ორი რიცხვი. თუ პირველი რიცხვი მეორეზე მეტია, დაბეჭდე First number is bigger, თუ ნაკლებია — Second number is bigger,
#სხვა შემთხვევაში — Numbers are equal.
num1=int(input("Enter your first num: "))
num2=int(input("Enter your second num: "))
if num1>num2:
    print("First number is bigger")
elif num1<num2:
    print("Second number is bigger")
else:
    print("Numbers are equal")


#8. მომხმარებელს შეაყვანინე ასაკი. თუ ასაკი 6-ზე ნაკლებია, დაბეჭდე Kindergarten, თუ 18-ზე ნაკლებია — School, სხვა შემთხვევაში — University or Work.
age=int(input("Enter your age: "))
if age<6:
    print("Kindergarten")
elif age<18 and age>6:
    print("School")
else:
    print("University or work")

