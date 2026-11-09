#შექმენით პროგრამა, რომელიც მომხმარებელს შეაყვანინებს:

#სახელს
#გვარს
#ასაკს
#საყვარელ ფერს

#ყველა ინფორმაცია შეინახეთ შესაბამის ცვლადებში და გამოიტანეთ #ტერმინალში შემდეგი ფორმით:
#User full name: Saba Dzidzikashvili
#User age: 17
#Favorite color: red

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
favorite_color = input("Enter your favorite color: ")

print(f"User full name: {first_name} {last_name}")
print(f"User age: {age}")
print(f"Favorite color: {favorite_color}")

#როგორ მუშაობს?
#1. input() მომხმარებელს სთხოვს ინფორმაციის შეყვანას.
#2. შეყვანილი ინფორმაცია ინახება შესაბამის ცვლადში.
#3. print() ინფორმაციას ტერმინალში გამოიტანს.
#4. f"..." საშუალებას გვაძლევს, ტექსტში ცვლადების მნიშვნელობები ჩავსვათ.