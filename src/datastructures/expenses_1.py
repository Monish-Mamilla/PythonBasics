


def total_expense(expenses) :

    total =0
    for expense in expenses :
         total += expense
    
    return total

def print_total_expenses() :
    expenses_sergey = [30,45,70,90]
    expenses_sundar =  [40,23,10,85]

    total_expense_sergey = total_expense(expenses_sergey)
    total_enpense_sundar = total_expense(expenses_sundar)

    print(f"Total Expense of Sergey : { total_expense_sergey}")
    print(f"Total Expense of Sundar : {total_enpense_sundar}")

if __name__ == "__main__" :

    print("Main function called")

    print_total_expenses()