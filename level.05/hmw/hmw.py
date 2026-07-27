#1)მომხმარებელს შეაყვანინე ასაკი, გადააქციე  int-ად და დაბეჭდე შედეგი.,
age = int(input("enter your age: "))
print(age)


#2)მომხმარებელს შეაყვანინე ასაკი, გადააქციე int-ად, მიუმატე 10 და დაბეჭდე შედეგი.,
age=int(input("enter your age"))
print(age+10)


#3)მომხმარებელს შეაყვანინე ორი რიცხვი, ორივე გადააქციე int-ად და დაბეჭდე მათი ჯამი.,
age=int(input("enter your age: "))
fav_number=int(input("enter your fav number: "))


#4)მომხმარებელს შეაყვანინე სიმაღლე, გადააქციე float-ად და დაბეჭდე მისი ტიპი.,
height=float(input("Enter your height: "))


#5)მომხმარებელს შეაყვანინე პროდუქტის ფასი, გადააქციე float-ად, მიუმატე 5.5 და დაბეჭდე შედეგი.,
price=float(input("Enter your price: "))
print(price+5.5)


#6)შექმენი ცვლადები name, age და height. დაბეჭდე თითოეულის ტიპი type-ის გამოყენებით.,
name="gio"
age=14
height=1.65
print(type(name))
print(type(age))
print(type(height))


#7)მომხმარებელს შეაყვანინე სახელი და ასაკი. ასაკი გადააქციე int-ად და f-string-ის გამოყენებით დაბეჭდე:
#hello Nika you are 15 years old,
name=input("Enter your name: ")
age=int(input("Enter your age: "))
print(f"hello {name} you are {age} years old")


#8)მომხმარებელს შეაყვანინე ორი რიცხვი, ორივე გადააქციე int-ად და დაბეჭდე მათი ნამრავლი.,
num1=int(input("Enter your number"))
num2=int(input("Enter your number"))
print(num1*num2)


#9)მომხმარებელს შეაყვანინე საყვარელი რიცხვი, გადააქციე int -ად, გამოაკელი 3 და დაბეჭდე შედეგი.,
fav_num=int(input("Enter your fav num: "))
print(fav_num-3)


#10)მომხმარებელს შეაყვანინე ასაკი, გადააქციე int-ად, შემდეგ დაბეჭდე:,
#ასაკი
#ასაკს დამატებული 10
#ასაკის ტიპი type-ის გამოყენებით.

age=input("Enter your age: ")
print(age+10)
print(type(age))