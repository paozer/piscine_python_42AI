def what_are_the_vars(*args, **kwargs):
    obj = ObjectC()
    for key in kwargs.keys():
        if key.startswith("var_"):
            raise NameError("Named variables can't start with var_.")
        setattr(obj, str(key), kwargs[key])
    i = 0
    for arg in args:
        setattr(obj, 'var_' + str(i), arg)
        i += 1
    return obj


class ObjectC(object):
    def __init__(self):
        return


def doom_printer(obj):
    if obj is None:
        print("Error")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print(f"{attr}: {value}")
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
