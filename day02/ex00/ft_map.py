from collections import Iterable


def ft_map(function_to_apply, list_of_inputs):
    if isinstance(list_of_inputs, Iterable) is False:
        print('ft_map requires requires iterable list of input')
        raise Exception
    for input_ in list_of_inputs:
        yield(function_to_apply(input_))
