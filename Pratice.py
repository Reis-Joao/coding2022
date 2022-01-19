from dis import dis

def convert_feet_to_meters(distance):
    print(distance)
    return 0.3048 * distance

print("I am here!")
distance = 10
print(distance)
distance = convert_feet_to_meters(200)
print(distance)
print("Distance is", distance,"meters")
print("Now I am done")