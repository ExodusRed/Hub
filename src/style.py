class Style():
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            self.key = val
            print(key, val)