def add_employee_to_file(record, path):
    f = open(path, "a")
    try:
        f.write(record + "\n")   

    finally:
        f.close()

# add_employee_to_file("Boss Boss, 19", "data.txt")