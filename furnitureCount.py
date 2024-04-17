import argparse
from re import finditer, search

from wallClass import Wall
from roomClass import Room

CHAIR_TYPES = 'WPSC'


def read_floor_plan(floor_plan_file_path):
    temp = ""
    with open(floor_plan_file_path) as floor_plan_file:
        for line in floor_plan_file:
            temp += line
    return temp


def custom_print(count_data):
    temp = ""
    for chair_type in count_data:
        temp += f'{chair_type}: {count_data[chair_type]}'
        if chair_type != "C":
            temp += f', '
    print(temp)


def count_furniture(floor_plan_file_path):

    floor_plan = read_floor_plan(floor_plan_file_path)
    #print(floor_plan)

    rooms_temp = []
    spaces = []
    rows = floor_plan.split('\n')
    rows.pop(0)

    for no, row in enumerate(rows):
        found = list(finditer(r'[^/\\|+-]+', row))
        did_found = 0
        if True:
            did_found = 1
            wall_segments = [Wall(no, rs.start(), rs.end()) for rs in found]
            for rt in rooms_temp:
                for wall in wall_segments:
                    if max(rt.walls[-1].col_start, wall.col_start) < min(rt.walls[-1].col_end, wall.col_end):
                        rt.walls.append(wall)
                        wall_segments.remove(wall)
                        break
                else:
                    text = ''.join([rows[w.idx][w.col_start:w.col_end] for w in rt.walls])
                    label = search(r'\(\w+( +\w+)*\)', text)
                    if label:
                        rt.label = label[0][1:-1]
                        rt.chair_count = {chair_types: text.count(chair_types) for chair_types in CHAIR_TYPES}
                        spaces.append(rt)
                    rt.done = True

            #reset ws list to only not complete
            rooms_temp = [rt for rt in rooms_temp if rt.done == False]
            #create new wss with remaining rss
            for wall in wall_segments:
                new_room = Room()
                new_room.walls.append(wall)
                rooms_temp.append(new_room)
    for rt in rooms_temp:
        print(rt.label, rt.done)

    info_room = []
    total_count = { "W": 0, "P": 0, "S": 0, "C": 0}
    for space in spaces:
        temp_label = space.get_label()
        temp_chair_count = space.get_chair_count()

        for chair_type in temp_chair_count:
            total_count[chair_type] += temp_chair_count[chair_type]
        
        info_room.append({ 'label': temp_label, 'count': temp_chair_count})
    
    sorted_spaces = sorted(info_room, key=lambda r: r['label'])
    
    print("total: ")
    custom_print(total_count)

    for space in sorted_spaces:
        print(space['label'])
        custom_print(space['count'])


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
            "--floor_plan_file_path",
            type=str,
            required=True,
            help="Path to the file that has the floor plan."
            )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    count_furniture(args.floor_plan_file_path)

