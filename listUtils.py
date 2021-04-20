class list:
    def __init__(self, arr):
        self.arr = arr

    def even(self):
        data = []
        for i in self.arr:
            try:
                if i % 2 == 0:
                    data.append(i)
            except:
                pass
        return data

    def odd(self):
        data = []
        for i in self.arr:
            try:
                if i % 2 != 0:
                    data.append(i)
            except:
                pass
        return data

    def under(self, num):
        data = []
        for i in self.arr:
            try:
                if i < num:
                    data.append(i)
            except:
                pass
        return data

    def over(self, num):
        data = []
        for i in self.arr:
            if i > num and isinstance(i, int):
                data.append(i)
        return data

    def in_range(self, min, max):
        data = []
        for i in self.arr:
            try:
                if i >= min and i <= max:
                    data.append(i)
            except:
                pass
        return data