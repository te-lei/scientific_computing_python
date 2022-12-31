# Arithmetic Formatter

#### This is my submission for the Arithmetic Formatter project. 

#### Instructions for building your project can be found at https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter

### Code begins:

#### Define function, set required argument of list and an optional argument to calculate the numbers (automatically set to false).
#### Create lists for the operands in the equation (number_1 & number_2) and the signs (+ or -).

    def arithmetic_arranger(list, calculate= False):
      number_1 = []
      signs = []
      number_2 = []

#### Create lists for the amount of empty spaces to include before each number in order for them to be right aligned and visually correct.
#### Create a list of dashes to denote the line separating the operands and the sum/difference.

      s = " "
      num_spaces_1 = []
      num_spaces_2 = []
      dashes = []
      d = "-"

#### Create a list for the sums/differences for each pair of operands.

      sums = []

#### Define calculation function which adds opperands (num_1 and num_2) if the sign is "+" and subtracts operands if the sign is "-". Present an error if the sign is anything other than "+" or "-" and exit the function.

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

#### Create a limit of 5 expressions to be calculated by checking if the list argument has 5 or less items. 

      list_length = len(list)

      if list_length <= 5:

#### Parse the list to identify num_1, num_2, and the sign. Print errors and exit the code if the numbers entered exceed 4 digits. Populate lists for number_1, number_2, and signs with their respective values.

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

#### Determine the amount of spaces required for each operand to properly align the equations. Populate lists for spaces with these values.

#### Calculate the amount of dashes to be two more than the length of the largest number in the equation. 

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

#### Calculate the sum or difference if calculate argument is set to True.

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

#### Reject any entries that exceed 5 expressions.

      else:
          print("Error: Too many problems.")

#### Return expressions with or without sums depending on whether calculate argument is set to True.

      if calculate:
          aaaaa = print("    ".join(str(x) for x in sums))
          return aa, aaa, aaaa,aaaaa
      else:
          return aa, aaa, aaaa
