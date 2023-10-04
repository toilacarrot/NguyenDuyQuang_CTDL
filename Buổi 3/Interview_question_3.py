def reverse_integer(integer):

  string = str(integer)

  reversed_string = string[::-1]
  reversed_integer = int(reversed_string)

  return reversed_integer



integer = 1234
reversed_integer = reverse_integer(integer)

print(reversed_integer)
