class Model:
    def _format_attribute_name(self, raw_attribute_name: str) -> str:
        new_attribute_name = ""
        for i, char in enumerate(raw_attribute_name):
            if char.isupper():
                if i != 0:
                    # For handle "CC" in keys 
                    if char != "C" or raw_attribute_name[i-1] != "C":
                        new_attribute_name += "_"
                new_attribute_name += char.lower()
            else:
                new_attribute_name += char
        return new_attribute_name 

    def __repr__(self):
        state = [f'{k}={v!r}' for (k, v) in vars(self).items()]
        return f'{self.__class__.__name__}({", ".join(state)})'
