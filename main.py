def sanitize_phone_number(phone):
    return phone.strip().replace("-", "").replace("(", "").replace(")", "").replace("+", "").replace(" ", "")
        

print(sanitize_phone_number("    +38(050)123-32-34"))
print(sanitize_phone_number("     0503451234"))
print(sanitize_phone_number("(050)8889900"))
print(sanitize_phone_number("38050-111-22-22"))
print(sanitize_phone_number("38050 111 22 11   "))