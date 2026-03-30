contacts = {}

while True:
    print("\n1 - Додати контакт")
    print("2 - Показати контакти")
    print("3 - Видалити контакт")
    print("4 - Вихід")

    choice = input("Виберіть дію: ").strip()

    if choice == "1":
        name = input("Введіть ПІБ: ").strip()
        number = input("Введіть номер телефону: ").strip()

        if name == "" or number == "":
            print("Поля не можуть бути порожніми!")
            continue

        contacts[name] = number
        print("Контакт додано")

    elif choice == "2":
        print("\nСписок контактів:")

        if not contacts:
            print("Контактів немає")
        else:
            i = 1
            for name, phone in contacts.items():
                print(f"{i}. {name} : {phone}")
                i += 1

    elif choice == "3":
        if not contacts:
            print("Немає що видаляти")
        else:
            print("\nСписок контактів:")
            names = list(contacts.keys())

            for i, name in enumerate(names, 1):
                print(f"{i}. {name} : {contacts[name]}")

            try:
                index = int(input("Введіть номер контакту для видалення: ")) - 1

                if 0 <= index < len(names):
                    deleted_name = names[index]
                    del contacts[deleted_name]
                    print(f"Видалено: {deleted_name}")
                else:
                    print("Невірний номер")

            except ValueError:
                print("Введіть число!")

    elif choice == "4":
        print("Програма завершена")
        break

    else:
        print("Невірний вибір")
