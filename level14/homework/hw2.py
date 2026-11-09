#მომხმარებელს შემოაყვანინეთ 15 სხვადასხვა რიცხვი. პროგრამამ უნდა იპოვოს მათ შორის ყველაზე დიდი და ყველაზე პატარა რიცხვი, დაითვალოს დადებითი, უარყოფითი და ნულის ტოლი რიცხვების რაოდენობა. ასევე გამოთვალოს ყველა შეყვანილი რიცხვის საშუალო არითმეტიკული და დაადგინოს, საშუალო დადებითია, უარყოფითი თუ ნულის ტოლი.

numbers = []

for i in range(15):
    number = int(input("შეიყვანეთ რიცხვი: "))
    numbers.append(number)

# მაქსიმალური და მინიმალური რიცხვი
maximum = numbers[0]
minimum = numbers[0]

positive = 0
negative = 0
zero = 0
total = 0

for number in numbers:

    total += number

    if number > maximum:
        maximum = number

    if number < minimum:
        minimum = number

    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zero += 1

average = total / 15

print("\n====== შედეგები ======")
print("ყველა რიცხვი:", numbers)
print("ყველაზე დიდი:", maximum)
print("ყველაზე პატარა:", minimum)
print("დადებითი რიცხვები:", positive)
print("უარყოფითი რიცხვები:", negative)
print("ნულის ტოლი რიცხვები:", zero)
print("საშუალო არითმეტიკული:", round(average, 2))

if average > 0:
    print("საშუალო დადებითია")
elif average < 0:
    print("საშუალო უარყოფითია")
else:
    print("საშუალო ნულის ტოლია")