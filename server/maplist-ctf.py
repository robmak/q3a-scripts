maps = [
    {'map': 'q3ctf3', 'bot_minplayers': 4, 'capturelimit': 3},
    {'map': 'q3ctf4', 'bot_minplayers': 4, 'capturelimit': 8, 'timelimit': 10},
    {'map': '13agony_ctf', 'bot_minplayers': 5, 'timelimit': 12},
    {'map': '13circle', 'bot_minplayers': 3},
    {'map': '13dream', 'bot_minplayers': 4, 'capturelimit': 8},
    {'map': '13ground_xt', 'bot_minplayers': 3, 'timelimit': 10},
    {'map': '13vast', 'bot_minplayers': 4, 'capturelimit': 7, 'timelimit': 10},
    {'map': 'ct3ctf1', 'bot_minplayers': 5, 'capturelimit': 8},
    {'map': 'ctctf6', 'bot_minplayers': 4, 'capturelimit': 7},
    {'map': 'eg_ctf1', 'bot_minplayers': 3, 'capturelimit': 8},
    {'map': 'geit3ctf1', 'bot_minplayers': 4},
    {'map': 'geit3ctf2', 'bot_minplayers': 3},
    {'map': 'hctf3', 'bot_minplayers': 3, 'timelimit': 10},
    {'map': 'ironwood', 'bot_minplayers': 5, 'capturelimit': 3},
    {'map': 'nor3ctf1', 'bot_minplayers': 5},
    {'map': 'quartzctf1', 'bot_minplayers': 4, 'timelimit': 10},
    {'map': 'q3wctf1', 'bot_minplayers': 5},
    {'map': 'q3wctf2', 'bot_minplayers': 5},
    {'map': 'q3wcp1', 'bot_minplayers': 4, 'timelimit': 10},
    {'map': 'q3wcp9', 'bot_minplayers': 3, 'timelimit': 10},
    {'map': 'q3wcp10', 'bot_minplayers': 3, 'timelimit': 12},
    {'map': 'q3wcp11', 'bot_minplayers': 4, 'timelimIt': 10},
    {'map': 'q3wcp12', 'bot_minplayers': 3},
    {'map': 'q3wcp13', 'bot_minplayers': 4},
    {'map': 'q3wcp14', 'bot_minplayers': 3},
    {'map': 'q3wxs2', 'bot_minplayers': 3},
    {'map': 'schadctf', 'bot_minplayers': 3},
]


defaults = {
    'bot_minplayers': 3,
    'timelimit': 15,
    'capturelimit': 5,
    'fraglimit': 25,
    'map': 'q3ctf3',
}

param_keys = ['bot_minplayers', 'capturelimit', 'timelimit', 'fraglimit']

from random import shuffle

shuffle(maps)
result = []
size = len(maps)
for i in range(size):
    e = dict(defaults)
    e.update(maps[i])
    params = ' ; '.join([str('set '+key+' '+str(e[key])) for key in param_keys]) + f'; map {e["map"]}'
    print(params)
    if i < size - 1:
        result.append(str(f'set d{i} "{params} ; set nextmap vstr d{i+1}"\n'))
    else:
        result.append(str(f'set d{i} "{params} ; set nextmap vstr d0"\n'))

result.append('vstr d0')

with open("./baseq3/randomctfmaps.cfg", "w") as configfile:
    configfile.writelines(result)

