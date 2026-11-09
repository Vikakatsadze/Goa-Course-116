#მომხმარებელს შემოაყვანინეთ ერთი რიცხვი, შემდგომ შეამომწეთ, იმ შემთხვევაში თუ რიცხვი ლუწია გამოუტანეთ ტერმინალში "Your number is even!" ყველა სხვა შემთხვევაში "Your number is odd!"

num = int(input("შეიყვანე რიცხვი: "))

if num % 2 == 0:
    print("Your number is even!")
else:
    print("Your number is odd!")