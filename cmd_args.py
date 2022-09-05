import argparse
# import sys

# name = sys.argv[1]

# print("Hello " + name)


#--------- below statements are separate-------------#

parser = argparse.ArgumentParser(
  description="This program prints the numbers"
)

parser.add_argument("-c", "--color", metavar="color", required=True,choices={"red", "blue"}, help="the color to search for")

args = parser.parse_args()

print(args.color)