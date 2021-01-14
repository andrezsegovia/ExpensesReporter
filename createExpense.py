from expense import Expense

def read():

    print("Insert the expense's name:")
    name = input()

    print("Insert the expense's category")
    category = input()

    print("Insert the expense's value")
    value = int(input())

    print("Insert the expense's date")
    date = int(input())

    return Expense(name, category, value, date)