#მომხმარებელს შემოაყვანინეთ პროდუქტის სახელი, ფასი და რაოდენობა. გამოთვალეთ სრული ღირებულება და დაბეჭდეთ ყველა მონაცემი. (სტული ფასი = ფასი * რაოდენობაზე)

product_name = input("Enter product name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter product quantity: "))

total_price = price * quantity

print("Product name:", product_name)
print("Price:", price)
print("Quantity:", quantity)
print("Total price:", total_price)

#სრული ღირებულება გამოითვლება ფორმულით:
#\[
#\text{სრული ფასი}=\text{ფასი}\times\text{რაოდენობა}
#\]

#მაგალითად, თუ პროდუქტის ფასი არის 5 ლარი და რაოდენობა 3:
#\[
#5 \times 3 = 15
#\]

#სრული ღირებულება იქნება 15 ლარი.