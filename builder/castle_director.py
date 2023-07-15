'''
Director for building a castle
'''
from house_builder import HouseBuilder

class CastleDirector():
    @staticmethod
    def construct():
        return HouseBuilder().set_building_type("Castle")\
          .set_wall_material("Stone")\
          .set_number_doors(100)\
          .set_number_windows(500)\
          .get_result()
    