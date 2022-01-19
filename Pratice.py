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
distance = convert_feet_to_meters(200)
print("Distance is", distance,"meters")
print("Now I am done")

print("1000 inches in meters are", convert_feet_to_meters(convert_inches_to_feet(1000.0)))

print("1000 inches in meters are", convert_inches_to_meters(1000))