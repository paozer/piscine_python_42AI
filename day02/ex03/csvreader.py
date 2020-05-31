class CsvReader():
    def __init__(self, filename=None, sep=',',
                 header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.data = None
        self.header = None
        try:
            self.f = open(filename, 'r')
        except FileNotFoundError:
            self.f = None
            print("File not found. Try again!")
            return None
        lst = self.f.readlines()
        if skip_top > 0 and skip_top < len(lst):
            lst = lst[skip_top::]
        if skip_bottom > 0 and skip_bottom < len(lst):
            lst = lst[:-skip_bottom:]
        clean = []
        for i in lst:
            i = i.rstrip()
            i = i.split(sep)
            clean.append(l)
        lst = clean
        if header:
            length = len(lst[1])
        else:
            length = len(lst[0])
        for i in lst:
            if len(i) is not length:
                return None
        if header:
            self.header = lst[0]
            self.data = lst[1::]
        else:
            self.header = None
            self.data = lst

    def getdata(self):
        return self.data

    def getheader(self):
        return self.header

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        if self.f is not None:
            self.f.close()


if __name__ == "__main__":
    with CsvReader("test", sep='.', header=False, skip_bottom=4) as reader:
        print(reader.getheader())
        print(reader.getdata())
