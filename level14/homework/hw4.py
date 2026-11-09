#შეიყვანეთ საწყისი და საბოლოო რიცხვები. პროგრამამ უნდა გაიაროს ამ დიაპაზონში არსებული ყველა მთელი რიცხვი და თითოეული მათგანი შეამოწმოს. თუ რიცხვი იყოფა 3-ზე და 5-ზე ერთდროულად, გამოიტანოს „FizzBuzz“; თუ მხოლოდ 3-ზე იყოფა — „Fizz“; თუ მხოლოდ 5-ზე იყოფა — „Buzz“; სხვა შემთხვევაში გამოიტანოს თავად რიცხვი. დამატებით დაითვალეთ, რამდენი Fizz, Buzz და FizzBuzz შეგხვდათ მოცემულ დიაპაზონში.

start = int(input("შეიყვანეთ საწყისი რიცხვი: "))
end = int(input("შეიყვანეთ საბოლოო რიცხვი: "))

fizz = 0
buzz = 0
fizzbuzz = 0

for number in range(start, end + 1):

    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
        fizzbuzz += 1

    elif number % 3 == 0:
        print("Fizz")
        fizz += 1

    elif number % 5 == 0:
        print("Buzz")
        buzz += 1

    else:
        print(number)

print("\n====== სტატისტიკა ======")
print("Fizz:", fizz)
print("Buzz:", buzz)
print("FizzBuzz:", fizzbuzz)