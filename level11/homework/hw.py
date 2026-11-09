# საწყისი მონაცემები

total_income = 0
completed_trips = 0
cancelled_trips = 0
total_distance = 0

trip_history = []


# მთავარი მენიუ

while True:

    print("\n======= TAXI SYSTEM =======")
    print("1. მგზავრობის შეკვეთა")
    print("2. შემოსავლის ნახვა")
    print("3. მგზავრობების სტატისტიკა")
    print("4. გასვლა")
    print("===========================")

    choice = input("აირჩიეთ მოქმედება: ")

    # 1. მგზავრობის შეკვეთა

    if choice == "1":

        # მანძილის შემოწმება

        distance = float(input("შეიყვანეთ მანძილი (კმ): "))

        while distance <= 0:
            print("მანძილი უნდა იყოს დადებითი!")
            distance = float(input("შეიყვანეთ მანძილი თავიდან: "))

        # მგზავრების რაოდენობის შემოწმება

        passengers = int(input("მგზავრების რაოდენობა (1-4): "))

        while passengers < 1 or passengers > 4:
            print("მგზავრების რაოდენობა უნდა იყოს 1-დან 4-მდე!")
            passengers = int(input("შეიყვანეთ რაოდენობა თავიდან: "))

        # ღამის მგზავრობის შემოწმება

        night = input("ღამის მგზავრობა? (yes/no): ").lower()

        while night != "yes" and night != "no":
            print("შეიყვანეთ მხოლოდ yes ან no!")
            night = input("ღამის მგზავრობა? (yes/no): ").lower()

        # საფასურის გამოთვლა

        base_price = 2.50
        distance_price = distance * 0.70

        subtotal = base_price + distance_price

        passenger_extra = 0

        if passengers >= 3:
            passenger_extra = 3.00

        subtotal += passenger_extra

        night_extra = 0

        if night == "yes":
            night_extra = subtotal * 0.20

        final_price = subtotal + night_extra

        # მგზავრობის დეტალები

        print("\n====== მგზავრობის დეტალები ======")

        print("მანძილი:", distance, "კმ")
        print("მგზავრები:", passengers)
        print("ღამის მგზავრობა:", night)
        print("საბაზისო საფასური:", base_price, "ლარი")
        print("მანძილის ღირებულება:", distance_price, "ლარი")
        print("მგზავრების დანამატი:", passenger_extra, "ლარი")
        print("ღამის დანამატი:", round(night_extra, 2), "ლარი")
        print("საბოლოო საფასური:", round(final_price, 2), "ლარი")

        print("=================================")

        # მგზავრობის დადასტურება

        confirmation = input("დაადასტურებთ მგზავრობას? (yes/no): ").lower()

        while confirmation != "yes" and confirmation != "no":

            print("არასწორი პასუხი!")
            confirmation = input("დაადასტურებთ მგზავრობას? (yes/no): ").lower()

        if confirmation == "yes":

            total_income += final_price
            completed_trips += 1
            total_distance += distance

            trip_history.append(final_price)

            print("მგზავრობა წარმატებით დასრულდა!")

        else:

            cancelled_trips += 1

            print("მგზავრობა გაუქმებულია!")

    # 2. მძღოლის შემოსავალი

    elif choice == "2":

        print("\n====== მძღოლის შემოსავალი ======")

        print("მთლიანი შემოსავალი:", round(total_income, 2), "ლარი")
        print("დასრულებული მგზავრობები:", completed_trips)

        if completed_trips > 0:

            average_price = total_income / completed_trips

            print("საშუალო საფასური:", round(average_price, 2), "ლარი")

        else:

            print("ჯერ დასრულებული მგზავრობა არ არსებობს.")

        print("================================")

    # 3. მგზავრობების სტატისტიკა

    elif choice == "3":

        print("\n====== მგზავრობების სტატისტიკა ======")

        print("დასრულებული მგზავრობები:", completed_trips)
        print("გაუქმებული მგზავრობები:", cancelled_trips)
        print("საერთო გავლილი მანძილი:", round(total_distance, 2), "კმ")
        print("მძღოლის მთლიანი შემოსავალი:", round(total_income, 2), "ლარი")

        if completed_trips > 0:

            average_price = total_income / completed_trips

            print("საშუალო საფასური:", round(average_price, 2), "ლარი")

            # ყველაზე ძვირი და იაფი მგზავრობა

            expensive_trip = trip_history[0]
            cheapest_trip = trip_history[0]

            over_20 = 0

            for price in trip_history:

                if price > expensive_trip:
                    expensive_trip = price

                if price < cheapest_trip:
                    cheapest_trip = price

                if price > 20:
                    over_20 += 1

            print("ყველაზე ძვირი მგზავრობა:", round(expensive_trip, 2), "ლარი")
            print("ყველაზე იაფი მგზავრობა:", round(cheapest_trip, 2), "ლარი")
            print("20 ლარზე მეტი ღირებულების მგზავრობები:", over_20)

            # მგზავრობების ისტორია

            print("\n====== მგზავრობების ისტორია ======")

            trip_number = 0

            for price in trip_history:

                trip_number += 1

                print("მგზავრობა №" + str(trip_number) + ": " +
                      str(round(price, 2)) + " ლარი")

            print("==================================")

        else:

            print("ჯერ დასრულებული მგზავრობები არ არსებობს.")

        print("====================================")

    # 4. სისტემიდან გასვლა

    elif choice == "4":

        print("\nსისტემიდან გასვლა...")
        print("დასრულებული მგზავრობები:", completed_trips)
        print("გაუქმებული მგზავრობები:", cancelled_trips)
        print("მთლიანი შემოსავალი:", round(total_income, 2), "ლარი")
        print("გმადლობთ სარგებლობისთვის!")

        break

    # არასწორი არჩევანი

    else:

        print("არასწორი არჩევანი! აირჩიეთ 1-დან 4-მდე.")