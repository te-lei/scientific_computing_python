
def arithmetic_arranger(list, calculate= False):
    number_1 = []
    signs = []
    number_2 = []

    s = " "
    num_spaces_1 = []
    num_spaces_2 = []
    dashes = []
    d = "-"
    sums = []

    def calc():
        if sign == "+":
            sum_plus = int(num_1) + int(num_2)
            sum_length = len(str(sum_plus))
            sum_space = most - sum_length
            sum_plus1 = (2 + sum_space) * s + str(sum_plus)
            sums.append(sum_plus1)
        elif sign == "-":
            sum_minus = int(num_1) - int(num_2)
            summ_length = len(str(sum_minus))
            summ_space = most - summ_length
            sum_minus1 = (2 + summ_space) * s + str(sum_minus)
            sums.append(sum_minus1)
        else:
            print("Error: Operator must be '+' or '-'.")
            exit()

    list_length = len(list)

    if list_length <= 5:

        for i in list:
            clean = i.split()

            num_1 = clean[0]
            # print(num_1)
            x = len(num_1)

            try:
                int(num_1)
            except:
                print("Error: Numbers must only contain digits.")
                exit()

            if x <= 4:
                None
            else:
                print("Error: Numbers cannot be more than four digits.")
                exit()

            number_1.append(int(num_1))
            sign = clean[1]
            # print(sign)
            signs.append(sign)



            num_2 = clean[2]
            # print(num_2)
            y = len(num_2)

            if y <= 4:
                None
            else:
                print("Error: Numbers cannot be more than four digits.")
                exit()
            try:
                int(num_2)
            except:
                print("Error: Numbers must only contain digits.")
                exit()

            number_2.append(int(num_2))

            chars = x, y
            most = max(chars)
            # print(most, 'is the most chars')

            space = most + 2
            z = space * d
            dashes.append(z)
            p = most - x
            q = most - y
            space_before_1 = 2*s + p * s + num_1
            num_spaces_1.append(space_before_1)
            space_before_2 = sign + s + q * s + num_2
            num_spaces_2.append(space_before_2)

            if calculate is True:
                calc()
            else:
                None

        for sign in signs:
            if sign == "+" or "-":
                None
            else:
                print("Error: Operator must be '+' or '-'.")
                exit()

        aa = print("    ".join(str(x) for x in num_spaces_1))
        aaa = print("    ".join(str(x) for x in num_spaces_2))
        aaaa = print("    ".join(str(x) for x in dashes))

    else:
        print("Error: Too many problems.")

    if calculate:
        aaaaa = print("    ".join(str(x) for x in sums))
        return aa, aaa, aaaa,aaaaa
    else:
        return aa, aaa, aaaa
