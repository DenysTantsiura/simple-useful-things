# print(help(dict))
# help(dict)

base_list = [-1, 0, 1, 2, 3]


def check_list_increase0(base_list: list) -> list:
    if len(base_list) > 1:
        for num_el in range(1, len(base_list)):
            if base_list[num_el-1] + 1 != base_list[num_el]:
                return False
    return True


def check_list_increase1(base_list: list) -> list:
    if len(base_list) > 1:
        return all([el-1 == base_list[idx] for idx, el in enumerate(base_list[1:])])
    return True

    # return all(list(filter(lambda el>: el, base_list)))
print(check_list_increase1(base_list))
print(check_list_increase1([-1, 0, 1, 2, 4]))
print(check_list_increase1([-2, 0, 1, 2, 3]))
print(check_list_increase1([0, 1]))
print(check_list_increase1([1]))


def check_list_increase1(base_list: list) -> list:
    return all([el-1 == base_list[idx] for idx, el in enumerate(base_list[1:])]) if len(base_list) > 1 else True

print(check_list_increase1(base_list))
print(check_list_increase1([-1, 0, 1, 2, 4]))
print(check_list_increase1([-2, 0, 1, 2, 3]))
print(check_list_increase1([0, 1]))
print(check_list_increase1([1]))
