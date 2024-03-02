from app.queries.my_select  import select_1, select_2, select_3, select_4, select_5, select_6, select_7, select_8, select_9, select_10

def main():
    while True:
        print("\nВиберіть опцію:")
        print("1: Знайти 5 студентів із найбільшим середнім балом з усіх предметів")
        print("2: Знайти студента із найвищим середнім балом з певного предмета")
        print("3: Знайти середній бал у групах з певного предмета")
        print("4: Знайти середній бал на потоці")
        print("5: Знайти які курси читає певний викладач")
        print("6: Знайти список студентів у певній групі")
        print("7: Знайти оцінки студентів у окремій групі з певного предмета")
        print("8: Знайти середній бал, який ставить певний викладач")
        print("9: Знайти список курсів, які відвідує певний студент")
        print("10: Список курсів, які певному студенту читає певний викладач")
        print("0: Вийти")

        choice = input("Ваш вибір: ")

        if choice == '1':
            print(select_1())
        elif choice == '2':
            print(select_2())
        elif choice == '3':
            print(select_3())
        elif choice == '4':
            print(select_4())
        elif choice == '5':
            print(select_5())
        elif choice == '6':
            print(select_6())
        elif choice == '7':
            print(select_7())
        elif choice == '8':
            print(select_8())
        elif choice == '9':
            print(select_9())
        elif choice == '10':
            print(select_10())
        elif choice == '0':
            break
        else:
            print("Неправильний вибір, будь ласка, спробуйте знову.")

if __name__ == "__main__":
    main()
