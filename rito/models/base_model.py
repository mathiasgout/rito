class Model:
    def __repr__(self):
        state = [f'{k}={v!r}' for (k, v) in vars(self).items()]
        return f'{self.__class__.__name__}({", ".join(state)})'
