def sort_dict(dict_in: dict) -> dict:
    """Sort the dictionary by decreasing values."""
    dict_out = {}
    while dict_in:
        max_vlist = max(set(dict_in.values()))
        for key, val in dict_in.items():
            if val == max_vlist:
                dict_out[key] = dict_in.pop(key)
                break
    return dict_out


print(sort_dict({"objdtr": 8, 1: 11, "6": 4, 3: 11, }))


#====тест! на швидкість! після генерації словника рандомнозначень на 2к елем?====
grades = {"objdtr": 8, 1: 11, "6": 4, 3: 11, }
value_key_pairs = ((value, key) for (key,value) in grades.items())
sorted_value_key_pairs = sorted(value_key_pairs, reverse=True)
print({k: v for v, k in sorted_value_key_pairs})
