from math import pow, sqrt, ceil


class TinyStatistician:
    def __init__(self):
        pass

    def mean(self, x):
        if not x:
            return None
        ret = 0
        m = len(x)
        for i in x:
            ret += float(i) / m
        return ret

    def median(self, x):
        return self.quartiles(x, 0.5)

    def quartiles(self, x, percentiles):
        if not x:
            return None
        if percentiles == 0:
            return x[0]
        if percentiles == 1:
            return x[len(x) - 1]
        k = ceil(percentiles * len(x))
        if percentiles * len(x) < k:
            return float(x[k - 1])
        return 0.5 * (x[k - 1] + x[k])

    def var(self, x):
        if not x:
            return None
        ret = 0
        mean = self.mean(x)
        for i in x:
            ret += pow(i - mean, 2)
        length = len(x)
        return ret / length

    def std(self, x):
        return sqrt(self.var(x))


if __name__ == "__main__":
    yes = TinyStatistician()
    a = [2, 1, 3, 4, 5, 6, 99]
    print(yes.mean(a))
    print(yes.median(a))
    print(yes.quartiles(a, 0))
    print(yes.var(a))
    print(yes.std(a))
    print()
    b = [2, 1, 3, 4, 6, 5]
    print(yes.mean(b))
    print(yes.median(b))
    print(yes.quartiles(b, 0.7))
    print(yes.var(b))
    print(yes.std(b))
