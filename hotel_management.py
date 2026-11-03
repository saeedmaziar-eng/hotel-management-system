Rooms = [
    {"title": "101", "count": 2, "price": 1500000},
    {"title": "102", "count": 3, "price": 2000000},
    {"title": "103", "count": 1, "price": 1000000}
]
while True:
    print("Hotel Management System")
    print("1 -> Show Rooms")
    print("2 -> Add Room")
    print("3 -> Remove Room")
    print("4 -> Update Room")
    print("5 -> Reserve Room")
    print("6 -> Cancel Reservation")
    print("7 -> Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        for room in Rooms:
            print(f"{room['title']} -> {room['count']} -> {room['price']}")

    elif choice == 2:
        found = False
        new_room = input("Enter new room name: ")
        for room in Rooms:

            if room["title"]== new_room:
                found = True
                break
        if found:
            print("Room already exists")
        else:
            new_count = int(input("Enter new room count: "))
            new_price = int(input("Enter new room price: "))
            Rooms.append({"title": new_room, "count": new_count, "price": new_price})
            print("Room added")
            print(Rooms)

    elif choice == 3:
        new_title = input("Enter new room name: ")
        found = False
        for room in Rooms:
            if room["title"] == new_title:
                found = True
                break
        if found:
            Rooms.remove(room)
            print("Room deleted")
            print(Rooms)
        else:
            print("Room does not exist")

    elif choice == 4:
        new_title = input("Enter new room title: ")
        found = False
        for room in Rooms:
            if room["title"] == new_title:
                found = True
                break
        if found:
            new_price = int(input("Enter new room price: "))
            room["price"] = new_price
            print("price updated")
            print(Rooms)
        else:
            print("Room does not exist")

    elif choice == 5:
        new_title = input("Enter new room title: ")
        found = False
        for room in Rooms:
            if room["title"] == new_title:
                found = True
                break
        if found:
            if room["count"] <= 0:
                print("No rooms available")
            else:
                room["count"] -= 1
                print("Room reserved successfully")
                print(Rooms)
        else:
            print("Room does not exist")

    elif choice == 6:
        new_title = input("Enter new room title: ")
        found = False
        for room in Rooms:
            if room["title"] == new_title:
                found = True
                break
        if found:
                room["count"] += 1
                print("Reserved cancelled successfully")
                print(Rooms)
        else:
            print("Room does not exist")

    elif choice == 7:
        print("Exit")
        break
    else:
        print("Invalid choice")


