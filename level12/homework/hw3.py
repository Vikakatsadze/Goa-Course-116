#მომხმარებელს შეაყვანინეთ 7 მთელი რიცხვი და შეინახეთ ისინი სიაში.

#პროგრამამ უნდა:

#- დაბეჭდოს ყველა შეყვანილი რიცხვი;
#- დათვალოს, რამდენი რიცხვია დადებითი;
#- დათვალოს, რამდენი რიცხვია უარყოფითი;
#- დათვალოს, რამდენი რიცხვია ნულის ტოლი;
#- დაბეჭდოს მიღებული შედეგები.

#BONUS
#ციკლისა და პირობითი ოპერატორების გამოყენებით იპოვეთ სიაში ყველაზე დიდი რიცხვი max() ფუნქციის გამოყენების გარეშე.

numbers = []

for i in range(7):
    number = int(input("შეიყვანეთ რიცხვი: "))
    numbers.append(number)

positive = 0
negative = 0
zero = 0

print("შეყვანილი რიცხვები:")

for number in numbers:
    print(number)

    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zero += 1

print("დადებითი რიცხვები:", positive)
print("უარყოფითი რიცხვები:", negative)
print("ნულის ტოლი რიცხვები:", zero)

biggest = numbers[0]

for number in numbers:
    if number > biggest:
        biggest = number

print("ყველაზე დიდი რიცხვია:", biggest)