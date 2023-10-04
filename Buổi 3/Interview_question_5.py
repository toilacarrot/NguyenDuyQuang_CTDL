def find_duplicates(array):

  seen = {}

  duplicates = []
  for element in array:
    if element in seen:
      duplicates.append(element)
    else:
      seen[element] = True

  # Trả về danh sách các phần tử trùng lặp.
  return duplicates


# Ví dụ sử dụng thuật toán:

array = [1, 2, 3, 1, 5]

duplicates = find_duplicates(array)

print(duplicates)

