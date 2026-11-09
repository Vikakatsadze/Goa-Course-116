#შექმენით პროგრამა სადაც პირველრიგში მომხმარებელი შემოიტანს რიცვხების რაოდენობას, შემდეგ for ციკლის გამოყენებით მაგდენი რიცხვი შემოატანინეთ input და ჩასვით სიაში

numbers = []

count = int(input("რამდენი რიცხვის შეყვანა გსურთ? "))

for i in range(count):
    number = int(input("შეიყვანეთ რიცხვი: "))
    numbers.append(number)

print("შეყვანილი რიცხვები:", numbers)

# მაქსიმალური რიცხვის პოვნა
maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

# მინიმალური რიცხვის პოვნა
minimum = numbers[0]

for number in numbers:
    if number < minimum:
        minimum = number

print("ყველაზე დიდი რიცხვი:", maximum)
print("ყველაზე პატარა რიცხვი:", minimum)