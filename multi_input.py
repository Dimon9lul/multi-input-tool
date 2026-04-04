def json_form(target: list[dict]):
    out = "[REPLACE\n]"
    dicts = []
    for dic in target:
        dict_text = ""
        dict_text += "\n  {"
        dict_text += ",".join([f'\n    "{key}": {dic[key]}' for key in dic])
        dict_text += "\n  }"
        dicts.append(dict_text)
    return out.replace("REPLACE", ",".join(dicts))


def add_to_list(target: list[dict]):
    def target_function(func):
        def inner_func(start: int, stop: int, names: list[str]):
            count = 0
            for i in range(start, stop, 1 if start < stop else -1):
                try:
                    new_dict = target[count]
                except IndexError:
                    new_dict = {}
                    target.append(new_dict)
                finally:
                    new_dict[names[0]] = i
                    new_dict[names[1]] = func(i)
                count += 1
        return inner_func
    return target_function


if __name__ == "__main__":
    results = []

    @add_to_list(results)
    def linear_function(x):
        return 2 * x

    linear_function(0, 4, ["x", "y"])
    print(json_form(results))

