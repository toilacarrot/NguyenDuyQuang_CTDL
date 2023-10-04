def is_palindrome(string):  
  # Chuẩn hóa chuỗi.
  string = string.lower().replace(" ", "").replace("-", "")
  # Tạo một biến để theo dõi vị trí của ký tự hiện tại trong chuỗi.
  i = 0
  # Duyệt qua tất cả các ký tự của chuỗi.
  while i < len(string) // 2:
    # So sánh ký tự hiện tại với ký tự cuối cùng của chuỗi.
    if string[i] != string[len(string) - i - 1]:
      # Chuỗi không phải là chuỗi đối xứng.
      return False
    # Tăng biến i lên 1 để theo dõi ký tự tiếp theo trong chuỗi.
    i += 1
  # Nếu tất cả các ký tự trong chuỗi đều bằng nhau, thì chuỗi là chuỗi đối xứng.
  return True
string = "madam"

if is_palindrome(string):
  print("Chuỗi là chuỗi đối xứng.")
else:
  print("Chuỗi không phải là chuỗi đối xứng.")

