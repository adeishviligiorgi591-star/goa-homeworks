#level 18:

#1. Nested for loop-ის გამოყენებით დაბეჭდეთ 3x3 ვარსკვლავების კვადრატი.
for  i in range(3):
    for j in range(3):
        print("*",end=" ")
    print()
#2. Nested while loop-ის გამოყენებით დაბეჭდეთ 4 სტრიქონი, თითოეულში 5 ვარსკვლავით.
i= 1
while i<=4:
    j=1
    while j<=5:
        print("*", end=" ")
        j+=1
    print()
    i+=1

#3. Nested for loop-ის გამოყენებით დაბეჭდეთ ყველა შესაძლო წყვილი 1-დან 3-მდე რიცხვებით.
for i in range(1,3):
    for j in range(1,3):
        print(i,j)
#4. Nested while loop-ის გამოყენებით დაბეჭდეთ 1-დან 5-მდე რიცხვების გამრავლების ტაბულა.
i=1
while i<=4:
    j=1
    while j<=4:
        print(i, "X", j, "=", j * i)
        j+=1
    print()
    i+=1
#5. Nested for loop-ის გამოყენებით შექმენით ვარსკვლავების სამკუთხედი.
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()
#6. Nested while loop-ის გამოყენებით შექმენით რიცხვების სამკუთხედი 1-დან 5-მდე.
for i in range(1,5):
    for j in range(i):
        print(j,end=" ")
    print()
#7. Nested for loop-ის გამოყენებით შექმენით 5x5 კვადრატი, მაგრამ მესამე ვარსკვლავი არ დაბეჭდოთ. გამოიყენეთ continue.
for i in range(5):
    for j in range(1,6):
      if j==2:
        continue
      print("*", end=" ")
    print()
    
#8. მომხმარებელს შემოატანინეთ ორი რიცხვი და Nested while loop-ის გამოყენებით შექმენით ვარსკვლავების მართკუთხედი,
# სადაც პირველი რიცხვი იქნება სტრიქონების რაოდენობა, ხოლო მეორე — თითოეულ სტრიქონში ვარსკვლავების რაოდენობა
num1=int(input("Enter your first num: "))
num2=int(input("Enter your second num: "))
i=1
while i<=num1:
    j=1
    while j<=num2:
        print("*", end=" ")
        j+=1
    print()
    i+=1