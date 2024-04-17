import copy

class Room():
    label: str
    chair_count: dict
    walls : list
    done: bool

    def __init__(self, label=None, chair_count=None, walls=[]):
        self.label = label
        self.chair_count = chair_count

        if bool(walls):
            self.walls = copy.deepcopy(walls)
        else:
            self.walls = []
        self.done = False

    def get_label(self):
        return self.label

    def get_chair_count(self):
        return self.chair_count

    def print_info(self):
        print(f'room.label={self.label}, ' \
              f'room.chair_count={self.chair_count}' \
              f'room.done={self.done}')
        print("\tWalls:")
        for wall in self.walls:
            wall.print_data()
