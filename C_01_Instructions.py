# Generates headings (eg:---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Display function here
def instructions():
    statement_generator("Instructions","-")

    print('''
To use the progress, you simply need to type in a number that is equal or more than 1 to less or equal 200
the program will also show the numbers' factor based on your chosen integer

The program will also say if your chosen number is a prime number, or a perfect square :)
- Is a prime number
- Or if it's a perfect square
''')

# The Main Routine goes here

# Display instruction if the user commanded so
want_instructions = input("Press <Enter> to see instruction or type anything then press <Enter> to Run with no Instructions ")


if want_instructions == "":
    instructions()

print()
print(" Alrighty, let's proceed")
