message = "Hello my little friends!"#input("Enter a message: ")
offset = 37 #int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
  if ch == " " or ch == "!":
    encoded_message = encoded_message + ch
  elif ch.isupper():
    ch_int = ord(ch) - ord("A")
    new_ch_int = (ch_int + offset) % 26
    new_char = chr(new_ch_int + ord("A"))
    encoded_message = encoded_message + new_char
  else:
    ch_int = ord(ch) - ord("a")
    new_ch_int = (ch_int + offset) % 26
    new_char = chr(new_ch_int + ord("a"))
    encoded_message = encoded_message + new_char
print(encoded_message)
