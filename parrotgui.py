import argparse

parser = argparse.ArgumentParser(description='Literraly just a CLI ASCII animator')
parser.add_argument('-f', '--folder',
                    required=False)
parser.add_argument('-c', '--color',
                    required=False, action='store_true')
args = parser.parse_args()


print('folder:'+ args.folder+' color: ', args.color)