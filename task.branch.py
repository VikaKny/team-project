contacts = []

while True:
    print("\n1 - Додати контакт")
    print("2 - Показати контакти")
    print("3 - Вихід")

    choice = input("Виберіть дію: ")

    if choice == "1":
        number = input("Введіть номер телефону: ")
        contacts.append(number)
        print("Контакт додано")

    elif choice == "2":
        print("\nСписок контактів:")
        if len(contacts) == 0:
            print("Контактів немає")
        else:
            for i, c in enumerate(contacts, 1):
                print(i, "-", c)

    elif choice == "3":
        print("Програма завершена")
        break

    else:
        print("Невірний вибір")