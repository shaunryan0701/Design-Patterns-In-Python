'''
Class for a small chair
'''

from interface_chair import IChair
class SmallChair(IChair):
    "The Small Chair Concrete Class implements the IChair interface"
    def __init__(self) -> None:
        self._height = 40
        self._width = 40
        self._depth = 35
    

    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }
    