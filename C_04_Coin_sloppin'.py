for item in range(1, 13):
    num_gold_choc_coin = 12
    num_students = item

    division = num_gold_choc_coin / num_students
    per_student = num_gold_choc_coin // num_students
    gold_choc_coin_left = num_gold_choc_coin % num_students

    if gold_choc_coin_left == 0:
        print(f"{item} is a factor of 12! (yippie) ")

    print(f"Each students gets {per_student} and we have {gold_choc_coin_left} left over ")