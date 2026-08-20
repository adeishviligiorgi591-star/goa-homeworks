# 1) იპოვე ყველა ლუწი რიცხვის ჯამი 1-დან 100-მდე
i=1
total=0
while i<100:
    if i%2==0:
        total+=i
    i+=1
print(total)


# 2) მომხმარებელს შემოატანინე რიცხვი და დათვალე, რამდენი 
# რიცხვია 1-დან ამ რიცხვამდე ისეთი, რომელიც 3-ზე იყოფა.
num=int(input("Enter your num: "))
total=0
i=1
while i<num:
    if i%3==0:
        total+=1
    i+=1
print(total)


# 3) მომხმარებელს შემოატანინე 5 რიცხვი და for loop-ის გამოყენებით იპოვე მათი ჯამი
total=0
for i in range(5):
    num1=int(input("Enter your num1: "))
    total+=num1
print(total)
    


# 4) მომხმარებელს შემოატანინე 5 რიცხვი და იპოვე მათ შორის ყველაზე დიდი რიცხვი.
num=int(input("Enter your num: "))
for i in range(4):
    max_num=int(input("Enter your num: "))
    if num>max_num:
        max_num=num
print(max_num)
# 5) მომხმარებელს შემოატანინე სიტყვა და for loop-ის გამოყენებით გამოიტანე მისი თითოეული ასო ცალ-ცალკე.
word=input("Enter your word: ")
for i in word:
    print(i)