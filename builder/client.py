'''
Client to access Director
'''

from castle_director import CastleDirector
from igloo_director import IglooDirector

CASTLE = CastleDirector.construct()
IGLOO = IglooDirector.construct()
print(CASTLE.construction())
print(IGLOO.construction())