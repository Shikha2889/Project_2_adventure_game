import json
import sys

def load_world_map(fn):
    #opening JSON file
    f = open(fn, 'r')
    data = json.loads(f.read())
    return data

worldmap = load_world_map(sys.argv[1])


#variable to store the current location of the user
curr_loc = "start"
next_room = 'null'

# a list of all the rooms user is required to visit before he/she can win the game
required_rooms =[roomname for roomname in worldmap if worldmap[roomname]['mustvisit']]
#print(required_rooms)

visited_rooms =[]

def list_contains(list1,list2):
    check = all(item in list1 for item in list2)
    return check


while True:
    #if curr_loc == "start" and next_room=='null':
    #    print(worldmap["start"]["description"])
    
    for roomname in worldmap:
        if(roomname ==curr_loc):
            print(worldmap[roomname]["description"])
            exit =list(worldmap[roomname]["exits"].keys())
            print(exit)
            command = input("> ")
            if command not in exit:
                print("You can't go that way.") 
            else:
                next_room = worldmap[roomname]["exits"][command]
                print(next_room)
                visited_rooms.append(next_room)
                #print(worldmap[next_room]["description"])
                #print(worldmap[next_room]['roomtype'])
                if(worldmap[next_room]["roomtype"]=="win"):
                    visited= list_contains(visited_rooms,required_rooms)
                    if(visited == False):
                        print("You aren't ready to go there yet")
                    else:

                        curr_loc = next_room
                        print(worldmap[roomname]["description"])
                        break;
                        #print("current_loc: ", curr_loc)
                elif(worldmap[next_room]["roomtype"]=='lose'):
                    print(worldmap[next_room]["description"]);
                    curr_loc = next_room    
                    #print("exit lose")
                    break;
                else:
                    curr_loc = next_room
                    #print("current_loc: ", curr_loc)

        if(worldmap[curr_loc]["roomtype"]=="win" or worldmap[curr_loc]["roomtype"]=="lose"):
            break;