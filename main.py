import simplekml
import argparse
import string
import random

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('target', type=str)
arg_parser.add_argument('-s', '--size', type=int, default=20)

LAT_RANGE = range(-90, 91)
LON_RANGE = range(-180, 181)

def randomString(characters):
    new_str = ''

    for i in range(characters):
        new_str = new_str + random.choice(string.ascii_letters)

    return new_str

def randomPoint():
    return (random.choice(LON_RANGE), random.choice(LAT_RANGE))

def randomLine(length):
    coords = []

    for i in range(length):
        coords.append(randomPoint())

    return coords

def main() :
    arguments = arg_parser.parse_args()
    
    kml = simplekml.Kml(name=arguments.target)

    for i in range(arguments.size):
        kml.newlinestring(name=randomString(10), description=randomString(30), coords=randomLine(int(100 * random.random())))

    kml.save(arguments.target + '.kml')

    return

main()
