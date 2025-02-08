def validate_card_number(card_number):
    check_digit = card_number[-1:]
    new_card_number = card_number[:-1]
    sum = 0
    try:
        check_digit = int(card_number[-1:])
        for digit in range(0, len(new_card_number)):
            if digit % 2 == 0:
                sum += int(new_card_number[digit])
            else:
                sum += int(new_card_number[digit]) * 2 - 9
    except:
        print("input was not able to be parsed")

    parity = (10 - (sum % 10)) % 10
    sum += check_digit
    if check_digit == parity and sum % 10 == 0:
        return True
    else:
        return False

target_card_number = "17893729974"

print(validate_card_number(target_card_number))