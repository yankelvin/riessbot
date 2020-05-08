map_maze = {
    'A': {
        'adjacent': [('B', 5)],
        'point': (1, 1)
    },
    'B': {
        'adjacent': [('A', 5), ('C', 7), ('F', 2)],
        'point': (1, 6)
    },
    'C': {
        'adjacent': [('B', 7), ('L', 8)],
        'point': (1, 13)
    },
    'D': {
        'adjacent': [('E', 3)],
        'point': (3, 1)
    },
    'E': {
        'adjacent': [('D', 3), ('I', 6)],
        'point': (3, 4)
    },
    'F': {
        'adjacent': [('B', 2), ('G', 5), ('J', 6)],
        'point': (3, 6)
    },
    'G': {
        'adjacent': [('F', 5), ('K', 6)],
        'point': (3, 11)
    },
    'H': {
        'adjacent': [('I', 3)],
        'point': (9, 1)
    },
    'I': {
        'adjacent': [('E', 6), ('J', 2), ('H', 3)],
        'point': (9, 4)
    },
    'J': {
        'adjacent': [('F', 6), ('I', 2), ('K', 5), ('O', 2)],
        'point': (9, 6)
    },
    'K': {
        'adjacent': [('G', 6), ('J', 5), ('L', 2), ('T', 9)],
        'point': (9, 11)
    },
    'L': {
        'adjacent': [('C', 8), ('K', 2), ('U', 9)],
        'point': (9, 13)
    },
    'M': {
        'adjacent': [('N', 3)],
        'point': (11, 1)
    },
    'N': {
        'adjacent': [('M', 3), ('O', 2), ('R', 7)],
        'point': (11, 4)
    },
    'O': {
        'adjacent': [('J', 2), ('N', 2), ('P', 3)],
        'point': (11, 6)
    },
    'P': {
        'adjacent': [('O', 3), ('S', 7)],
        'point': (11, 9)
    },
    'Q': {
        'adjacent': [('R', 3)],
        'point': (18, 1)
    },
    'R': {
        'adjacent': [('N', 7), ('Q', 3), ('S', 5)],
        'point': (18, 4)
    },
    'S': {
        'adjacent': [('P', 7), ('R', 5), ('T', 2)],
        'point': (18, 9)
    },
    'T': {
        'adjacent': [('K', 9), ('S', 2), ('U', 2)],
        'point': (18, 11)
    },
    'U': {
        'adjacent': [('L', 9), ('T', 2)],
        'point': (18, 13)
    }
}
