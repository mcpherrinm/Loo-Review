from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Unicode, ForeignKey

Base = declarative_base()

class Building(Base):
    __tablename__ = 'base'
    id = Column(Integer, primary_key=True)
    code = Column(Unicode, unique=True)
    name = Column(Unicode, unique=True)

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __repr__(self):
        return '{0} - {1}'.format(self.code, self.name)

class Floor(Base):
    __tablename__ = 'floor'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode)
    building_id= Column(Integer, ForeignKey(Building.id))
    building = relationship(Building, backref='floors')

    def __init__(self, name, building):
        self.name = name
        self.building = building

    def __repr__(self):
        return "{0},{1}".format(self.building.code, self.name)

class Room(Base):
    """A Bathroom contains information about it that
    is non-subjective, such as toilet count and facilities"""
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode)
    #gender = Field(Enum(u'Male', u'Female', u'Unisex'))
    floor_id = Column(Integer, ForeignKey(Floor.id))
    location = relationship(Floor, backref='rooms')
    # Co-ord pair, WRT PDF floor plans, units etc TBD
    mapx = Column(Integer)
    mapy = Column(Integer)

    def __init__(self, name, gender, floor, x, y):
        self.name = name
        self.gender = gender
        self.location = floor
        self.mapx = x
        self.mapy = y

    def __repr__(self):
        return "{0} {1}".format(self.location.building.code, self.name)


class Review(Base):
    """Reviews contain information from reviewers that may differ between reviews,
    such as cleanliness and comfort
    For now, a review is a specific room"""
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    room_id = Column(Integer, ForeignKey(Room.id))
    room = relationship(Room, backref='reviews')
    description = Column(Unicode)
    rank = Column(Integer)

    def __init__(self, room, description, rank):
        self.room = room
        self.description = description
        self.rank = rank

    def __repr__(self):
        return '<Review of {0}>'.format(self.room)
