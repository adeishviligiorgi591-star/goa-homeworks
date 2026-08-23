#1.გამოიტანე რიცხვები 1-დან 15-მდე, მაგრამ არ გამოიტანო 7.
for i in range(1,15):
    if i==7:
        continue
    print(i)


#2.გამოიტანე 2-დან 30-მდე რიცხვები, მაგრამ გამოტოვე ყველა რიცხვი, რომელიც ლუწია.
for i in range(2,30):
    if i%2==0:
        continue
    print(i)


#3.მომხმარებელს შეაყვანინე 7 რიცხვი და გამოიტანე მხოლოდ დადებითი რიცხვები.
for i in range(7):
    num=int(input("Enter your num: "))
    if num<0:
        continue
    print(num)


#4.გამოიტანე რიცხვები 1-დან 40-მდე, მაგრამ გამოტოვე რიცხვები, რომლებიც 4-ზე იყოფა.
for i in range(1,40):
    if i%4==0:
        continue
    print(i)
#5.მომხმარებელს შეაყვანინე 10 რიცხვი და თუ რიცხვი არის 0, არ გამოიტანო.
for i in range(10):
    num=int(input("Enter your num: "))
    if num==0:
        continue
    print(num)


#6.გამოიტანე 1-დან 25-მდე რიცხვები, მაგრამ გამოტოვე 10-დან 15-მდე რიცხვები.
for i in range(1,25):
    if i==10 or i==11 or i==12 or i==13 or i==14:
        continue
    print(i)


#7.გამოიტანე რიცხვები 5-დან 50-მდე, მაგრამ არ გამოიტანო რიცხვები, რომლებიც 7-ზე იყოფა.
for i in range(5,50):
    if i%7==0:
        continue
    print(i)


#8.მომხმარებელს შეაყვანინე 5 რიცხვი. თუ რიცხვი 10-ზე მეტია, გამოტოვე და არ გამოიტანო.
for i in range(5):
    num=int(input("Enter your num: "))
    if num>10:
        continue
    print(num)