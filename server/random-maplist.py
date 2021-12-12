import argparse
import json
from os.path import isfile
from sys import exit
from random import shuffle

parser = argparse.ArgumentParser(description='Convert given json maplist into randomized ordered q3a server map rotation config.')
parser.add_argument('jsonlist',  help='JSON map list file. See example.', type=str)
args = parser.parse_args()

param_keys = ['bot_minplayers', 'capturelimit', 'timelimit', 'fraglimit']

if not isfile(args.jsonlist):
    exit(f'Error: Given jsonlist file "{args.jsonlist}" does not exist.')

with open(args.jsonlist, 'r') as maplist_file:
    maplist = json.load(maplist_file)

maps = maplist.get('maps', {})
defaults = maplist.get('defaults', {})

shuffle(maps)
result = []
size = len(maps)
for i in range(size):
    e = dict(defaults)
    e.update(maps[i])
    params = ' ; '.join([str('set '+key+' '+str(e[key])) for key in param_keys]) + f'; map {e["map"]}'
    if i < size - 1:
        result.append(str(f'set d{i+1} "{params} ; set nextmap vstr d{i+2};"'))
    else:
        result.append(str(f'{params} ; set d{i+1} "set nextmap vstr d1;"'))

result.append('vstr d1')

for item in result:
    print(item)

