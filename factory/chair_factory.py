"The Factory Class"
from small_chair import SmallChair
from medium_chair import MediumChair
from big_chair import BigChair

class ChairFactory():
    
    @staticmethod
    def get_chair(chair):
        if chair == 'SmallChair':
            return SmallChair()
        elif chair == 'MediumChair':
            return MediumChair()
        else:
            return BigChair()
