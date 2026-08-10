#1)while loop-ის გამოყენებით გამოთვალეთ 1-დან 100-მდე ყველა რიცხვის ჯამი. გამოიყენეთ total ცვლადი.
total=0
number=1
while number<100:
     total+=number
     number+=1
print(total)


#2)while loop-ის გამოყენებით გამოთვალეთ 1-დან 100-მდე ყველა კენტი რიცხვის ჯამი.
total=0
number=1
while number<100:
    if number%2==1:
          total+=number
    number+=1
print(total)


#3)while loop-ის გამოყენებით გამოიტანეთ რიცხვები 1-დან 50-მდე. როდესაც რიცხვი გახდება 25, გამოიყენეთ break და გააჩერეთ ციკლი.
num=1
while num<50:
     print(num)
     if num==25:
          break
     num+=1


#4)მომხმარებელს შეაყვანინეთ რიცხვები. სანამ მომხმარებელი არ შეიყვანს 0-ს, დაამატეთ
#  რიცხვები total ცვლადში. 0-ის შეყვანისას გამოიყენეთ break და ბოლოს გამოიტანეთ ჯამი.
total=0
while True:
     num=int(input("Enter your num: "))
     if num==0:
          break
     total+=num
     num+=1
print(total)


#5)მომხმარებელს შემოატანინეთ რიცხვი n და while loop-ის
#  გამოყენებით გამოთვალეთ 1-დან n-მდე ყველა ლუწი რიცხვის ჯამი.
number=1
total=0
n=int(input("Enter your num:" ))
while number<n:
     if number%2==0:
          total+=number
     number+=1
print(total)
#6)მომხმარებელს შეაყვანინეთ რიცხვები. თუ მომხმარებელი შეიყვანს უარყოფით რიცხვს, გამოიყენეთ 
# break. დადებითი რიცხვები დაამატეთ total ცვლადში და ბოლოს გამოიტანეთ ჯამი.
total=0
while True:
     num=int(input("Enter your num: "))
     if num<0:
          break
     total+=num
print(total)

#7)მომხმარებელს შეაყვანინეთ რიცხვები. თუ შეიყვანს 0-ს, გამოიყენეთ break. ყველა დადებითი რიცხვი დაამატეთ total ცვლადში, ხოლო უარყოფითი რიცხვები გამოტოვეთ.
total=0
while True:
     num=int(input("Enter your num: "))
     if num==0:
          break
     elif num>0:
          total+=num
print(total)




