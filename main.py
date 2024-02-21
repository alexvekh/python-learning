# Напишіть функцію to_indexed(source_file, output_file), яка зчитуватиме вміст файлу, 
# додаватиме до прочитаних рядків порядковий номер і зберігати їх у такому вигляді у новому файлі.
# Кожний рядок у створеному файлі повинен починатися з його номера, двокрапки та пробілу, 
# після чого має йти текст рядка з вхідного файлу.
# Нумерація рядків іде від 0.

def to_indexed(source_file, output_file):
    with open(source_file, 'r') as source:
        with open(output_file, 'w') as output:
            count = 0
            for line in source:
                output.write(str(count) + ": " + line)
                count += 1




def get_employees_by_profession(path, profession):
    with open(path, 'r') as file:
        lines = file.readlines()
    #print(lines)
    
    pro_list = []
    for line in lines:
        if line.find(profession) >= 0:
            line = line.replace(' courier\n', '')
            pro_list.append(line)
    #print(pro_list)

    names = ' '.join(pro_list)
    return names

# get_employees_by_profession('data.txt', 'courier')







