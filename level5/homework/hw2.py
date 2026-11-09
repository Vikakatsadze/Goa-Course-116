#მომხმარებელს შემოაყვანინეთ ორი რიცხვი. გამოთვალეთ მათი ჯამი, სხვაობა, ნამრავლი და განაყოფი და დაბეჭდეთ შედეგები.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)

if num2 != 0:
    print("Quotient:", num1 / num2)
else:
    print("Division by zero is not allowed")


#+ — ჯამი.


#- — სხვაობა.


#* — ნამრავლი.


#/ — განაყოფი.


#if num2 != 0 ამოწმებს, რომ მეორე რიცხვი ნულის ტოლი არ იყოს, რადგან ნულზე გაყოფა შეუძლებელია.    