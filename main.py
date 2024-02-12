grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

def formatted_grades(students):
    formatted_students = []
    count = 1 
    for key, value in students.items():
        #print('{:>4}|{:<10}|{:^5}|{:^5}'.format(count, key, value, grades[value]))
        #print(f'{count:>4}|{key:<10}|{value:^5}|{grades[value]:^5}')
        formatted_students.append('{:>4}|{:<10}|{:^5}|{:^5}'.format(count, key, value, grades[value]))
        count += 1
    return formatted_students

# students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
# for el in formatted_grades(students):
#     print(el)
