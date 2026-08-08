1. #While loop-ის გამოყენებით გამოიტანეთ 20-დან 1-მდე რიცხვები.
number=20
while number>=1:
    print(number)
    number-=1    


#2. #გამოიტანეთ 1-დან 50-მდე მხოლოდ ლუწი რიცხვები.
number=1
while number<=50:
      if number%2==0:
            print(number)
      number+=1
            

#3. #გამოიტანეთ 1-დან 100-მდე რიცხვები, რომლებიც იყოფა 5-ზე.
number=1
while number<=100:
      if number%5==0:
            print(number)
      number+=1


#4. #მომხმარებელს შემოატანინეთ რიცხვი და while loop-ის გამოყენებით გამოიტანეთ 1-დან ამ რიცხვამდე ყველა რიცხვი.
number=int(input("Enter your number: "))
while number>=1:
    print(number)
    number-=1


#5. #მომხმარებელს შემოატანინეთ რიცხვი და გამოიტანეთ 1-დან ამ რიცხვამდე მხოლოდ კენტი რიცხვები.
number=int(input("Enter your number: "))
while number>=1:
    if number%2==1:
        print(number)
    number-=1


#6. #მომხმარებელს შემოატანინეთ პაროლი. სანამ პაროლი არ იქნება "python123", მანამდე მომხმარებელს თავიდან შეაყვანინეთ პაროლი.
password="" 
while password!="python123":
    password=input("Enter your pssword: ")
print("password corect")

