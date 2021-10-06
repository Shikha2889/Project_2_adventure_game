worldmap = {
    'start': {
        'description': "Your goal is to get your laptop and charger and meet your friends to work on MCS 260.  You are standing in UIC's Student Center East, near the revolving doors leading to the main quad.  To the east is a hallway leading to the bookstore and the escalators.  To the south is the I-card office.  To the north is Panda Express.  The revolving doors to the west don't seem to be working right now.",
        'exits': {'north': 'panda', 'south': 'cardoffice', 'east': 'hallway'},
        'mustvisit': False,
        'roomtype': 'normal'
    },
    'panda': {
        'description': 'You are in Panda Express, surrounded by students eating lo mein.  The only exit is to the south.',
        'exits': {'south': 'start'},
        'mustvisit': False,
        'roomtype': 'normal'
    },
    'cardoffice': {
        'description': 'You are standing outside the I-card office.  There are at least fifty students standing here, waiting for the office to open so they can get their IDs renewed.  The office is closed and locked.  To the north is the entrance lobby.',
        'exits': {'north': 'start'},
        'mustvisit': False,
        'roomtype': 'normal'
    },
    'hallway': {
        'description': 'This is the main hallway of SCE, with the escalator to the north, the bookstore to the south, the Halsted lobby to the east, and the quad lobby to the west.',
        'exits': {'north': 'escalators', 'south': 'bookstore', 'east': 'halsted', 'west': 'start'},
        'mustvisit': False,
        'roomtype': 'normal'
    },
    'halsted': {
        'description': 'You are in the entrance lobby of SCE near Halsted street.  To the east, where you would expect the outer doors to be, there is the event horizon of a gravitational singularity (a black hole).  To the west is the hallway.',
        'exits': {'east': 'blackhole', 'west': 'hallway'},
        'mustvisit': False,
        'roomtype': 'normal'
    },
    'bookstore': {
        'description': 'You are in the UIC bookstore.  Against the back wall (to the south) is an area where computers are sold and repaired.  To the north is the bookstore exit.',
        'exits': {'north': 'hallway', 'south': 'computershop'},
        'mustvisit': False,
        'roomtype': 'normal'
    },
    'computershop': {
        'description': 'As you enter the computer shop, a helpful clerk recognizes you and hands you the laptop they recently repaired for you.  You accept it gratefully.  The rest of the bookstore is to the north.',
        'exits': {'north': 'bookstore'},
        'mustvisit': True,
        'roomtype': 'normal'
    },
    'blackhole': {
        'description': 'You fall into the gravitational singularity.  In time, your study partners wonder what happened to you.',
        'exits': {},
        'mustvisit': False,
        'endgame': True,
        'roomtype': 'lose'
    },
    'escalators': {
        'description': 'This is the escalator area.  To the south is the main hallway.  Up the escalator is the second floor.',
        'exits': {'south': 'hallway', 'up': 'floor2main'},
        'mustvisit': False,
        'roomtype': 'normal'
    },
    'floor2main': {
        'description': 'You are standing at the top of the escalators, on the second floor of SCE.  Dunkin Donuts is here, but it is closed.  To the west is a large seating area.  You can see your friends from MCS 260 waving to you from a table there.  To the east is an Amazon package pickup area.  Down the escalator is the first floor.',
        'exits': {'west': 'seating', 'east': 'amazon', 'down': 'escalators'},
        'mustvisit': False,
        'roomtype': 'normal'
    },
    'amazon': {
        'description': 'You are in the Amazon package pickup room.  You use the code from your email to open a locker and retrieve your charger.  The exit is to the west.',
        'exits': {'west': 'floor2main'},
        'mustvisit': True,
        'roomtype': 'normal'
    },
    'seating': {
        'description': 'You enter the seating area and sit down with your friends from MCS 260.  You open your laptop and plug in your charger.  Together, you and your friends complete the remaining problems from Worksheet 29 in no time.  SUCCESS!',
        'exits': {},
        'mustvisit': False,
        'roomtype': 'win'
    }
}
