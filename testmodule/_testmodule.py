"encoding utf-8"

class Person:

    def __init__(self,age,sex):
        self._age = age
        self._sex = sex

    def get_age(self):
        return self._age

    def get_sex(self):
        return self._sex