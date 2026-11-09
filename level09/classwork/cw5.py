#მომხმარებელს შემოაყვანინეთ თავისი ასაკი, შემდგომ იმ შემთხვევაში თუ მისი ასაკი მეტია 18-ზე დაეწერეთ "You are adult!", ყველა სხვა შემთხვევაში დაუწერეთ "You are not adult!".

age = int(input("შეიყვანე ასაკი: "))

if age > 18:
    print("You are adult!")
else:
    print("You are not adult!")