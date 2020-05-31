class Matrix:
    def __init__(self, arg1, arg2=None):
        if arg2 is None:
            if type(arg1) is list:
                if not arg1:
                    return None
                h = 0
                w = len(arg1[0])
                for row in arg1:
                    if type(row) is not list or len(row) != w:
                        return None
                self.data = arg1
                self.shape = (h, w)
            elif type(arg1) is tuple:
                self.data = list()
                for h in range(arg1[0]):
                    self.data.append(list())
                    for w in range(arg1[1]):
                        self.data[h].append(0.0)
                self.shape = arg1
        elif type(arg1) is list and type(arg2) is tuple:
            if len(arg2) != 2:
                return None
            h = arg2[0]
            w = arg2[1]
            if len(arg1) != h:
                return None
            self.data = list()
            for i in range(h):
                self.data.append(list())
                if len(arg1[i]) != w:
                    return None
                for y in range(w):
                    self.data[i].append(arg1[i][y])

    def __str__(self):
        text = '\n'.join(str(row) for row in self.data)
        text += f'\n{str(self.shape)}'
        return text
