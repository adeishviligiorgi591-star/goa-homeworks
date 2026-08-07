#1. While loop ის გამოყენები თგამოიტანეთ 20 მდე რიცხვები
number=1
while number<=20:
    print(number)
    number+=1


#2. გამოიტანეთ 5დან 50 მდე მხოლოდ კენტი რიცხვები
number=5
while number<=50:
    if number%2==1:
       print(number)
    number+=1


#3. გამოიტანეთ რიცხვები 50 მდე რომლებიც იყოფა 10ზე
number=10
while number<=50:
    if number%10==0:
        print(number)
    number+=1
#4.# მომხმარებელ შემოატანინეთ პაროლი, სანამ პაროლი არ დაემთხვევა 102110 მანამდე ისე თავიდან შეიყვანოს მომხმარებელმა პაროლი
password=""
while password!="102110":
    password=input("Enter your password")
print("password correct")
          



