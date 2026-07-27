#1) მომხმარებელს შემოატანინე ასაკი. თუ ასაკი არის 18 ან მეტი, დაბეჭდე:
#"შენ სრულწლოვანი ხარ."
age=int(input("Enter your age: "))
if age>=18:
    print("you are adult")


#2) მომხმარებელს შემოატანინე რიცხვი. თუ ის დადებითია, დაბეჭდე:
"დადებითი რიცხვია."
number=int(input("Enter your number: "))
if number>0:
    print("its positive number")


#3) მომხმარებელს შემოატანინე პაროლი. თუ პაროლი არის "python123", დაბეჭდე:
#"პაროლი სწორია."
password=input("Enter your password: ")
if password=="python123":
    print("password is correct")


#4) მომხმარებელს შემოატანინე თავისი ქულა. თუ ქულა არის 90 ან მეტი, დაბეჭდე:
#"შესანიშნავი შედეგი!"
score=int(input("Enter your score: "))
if score>=90:
    print("wonderful result")


#5) მომხმარებელს შემოატანინე ტემპერატურა. თუ ტემპერატურა 0-ზე ნაკლებია, დაბეჭდე:
#"გარეთ ყინავს."
temperature=int(input("Enter local temperature: "))
if temperature<0:
    print("its freezing outside")


#6) მომხმარებელს შემოატანინე სახელი. თუ შემოტანილი სახელი არის "Giorgi", დაბეჭდე:
#"მოგესალმები, Giorgi!"
name=(input("Enter your name: "))
if name=="giorgi":
    print("hello giorgi")

#7) მომხმარებელს შემოატანინე რიცხვი. თუ ის ლუწია, დაბეჭდე:
#"ლუწი რიცხვია."
number=int(input("Enter your number: "))
if number%2==0:
    print("its even number")


#8) მომხმარებელს შემოატანინე თანხა. თუ თანხა არის 100 ან მეტი, დაბეჭდე:
#"შეგიძლია ფასდაკლების მიღება."
cash=int(input("Enter your cash: "))
if cash>=100:
    print("you can get a discount")


#9) მომხმარებელს შემოატანინე კვირის დღე. თუ შემოტანილია "Sunday", დაბეჭდე:
#"დღეს დასვენების დღეა."
day=input("Enter a week day: ")
if day=="sunday":
    print("today is weekend")


#10) მომხმარებელს შემოატანინე ორი რიცხვი. თუ პირველი რიცხვი მეორეზე მეტია, დაბეჭდე:
#"პირველი რიცხვი უფრო დიდია."
number1=int(input("Enter your first number: "))
number2=int(input("Enter your second number: "))
if number1>number2:
    print("first number is bigger than second number")