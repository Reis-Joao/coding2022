from dis import dis

def convert_feet_to_meters(distance_feet):
    return 0.3048 * distance_feet

def convert_inches_to_feet(distance_inches):
    return distance_inches / 12.0

def convert_inches_to_meters(distance_inches):
    distance_feet = convert_inches_to_feet(distance_inches)
    distance_meter = convert_feet_to_meters(distance_feet)
    return distance_meter

print("I am here!")
distance = 10
print(distance)
distance_meter = convert_feet_to_meters(200)
print("Distance is", distance,"meters")
print("Now I am done")

print("1000 inches in meters are", convert_feet_to_meters(convert_inches_to_feet(1000.0)))

print("1000 inches in meters are", convert_inches_to_meters(1000))

#If Statements
if distance_meter > 10:
    print("Distance is greater than 10 meters.")
else:
    print("Distance is not greater than 10 meters.")

I_am_lying = True

if I_am_lying:
    print("I am lying")
else:
    print("I am telling the truth")

print(distance_meter > 10)

distance_meter = 0.0
if distance_meter:
    # same as not distance_meter == 0.0
    print("What is distance")
else:
    print("Distance is", distance_meter)

name = ""
if name:
    # same as not name == ""
    print(name)
print("Name has been printed")