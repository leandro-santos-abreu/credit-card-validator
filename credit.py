def validate_card(cn):
    for i in range(len(cn)):
        if not cn[i].isnumeric():
            return True


def separate_digits(cn):
    odd_digits = []
    pair_digits = []
    size = len(cn)

    for i in range(1, size + 1):
        if i % 2 == 0:
            pair_digits.append(int(cn[-i]) * 2)
        else:
            odd_digits.append(int(cn[-i]))

    return odd_digits, pair_digits


def sum_digits(odd_value, pair_value):
    o_sum = 0
    p_sum = 0

    size_pair = len(pair_value)
    size_odd = len(odd_value)

    for i in range(0, size_pair):
        p_sum = p_sum + ((pair_value[i] // 10) + pair_value[i] % 10)

    for i in range(0, size_odd):
        o_sum = o_sum + ((odd_value[i] // 10) + odd_value[i] % 10)

    return o_sum, p_sum


def define_flag(cn):
    if (cn[0] == "3" and
            (cn[1] == "4" or
             cn[1] == "7")):
        return "American Express"

    elif cn[0] == "4":
        return "VISA"

    elif ((50 < int(cn[0] + cn[1]) < 56) or
          len(cn) == 16):
        return "Mastercard"


if __name__ == '__main__':
    while True:
        cardNumber = input("Número: ")

        if validate_card(cardNumber):
            continue

        odd_values, pair_values = separate_digits(cardNumber)
        odd_sum, pair_sum = sum_digits(odd_values, pair_values)
        total = odd_sum + pair_sum

        if total % 10 == 0:
            flag = define_flag(cardNumber)
            print(flag)
            break
        else:
            print("\nINVÁLIDO")
            break
