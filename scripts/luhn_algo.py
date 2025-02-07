def validate_card_number(card_number):
    even_index_digits = []
    odd_index_digits = []
    try:
        for digit in range(0, len(card_number)):
            if digit % 2 == 0:
                even_index_digits.append(int(card_number[digit]))
            else:
                odd_index_digits.append(int(card_number[digit]) * 2)
    except:
        print("input was not able to be parsed")
    return (even_index_digits, odd_index_digits)

target_card_number = "17893729974"

print(validate_card_number(target_card_number))