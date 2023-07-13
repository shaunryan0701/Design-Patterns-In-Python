'''
Class for a medium chair
'''

from interface_chair import IChair
class MediumChair(IChair):
    "The Medium Chair Concrete Class implements the IChair interface"
    def __init__(self) -> None:
        self._height = 60
        self._width = 65
        self._depth = 50
    

    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }
    