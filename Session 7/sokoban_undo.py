#pusher
#box
#destination
#map

#set pusher ccoordinate
#rep: P
pusher = {
    "x": 1,
    "y": 0
    }

#set box coordinate
#rep: B
boxes = [
    {
        "x": 3,
        "y": 2
    },
    {
        "x": 1,
        "y": 3
    }
]
#set destination coordinate
#rep: D
dests = [{
    "x": 2,
    "y": 3
        }
        ,{
            "x": 5,
            "y": 6}
        ]

#set map_size
size = {
    "x": 6,
    "y": 7
    }

# re-structure
# day nhieu hop

saved_pusher = pusher.copy()
saved_boxes = [box.copy() for box in boxes]

def reset_level(saved_pusher, saved_boxes):
    global pusher, boxes

    pusher = saved_pusher
    boxes = saved_boxes

    
def is_in_map(x, y, size):
    return 0 <= x < size["x"] and 0 <= y < size["y"]

def check_overlap(x, y, items):
    for item in items:
        if x == item["x"] and y == item["y"]:
            return item
    return None

################################################

def print_map(size, pusher, boxes):    
    for y in range(size["y"]):
        for x in range(size["x"]):
            if x == pusher["x"] and y == pusher["y"]:
                print(" P ", end ="")
            elif check_overlap(x, y, boxes):
                print(" B ", end ="")
            elif check_overlap(x, y, dests):
                print(" D ", end ="")
            else:
                print(" - ", end ="")
        print()


##print_map(size, pusher, boxes)

####################################################

def move(item, dx, dy):
    item["x"] += dx
    item["y"] += dy

    return item

    

def input_process(direction):
    dx = 0
    dy = 0
    if direction == "W":
        dy -= 1
        #dy = dy - 1
    elif direction == "A":
        dx -= 1
    elif direction == "S":
        dy += 1
    elif direction == "D":
        dx += 1
    else:
        print("You enter wrong button pls do this again bro :)")

    return dx, dy

def check_win(boxes, dests):
    count = 0
    for box in boxes:
        if check_overlap(box["x"],box["y"], dests)is not None:
            count += 1
    if count == len(boxes):
        return True
    else:
        return False

undo_pusher = 0
undo_boxes = 0
        

##########################

# main GAME_LOOP
while True:
    print_map(size, pusher, boxes)
    direction = input("What is your next move? W/A/S/D? Enter R to reset game").upper()
    
    if direction == "R":
        reset_level(saved_pusher, saved_boxes)
        map(pusher, boxes, dests)
        continue


    if direction == "U":
        if undo_pusher != 0:
            reset_level(undo_pusher, undo_boxes)
            map(pusher, boxes, dests)
            continue
        else:
            print("Can't undo")
            
    undo_pusher = pusher.copy()
    undo_boxes = [box.copy() for box in boxes]
        
    # xu ly dau vao` 
    dx, dy = input_process(direction)

    found_box = check_overlap(pusher["x"] + dx, pusher["y"] + dy, boxes)
##    found_box["x"]
##    found_box["y"]

    if found_box is not None:
        if check_overlap(found_box["x"] + dx, found_box["y"] + dy, boxes) is None:
            if is_in_map(found_box["x"] + dx, found_box["y"] + dy, size):
                found_box = move(found_box, dx, dy)
                pusher = move(pusher, dx, dy)
                
                
    elif is_in_map(pusher["x"] + dx, pusher["y"] + dy, size):
        pusher = move(pusher, dx, dy)
        

        
    if check_win(boxes, dests):
        print("fucking win")
        break




print("you won")

