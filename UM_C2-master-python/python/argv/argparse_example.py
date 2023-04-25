import argparse

parser = argparse.ArgumentParser(description="ejemplo parser")

parser.add_argument("-f", "--file", type=str, required=False, help="string")
parser.add_argument("-s", "--size", type=int, default=1024, help="numero")
args = parser.parse_args()

print('File %s.' % args.file)
print('Size %d.' % args.size)

