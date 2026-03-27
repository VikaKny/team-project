contacts = []

while True:
    print("\n1 - Додати контакт")
    print("2 - Показати контакти")
    print("3 - Видалити контакт")
    print("4 - Вихід")

    choice = input("Виберіть дію: ")


    if choice == "1":
        name = input("Введіть ПІБ: ")
        number = input("Введіть номер телефону: ")

        contact = {
            "name": name,
            "phone": number
        }

        contacts.append(contact)
        print("Контакт додано")


    elif choice == "2":
        print("\nСписок контактів:")

        if len(contacts) == 0:
            print("Контактів немає")
        else:
            for i, c in enumerate(contacts, 1):
                print(f"{i} - {c['name']} : {c['phone']}")


    elif choice == "3":
        if len(contacts) == 0:
            print("Немає що видаляти")
        else:
            print("\nСписок контактів:")
            for i, c in enumerate(contacts, 1):
                print(f"{i} - {c['name']} : {c['phone']}")

            try:
                index = int(input("Введіть номер контакту для видалення: ")) - 1

                if 0 <= index < len(contacts):
                    deleted = contacts.pop(index)
                    print(f"Видалено: {deleted['name']}")
                else:
                    print("Невірний номер")

            except ValueError:
                print("Введіть число!")


    elif choice == "4":
        print("Програма завершена")
        break


    else:
        print("Невірний вибір")