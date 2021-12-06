"""
will generate graphical setting configs:
high > medium > low > pro
"""

from json import load


gfx_variables = {}


target_order = ['pro', 'low', 'medium', 'high'] # interpolating from left to right

with open("gfx-variables.json", "r") as f:
    gfx_variables = load(f)



target_configs = {target: {} for target in target_order}

# for target, config in target_configs.items():
for variable, value_map in gfx_variables.items():
    print(f'{variable} : {value_map}')
    last_target = None
    last_value = None
    for target in target_order:
        if target in value_map.keys():
            print(f'found {target} in value_map')
            target_configs[target][variable] = value_map[target]
            last_target = target
            last_value = value_map[target]

        elif last_target in value_map.keys():
            print(f'found last target {last_target} in value_map')
            target_configs[target][variable] = value_map[last_target]
        else:
            raise Error(f'No target ({target}) to interpolate from.')

# write temporary settings
for target, value_list in target_configs.items():
    file_content = [f'set {key} "{value}"\n' for key, value in value_list.items()]
    with open(f'gfx-{target}-tmp.cfg', 'w') as config_file:
        config_file.writelines(file_content)


# write persistent settings which will be written to local q3config.cfg on 'exec'
for target, value_list in target_configs.items():
    file_content = [f'seta {key} "{value}"\n' for key, value in value_list.items()]
    with open(f'gfx-{target}-pers.cfg', 'w') as config_file:
        config_file.writelines(file_content)


