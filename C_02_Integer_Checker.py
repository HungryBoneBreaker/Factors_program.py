# Ask the user for a number and make sure it has no decimals, is more or equal to 1 and less or equal to 200
def int_check(question, low, high):
    low_error = f"Please enter a number that is more or equal to {low}\n"
    high_error = f"Please enter a number that is less or equal to {high}\n"
    while True:

        try:
            # ask the human for a number
            response = int(input(question))

            # check that the number is more than or equal to 1 and is less or equal to 200
            if response >= low:
                return response
            else:
                print(low_error)
                print("and make sure the integer has no decimals!")

            if response <= high:
                return response
            else:
                print(high_error)
                print("and make sure the integer has no decimals!")

        except ValueError:
            print("Please make sure the integer is valid"
                  "e.g no decimals, equal or more than 1 and equal or less than 200")

# Main routine goes here
integer = int_check("Integer:", 1, 200)
print(f"Your integer is {integer}\n")

if int_check = 