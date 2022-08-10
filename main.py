import simplekml
import argparse
import string
import random

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('target', type=str)
arg_parser.add_argument('-s', '--size', type=int, default=20)
arg_parser.add_argument('-t', '--type', type=str, default='point')

LAT_RANGE = range(-90, 91)
LON_RANGE = range(-180, 181)

def randomString(characters):
    new_str = ''

    for i in range(characters):
        new_str = new_str + random.choice(string.ascii_letters)

    return new_str

def randomCoord():
    return (random.choice(LON_RANGE), random.choice(LAT_RANGE))

def randomLine(length):
    coords = []

    for i in range(length):
        coords.append(randomCoord())

    return coords

def main() :
    arguments = arg_parser.parse_args()
    
    kml = simplekml.Kml(name=arguments.target)

    for i in range(arguments.size):
        if arguments.type == 'point':
            point = kml.newpoint(name=randomString(10), description=randomString(30), coords=[randomCoord()])
        
        elif arguments.type == 'line':
            line = kml.newlinestring(name=randomString(10), description=randomString(30), coords=randomLine(int(100 * random.random())))
            line.style.linestyle.color = simplekml.Color.red
            line.style.linestyle.width = 10
        
        else:
            print('Not a valid type.')
            return

    kml.save(arguments.target + '.kml')

    return

main()
