#1. მომხმარებელს შეაყვანინე ორი რიცხვი და დაბეჭდე მათი ჯამი, სხვაობა, ნამრავლი და განაყოფი.
num1=int(input("Enter your first number: "))
num2=int(input("Enter your secend number: "))
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)


#2. მომხმარებელს შეაყვანინე რიცხვი, გამოაკელი 5 და შეადარე მიღებული შედეგი 20-ს. დაბეჭდე შედარების შედეგი.
num1=int(input("Enter your number: "))
print((num1-5)>20)


#3. მომხმარებელს შეაყვანინე ორი რიცხვი და შეამოწმე:
 #  არის თუ არა მათი ჯამი 50-ზე მეტი;
 #  არის თუ არა მათი ნამრავლი 100-ის ტოლი;
 #  არის თუ არა პირველი რიცხვი მეორეზე ნაკლები.
num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))
print((num1+num2)>50)
print((num1*num2)==100)
print(num1<num2)


#4. მომხმარებელს შეაყვანინე რიცხვი და შეამოწმე, იყოფა თუ არა ის 3-ზე ნაშთის გარეშე `%` ოპერატორის გამოყენებით.
num=int(input("Enter your number: "))
print(num % 3)


#5. მომხმარებელს შეაყვანინე ორი რიცხვი და დაბეჭდე პირველი რიცხვის მეორეზე გაყოფის შედეგი `/`-ით, მთელზე გაყოფის შედეგი `//`-ით და ნაშთი `%`-ით.
num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))
print(num1/num2)
print(num1//num2)
print(num1%num2)


#6. მომხმარებელს შეაყვანინე რიცხვი და დაბეჭდე მისი კვადრატი და კუბი `**` ოპერატორის გამოყენებით.
num=int(input("Enter your number: "))
print(num**2)
print(num**3)


#7. მომხმარებელს შეაყვანინე ორი რიცხვი და შეამოწმე, არის თუ არა მათი სხვაობა 10-ზე მეტი, ნაკლები ან ტოლი.
num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))
print((num1-num2)>10)
print((num1-num2)<=10)


#8. მომხმარებელს შეაყვანინე რიცხვი და დაბეჭდე:
  # რიცხვი გამრავლებული 3-ზე;
  # რიცხვი აყვანილი მე-3 ხარისხში;
  # რიცხვის 5-ზე გაყოფის ნაშთი;
  # რიცხვის 5-ზე მთელზე გაყოფის შედეგი.
num=int(input("Enter your number: ")) 
print(num*3)
print(num**3)
print(num%5)
print(num//5)