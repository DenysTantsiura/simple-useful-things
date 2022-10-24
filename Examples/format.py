grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    cx = 1
    Stud_list = []
    for v_name, v_rate in students.items():
        Stud_list.append("{0:>4}|{1:<10}|{2:^5}|{3:^5}".format(
            cx, v_name, v_rate, grades.get(v_rate)))
        cx += 1
    return Stud_list


print(formatted_grades({"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}))


#-------------------------------
def formatted_numbers():
    """повертає список відформатованих рядків"""
    list_dz_5_9 = []
    list_dz_5_9.append("|{0:^10}|{1:^10}|{2:^10}|".format(
        "decimal", "hex", "binary"))
    for i in range(16):
        list_dz_5_9.append(
            "|{0:<10}|{1:^10}|{2:>10}|".format(i, "{:x}".format(i), "{:b}".format(i)))
    return list_dz_5_9


# print(formatted_numbers())
for el in formatted_numbers():
    print(el)
