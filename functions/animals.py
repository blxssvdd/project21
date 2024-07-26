def show_anim(animals: list) -> None:
    delimeter = "-" * 28
    template = "|{:<5}|{:<20}|"
    print(delimeter)
    print(template.format("№", "Ім'я тваринки"))
    print(delimeter)
    for i, animal in enumerate(animals, start=1):
        print(template.format(i, animal))
    print(delimeter)


def add_anim(animal: list) -> list:
    animals = input("Введіть нову тваринку для додавання на лікування: ")

    if animal not in animals:
        animals.append(animal)
        print(f"\nТваринка '{animal}' додана до списку")
    else:
        print("\nТака тваринка вже є у списку")

    return animals


def add_anim(animals: list) -> list:
    anim = input("Введіть список тварин для додавання через пробіл\n-> ")
    anim = anim.split()
    animals.extend(anim)
    print("\nСписок тваринок розширено")
    return animals


def del_anim_by_name(animals: list) -> list:
    animal = input("Введіть ім'я тваринки для видалення зі списку товарів: ")

    if animal in animals:
        animals.remove(animal)
        print(f"\nТваринку '{animal}' видалено зі списку")
    else:
        print("\nТакої тваринки немає у списку")

    return animals


def del_anim_by_num(animals: list[str]) -> list[str]:
    index = input("Введіть номер тваринки для видалення: ")

    if index and index.isdigit() and 0 < int(index) <= len(animals):
        animal = animals.pop(int(index) - 1)
        print(f"Тваринку '{animal}' видалено ")
    else:
        print("Ви ввели не вірний номер тваринки")

    return animals


def sort(animals: list) -> None:
    print()
    anim = sorted(animals)
    for animal in anim:
        print(animal)


def sold_anim(animals: list[str], animals_sold: list[str]) -> tuple:
    animal = input("Введіть ім'я тваринки для вилікування: ")

    if animal in animals:
        animals.remove(animal)
        animals_sold.append(animal)
        print(f"\nТваринку '{animal}' вилікувано")
    else:
        print("\nТакої тваринки немає у списку")

    return animals, animals_sold


def find_anim_by_name(animals: list) -> None:
    animal = input("Введіть ім'я тваринки для пошуку: ")

    if animal in animals:
        index = animals.index(animal)
        print(f"Тваринка '{animal}' знаходиться під номером {index + 1}")
    else:
        print("\nТакої тваринки немає у списку")


def show_history(animals_sold: list) -> None:
    anim_sold = animals_sold[::-1]
    for animal in anim_sold:
        print(animal)


def palindrome(animals: list) -> None:
    palin_anim = [animal for animal in animals if animal.lower() == animal[::-1].lower()]
    print(f"\nУ списку з  є такі слова-паліндроми: {palin_anim}\n")
