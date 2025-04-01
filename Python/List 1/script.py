import os

PI = 3.14


def firstQuestion():
    try:
        degrees = float(input("Enter an angle in degrees: "))
        radians = degrees * (PI / 180)
        print(f"\n{degrees} degrees is equal to {radians:.2f} radians.\n")
    except ValueError:
        print("Please, enter a valid degree value.")


def secondQuestion():
    try:
        product_value = abs(float(input("Enter a product value: ")))
        product_discount = abs(float(input("Enter a discount value (%): "))) / 100
        discounted_value = product_value * (1 - product_discount)
        print(f"\nProduct value with discount: R$ {discounted_value:.2f}\n")
    except ValueError:
        print("Please, enter a valid value.")


def thirdQuestion():
    try:
        first_triangle_side = float(input("Enter the first triangle side value: "))
        second_triangle_side = float(input("Enter the second triangle side value: "))
        third_triangle_side = float(input("Enter the third triangle side value: "))

        semiperimeter = (
            first_triangle_side + second_triangle_side + third_triangle_side
        ) / 2

        area = (
            semiperimeter
            * (semiperimeter - first_triangle_side)
            * (semiperimeter - second_triangle_side)
            * (semiperimeter - third_triangle_side)
        ) ** 0.5

        print(f"\nTriangle area: {area:.2f}\n")
    except ValueError:
        print("Please, enter a valid value.")


def fourthQuestion():
    try:
        initial_value = float(input("Enter the initial value: "))
        interest_rate = float(input("Enter the interest rate (%): ")) / 100
        months_quantity = int(input("Enter the number of months: "))

        future_value = initial_value * (1 + (interest_rate * months_quantity))

        print(f"\n Future value: {future_value} \n")

    except ValueError:
        print("Please, enter a valid value.")


def fifthQuestion():
    try:
        total_sales = float(input("Enter the total sales value: "))
        commission_percentage = float(input("Enter the commission (%): ")) / 100
        total_commission = total_sales * commission_percentage

        print(f"\nTotal Commission value: R$ {total_commission:.2f}\n")

    except ValueError:
        print("Please, enter a valid value.")


def sixthQuestion():
    try:
        circle_radius = float(input("Enter the radius of the circle: "))
        circle_area = PI * (circle_radius**2)

        print(f"\nCircle Area: {circle_area:.2f}\n")

    except ValueError:
        print("Please, enter a valid value.")


def seventhQuestion():
    try:
        product_cost = float(input("Enter the product cost: "))
        product_selling_price = float(input("Enter the product selling price: "))

        gross_profit = product_selling_price - product_cost

        print(f"\nGross Profit: R$ {gross_profit:.2f}\n")

    except ValueError:
        print("Please, enter a valid value.")


def eighthQuestion():
    try:
        celsius_value = float(input("Enter the temperature in celsius: "))
        fahrenheit_value = ((9 / 5) * celsius_value) + 32

        print(f"\n Fahrenheit Value: {fahrenheit_value} \n")

    except ValueError:
        print("Please, enter a valid value.")


def ninthQuestion():
    try:
        product_value = float(input("Enter the product value: "))
        tax_rate = float(input("Enter the tax rate (%): ")) / 100

        final_value_with_tax = product_value * (1 + tax_rate)

        print(f"\n Final value with tax: {final_value_with_tax:.2f} \n")

    except ValueError:
        print("Please, enter a valid value.")


def tenthQuestion():
    try:
        total_purchase_value = float(input("Enter the total purchase value: "))
        installments_quantity = int(input("Enter the number of installments: "))

        if installments_quantity <= 0:
            print("\nNumber of installments must be greater than zero.\n")
            return

        value_per_installment = total_purchase_value / installments_quantity
        print(f"\n Value per Installment: R$ {value_per_installment:.2f} \n")

    except ValueError:
        print("Please, enter a valid value.")


def clearScreen():
    system = os.name
    if system == "posix":  # Linux/macOS
        os.system("clear")
    elif system == "nt":  # Windows
        os.system("cls")


def getMenuOption(is_exit_option=False):
    menu = ""

    if is_exit_option:
        menu = """
        ======= Menu Options =======
        1 - I'm tired, I don't want to test anymore, close!
        2 - Explore other options
        """
    else:
        menu = """
        ======= Menu Options =======
        1 - Degrees to Radians Converter
        2 - Discount Calculator
        3 - Triangle Area
        4 - Interest Calculator
        5 - Commission Calculator
        6 - Circle Area
        7 - Product Gross Profit
        8 - Convert from Celsius to Fahrenheit
        9 - Tax Calculator
        10 - Purchase Installment Calculator
        11 - Exit
        """

    print(menu)

    while True:
        try:
            option = int(input("Choose an option: "))
            return option
        except ValueError:
            print("Invalid option! Please enter a valid number.")


def main():
    questions = {
        1: firstQuestion,
        2: secondQuestion,
        3: thirdQuestion,
        4: fourthQuestion,
        5: fifthQuestion,
        6: sixthQuestion,
        7: seventhQuestion,
        8: eighthQuestion,
        9: ninthQuestion,
        10: tenthQuestion,
    }

    is_exit_option = False
    while True:
        menu_option = getMenuOption(is_exit_option)
        clearScreen()

        if is_exit_option:
            if menu_option == 1:
                print("Bye Bye...")
                exit()
            else:
                is_exit_option = False
        else:
            if menu_option in questions:
                questions[menu_option]()
                is_exit_option = True
            elif menu_option == 11:
                print("Bye Bye...")
                exit()
            else:
                print("Option not found. Try again.")
                input("Press Enter to continue...")


main()
