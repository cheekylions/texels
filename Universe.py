import Room

introduction = """Hello! Welcome to the first universe!
Have fun."""

first_room = Room.Room()

first_room.name = "The First Room"

first_room.width = 10
first_room.height = 10
first_room.length = 20

# There's got to be a better way than this?
# Or should layouts simply be kept in their own files...
# Or should all room data be kept in its own file, then merely referenced?
# Eventually will want some kind of visual editing tool to make complex bodies easy to design

first_room.layout = [
    [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1]],

    [[1, 1, 1, 1, 1],
     [1, 0, 0, 0, 1],
     [1, 0, 0, 0, 1],
     [1, 0, 0, 0, 1],
     [1, 0, 0, 0, 1],
     [1, 1, 1, 1, 1]],

    [[1, 1, 1, 1, 1],
     [1, 0, 0, 0, 1],
     [1, 0, 0, 0, 1],
     [1, 0, 0, 0, 1],
     [1, 0, 0, 0, 1],
     [1, 1, 1, 1, 1]],

    [[1, 1, 1, 1, 1],
     [1, 0, 0, 0, 1],
     [1, 0, 0, 0, 1],
     [1, 0, 0, 0, 1],
     [1, 0, 0, 0, 1],
     [1, 1, 1, 1, 1]],

    [[1, 1, 1, 1, 1],
     [1, 0, 0, 0, 1],
     [1, 0, 0, 0, 1],
     [1, 0, 0, 0, 1],
     [1, 0, 0, 0, 1],
     [1, 1, 1, 1, 1]],

    [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1]],
                    ]
