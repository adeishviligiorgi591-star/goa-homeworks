#1) შექმენი ორი ცვლადი, სადაც მომხმარებელს შემოატანინებ ორ რიცხვს.
age=input("Enter your age: ")
fav_number=input("Enter your fav number: ")


#2) პირველ დავალებაში შექმნილი ორივე ცვლადი გადაიყვანე ინტეჯერად (`int()`).
age=int(input("Enter your age: "))
fav_number=int(input("Enter your fav number: "))


#3) დაბეჭდე ამ ორ რიცხვზე ყველა მათემატიკური მოქმედების შედეგი:
#(+, -, *, /, %, //, **)
age=int(input("Enter your age: "))
fav_number=int(input("Enter your fav number: "))
print(age+fav_number)
print(age-fav_number)
print(age*fav_number)
print(age/fav_number)
print(age%fav_number)
print(age//fav_number)
print(age**fav_number)


#4) შექმენი ცვლადი, სადაც მომხმარებელს შემოატანინებ თავის სახელს.
name=input("Enter your name: ")


#5) შექმენი ცვლადი, სადაც მომხმარებელს შემოატანინებ თავის ასაკს.
age=input("Enter your age: ")


#6) f-string-ის გამოყენებით დაბეჭდე:
#"Hello, my name is {სახელი} and I am {ასაკი} years old."
name=input("Enter your name: ")
age=input("Enter your age: ")
print(f"Hello, my name is {name} and I am {age} years old")


#7) მომხმარებელს შემოატანინე თავისი საყვარელი ფერი და f-string-ის გამოყენებით დაბეჭდე:
#"My favorite color is {ფერი}."
fav_colour=input("your fav colour: ")
print(f"My favourite colour is {fav_colour}")


#8) მომხმარებელს შემოატანინე ორი რიცხვი, გადაიყვანე ინტეჯერებად და დაბეჭდე მათი ჯამი, სხვაობა და ნამრავლი.
num1=int(input("Enter your num1: "))
num2=int(input("Enter your num2: "))
print(num1+num2)
print(num1-num2)
print(num1*num2)


#9) მომხმარებელს შემოატანინე სახელი, გვარი და ქვეყანა. f-string-ის გამოყენებით დაბეჭდე:
#"My name is {სახელი} {გვარი} and I live in {ქვეყანა}."
name=input("Enter your name: ")
surname=input("Enter your surname: ")
country=input("Enter your country: ")
print(f"My name i {name}{surname} and I live in{country}")


#10) მომხმარებელს შემოატანინე ორი რიცხვი, გადაიყვანე ინტეჯერებად და დაბეჭდე:
#- პირველი რიცხვი მეორე ხარისხში.
#- მეორე რიცხვი მესამე ხარისხში.
num1=int(input("Enter your num"))
num2=int(input("Enter your num"))
print(num1**2)
print(num2**3)




