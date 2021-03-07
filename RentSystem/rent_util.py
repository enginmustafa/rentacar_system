def is_value_in_list(list_values, value) -> bool:
    for val in list_values:
        if val == value:
            return True

    return False


def are_values_in_list(list_values, values) -> bool:
    try:
        for val in values:
            in_list = False
            for value in list_values:
                if value == val:
                    in_list = True

            if not in_list:
                return False

        return True
    # Object not iterable
    except TypeError:
        return False








