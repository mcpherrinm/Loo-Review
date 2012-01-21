from elixir import *

options_defaults['tables_options'] = dict(mysql_engine="InnoDB")
options_defaults['mapper_options'] = { 'save_on_init': False }

class Review(Entity):
    """Reviews contain information from reviewers that may differ between reviews,
    such as cleanliness and comfort
    For now, a review is a specific room"""
    room = ManyToOne('Room')
    description = Field(UnicodeText)
    rank = Field(Integer)

    def __init__(self, room, description, rank):
        self.room = room
        self.description = description
        self.rank = rank

    def __repr__(self):
        return '<Review of {0}>'.format(self.room)

class Room(Entity):
    """A Bathroom contains information about it that
    is non-subjective, such as toilet count and facilities"""
    reviews = OneToMany('Review')
    name = Field(Unicode(30))
    gender = Field(Enum(u'Male', u'Female', u'Unisex'))
    location = ManyToOne('Floor')
    # Co-ord pair, WRT PDF floor plans, units etc TBD
    mapx = Field(Integer)
    mapy = Field(Integer)

    def __init__(self, name, gender, floor, x, y):
        self.name = name
        self.gender = gender
        self.location = floor
        self.mapx = x
        self.mapy = y

    def __repr__(self):
        return "{0} {1}".format(self.location.building.code, self.name)

class Floor(Entity):
    name = Field(Unicode(10))
    building = ManyToOne('Building')
    rooms = OneToMany('Room')

    def __init__(self, name, building):
        self.name = name
        self.building = building

    def __repr__(self):
        return "{0},{1}".format(self.building.code, self.name)

class Building(Entity):
    code = Field(Unicode(10), unique=True)
    name = Field(Unicode(120), unique=True)
    floors = OneToMany('Floor')

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __repr__(self):
        return '{0} - {1}'.format(self.code, self.name)

