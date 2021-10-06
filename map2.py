worldmap = {
    'start': {
        'description': 'You are in a hallway that runs east-west.  To the west, at the end of the hallway you see a treasure chest held closed by a comically large padlock.  To the east, you can see a sign at the end of the hallway that reads "KEY HERE".',
        'exits': {'east': 'eastend', 'west': 'westend'},
        'mustvisit': False,
        'roomtype': 'normal'
    },
    'eastend': {
        'description': 'You reach the east end of the hallway and find a table with a key sitting on top.  You take the key.  The only way to go is west, back to the place where you started.',
        'exits': {'west': 'start'},
        'mustvisit': True,
        'roomtype': 'normal'
    },
    'westend': {
        'description': 'You go to the treasure chest, use the key to open its padlock, and lift the lid.  Inside is a thick leather-bound book titled "A pictorial tour of the Unicode standard". It has been your dream to own this book ever since lecture 7 of MCS 260.  You take the book and smile with satisfaction.',
        'exits': {},
        'mustvisit': False,
        'roomtype': 'win'
    }
}
