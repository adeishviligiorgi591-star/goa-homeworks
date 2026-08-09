#while loop-ის გამოყენებით გამოიტანეთ რიცხვები 1-დან 20-მდე. როდესაც რიცხვი გახდება 10, გამოიყენეთ break და გააჩერეთ ციკლი.
number=1
while number<=20:
    print(number)
    if number==10:
        break
    number+=1

#while loop-ის გამოყენებით გამოთვალეთ 1-დან 50-მდე ყველა რიცხვის ჯამი. გამოიყენეთ total ცვლადი.
number=1
total=0
while number<=50:
    total+=number
    number+=1
print(total)
#მომხმარებელს შემოატანინეთ რიცხვები. სანამ მომხმარებელი არ შეიყვანს 0-ს, დაამატეთ ყველა რიცხვი total ცვლადში. 0-ის შეყვანისას გამოიყენეთ break და ბოლოს გამოიტანეთ ჯამი.
total=0
while True:
    number=int(input("Enter your num:"))
    if number==0:
       break
    total+=number
    number+=1
print(total)



#4.while loop ის გამოყენებით გამოთვალეთ 1 დან 200 მდე ყველა კენტი რიცხვის ჯამი და შეინახეთ sum ცვლადში და გამოიტანეთ
total=0
number=1
while number<=200:
    if number%2==1:
        total+=number
    number+=1
print(total)
