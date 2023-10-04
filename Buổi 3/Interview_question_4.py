def is_anagram(word1, word2):
  # Chuẩn hóa hai từ.
  word1 = word1.lower().replace(" ", "").replace("-", "")
  word2 = word2.lower().replace(" ", "").replace("-", "")
  # Tạo hai bộ từ điển để lưu trữ tần suất xuất hiện của các chữ cái trong hai từ.
  word1_dict = {}
  word2_dict = {}
  for char in word1:
    if char not in word1_dict:
      word1_dict[char] = 1
    else:
      word1_dict[char] += 1
  for char in word2:
    if char not in word2_dict:
      word2_dict[char] = 1
    else:
      word2_dict[char] += 1
  # Duyệt qua hai bộ từ điển và so sánh tần suất xuất hiện của các chữ cái.
  if word1_dict == word2_dict:
    return True
  else:
    return False

# Ví dụ sử dụng thuật toán:

word1 = "restful"
word2 = "fluster"

if is_anagram(word1, word2):
  print("Hai từ là anagram.")
else:
  print("Hai từ không phải là anagram.")

