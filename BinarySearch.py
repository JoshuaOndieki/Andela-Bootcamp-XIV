class BinarySearch(list):
    def __init__(self, a, b):
        super(BinarySearch, self).__init__((range(b, (b * a) + 1, b)))
        self.list_built = (range(b, (b * a) + 1, b))
        self.length = len(self.list_built)
        self.count = 0
        self.iter_num = {}

    def search(self, search_term):
        try:
            list_built = self.list_built
            self.iter_num = {}
            if search_term is not None:
                while self.length > 0:
                    self.count += 1
                    mid = int(self.length / 2)
                    if mid >= 1:
                        if search_term == list_built[mid]:
                            self.iter_num['count'] = self.count
                            self.iter_num['index'] = self.list_built.index(search_term)
                            try:
                                return self.iter_num
                            except TypeError:
                                self.iter_num = {}
                                return 0
                        elif search_term < list_built[mid]:
                            list_built = list_built[:mid]
                        elif search_term > list_built[mid]:
                            list_built = list_built[mid + 1:]

                        self.length = mid
                    else:
                        break
        except TypeError:
            return 0