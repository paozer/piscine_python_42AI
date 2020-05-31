def ft_reduce(function_to_apply, list_of_inputs):
    if len(list_of_inputs) < 2:
        return
    ret = next(i)
    for i in iter(list_of_inputs):
        ret = function_to_apply(ret, i)
    return ret
