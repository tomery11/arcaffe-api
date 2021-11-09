from abc import ABCMeta,abstractstaticmethod

class IData(metaclass=ABCMeta):
    @abstractstaticmethod
    def get_data():
        """ implement in child"""

