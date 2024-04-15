def move_forward():
    print("moving forward")

def turn(direction):
    print(f"turning {direction}")

def start_engine():
    print("starting engine")

def stop_engine():
    print("stopping engine")

def follow_roundabout(exit_number):
    print("Entering the roundabout")
    print(f"taking exit number {exit_number} from the roundabout")


start_engine()
destination = input("Where do you want to go? ")

if destination == "library":
        move_forward()
        turn("left")
        print("We arrived at the library")
elif destination == "tech park":
        move_forward()
        turn("right")
        print("We arrived at the tech park.")
elif destination in ["hospital","mall","airport","university","stadium"]:
    if destination == "hospital":
            move_forward()
            follow_roundabout(1)
            print("We arrived at the hospital.")
    elif destination == "mall":
            move_forward()
            follow_roundabout(2)
            move_forward()
            turn("right")
            print("We arrived at the mall")
    elif destination == "airport":
        move_forward()
        follow_roundabout(3)
        print("We arrived at the airport")
    elif destination == "university" or "stadium":
        move_forward()
        follow_roundabout(4)
        #move_forward()
        if destination == "university":
            move_forward()
            turn("left")
            print("We arrived at the university")
        elif destination == "stadium":
             move_forward()
             turn("right")
             print("We arrived at the stadium")

elif destination not in ["library","tech park","hospital","mall","airport","university","stadium"]:
     print("Destination not available.")   
stop_engine()

