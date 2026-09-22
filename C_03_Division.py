while True:
    num_chocolate_gold_coin = int(input("How many Chocolate gold coins? "))
    num_students = int(input("How many students? "))

    division = num_chocolate_gold_coin / num_students
    per_student = num_chocolate_gold_coin // num_students
    golden_choc_coin_left = num_chocolate_gold_coin % num_students

    print("Division: ", division)
    print("Chocolate gold coins per student: ", per_student)
    print("Chocolate gold coins left: ", golden_choc_coin_left)