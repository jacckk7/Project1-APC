#####################################################################################################
###################################### Projejo 1 de APC #############################################
################################## Breno Costa Avelino Lima #########################################
#####################################################################################################


#####################################################################################################
####################################### library import ##############################################
#####################################################################################################

from copy import deepcopy


#####################################################################################################
#################################### functions definition ###########################################
#####################################################################################################

def configuracao():
    i = 0
    config = []
    while True:
        config.append(input().split())
        if config[i] == ['--ATENDIMENTO']:
            config.pop(i)
            break
        elif config[i] == ['--CONFIGURACAO']:
            config.pop(i)
            continue
        i += 1
    
    for j in range(len(config)):
        config[j][1] = int(config[j][1])
        config[j][2] = int(config[j][2])
        
    return config

def comando_menos_um(config, people_count):
    print('Restaurante fechado.', 'Balanco final de mesas:', sep = '\n')
    config = sorted(config, key = lambda x:x[2])
    config = sorted(config, key = lambda x:x[0])
    i = 0
    for i in range(len(config)):
        if i == 0:
            print(f'{config[0][0]}:') 
            print(f' {config[0][1]} mesas de {config[0][2]} cadeiras.')
        elif config[i][0] == config[i - 1][0]:
            print(f' {config[i][1]} mesas de {config[i][2]} cadeiras.')
        else:
            print(f'{config[i][0]}:')
            print(f' {config[i][1]} mesas de {config[i][2]} cadeiras.')
    print(f'Um total de {people_count} pessoas visitaram o restaurante hoje.')
    print('Bom descanso!')

def comando_um(config_hold, time_hold, count_people):
    request = input().split()
    n_people = int(request[4])
    count_people += n_people
    name_area = request[8]
        
    i = 0
    chairs = -1
    for i in range(len(config_hold)):
        if name_area == config_hold[i][0] and config_hold[i][1] > 0:
            if chairs == -1 and config_hold[i][2] >= n_people:
                chairs = i
            elif config_hold[i][2] >= n_people and config_hold[i][2] < config_hold[chairs][2]:
                chairs = i
        
    if chairs != -1:
        config_hold[chairs][1] -= 1
        print(f'Um grupo de {n_people} pessoas ocupou uma mesa de {config_hold[chairs][2]} lugares na area {config_hold[chairs][0]}.')
        time_hold.append([(2 * n_people + 2), chairs, n_people])
        config_hold[chairs][3] += n_people
    else:
        print('Nao foi possivel levar o grupo de clientes para uma mesa.')
        count_people -= n_people
        
    j = 0
    for j in range(len(time_hold)):
        time_hold[j][0] -= 1
        if time_hold[j][0] == 0:
            config_hold[time_hold[j][1]][1] += 1
            config_hold[time_hold[j][1]][3] -= time_hold[j][2]
        
    return count_people
        
def comando_dois(config, config_hold, time_hold):
    config_sort = deepcopy(config)
    config_hold_sort = deepcopy(config_hold)
    
    config_sort = sorted(config, key = lambda x:x[0])
    config_hold_sort = sorted(config_hold, key = lambda x:x[0])
    
    i = 0
    name_area = config_sort[0][0]
    count_tables1 = 0
    count_tables2 = 0
    for i in range(len(config_sort)):
        if i + 1 == len(config_sort) and name_area == config_sort[i][0]:
            count_tables1 += config_sort[i][1]
            count_tables2 += config_hold_sort[i][1]
            print(f'{name_area}: ({count_tables1 - count_tables2} de {count_tables1} mesas)')
        elif i + 1 == len(config_sort) and name_area != [i][0]:
            print(f'{name_area}: ({count_tables1 - count_tables2} de {count_tables1} mesas)')
            name_area = config_sort[i][0]
            count_tables1 = config_sort[i][1]
            count_tables2 = config_hold_sort[i][1]
            print(f'{name_area}: ({count_tables1 - count_tables2} de {count_tables1} mesas)')
        elif name_area == config_sort[i][0]:
            count_tables1 += config_sort[i][1]
            count_tables2 += config_hold_sort[i][1]
        else:
            print(f'{name_area}: ({count_tables1 - count_tables2} de {count_tables1} mesas)')
            name_area = config_sort[i][0]
            count_tables1 = config_sort[i][1]
            count_tables2 = config_hold_sort[i][1]
        
    j = 0
    for j in range(len(time_hold)):
        time_hold[j][0] -= 1
        if time_hold[j][0] == 0:
            config_hold[time_hold[j][1]][1] += 1
            config_hold[time_hold[j][1]][3] -= time_hold[j][2]

def comando_tres(config, config_hold, time_hold):
    config_sort = deepcopy(config)
    config_hold_sort = deepcopy(config_hold)
    
    config_sort = sorted(config, key = lambda x:x[0])
    config_hold_sort = sorted(config_hold, key = lambda x:x[0])
    
    i = 0
    name_area = config_sort[0][0]
    count_chairs1 = 0
    count_chairs2 = 0
    for i in range(len(config_sort)):
        if i + 1 == len(config_sort) and name_area == config_sort[i][0]:
            count_chairs1 += (config_sort[i][1] * config_sort[i][2])
            count_chairs2 += config_hold_sort[i][3]
            print(f'{name_area}: ({count_chairs2} de {count_chairs1} pessoas)')
        elif i + 1 == len(config_sort) and name_area != config_sort[i][0]:
            print(f'{name_area}: ({count_chairs2} de {count_chairs1} pessoas)')
            name_area = config_sort[i][0]
            count_chairs1 = (config_sort[i][1] * config_sort[i][2])
            count_chairs2 = config_hold_sort[i][3]
            print(f'{name_area}: ({count_chairs2} de {count_chairs1} pessoas)')
        elif name_area == config_sort[i][0]:
            count_chairs1 += (config_sort[i][1] * config_sort[i][2])
            count_chairs2 += config_hold_sort[i][3]
        else:
            print(f'{name_area}: ({count_chairs2} de {count_chairs1} pessoas)')
            name_area = config_sort[i][0]
            count_chairs1 = (config_sort[i][1] * config_sort[i][2])
            count_chairs2 = config_hold_sort[i][3]
        
    j = 0
    for j in range(len(time_hold)):
        time_hold[j][0] -= 1
        if time_hold[j][0] == 0:
            config_hold[time_hold[j][1]][1] += 1
            config_hold[time_hold[j][1]][3] -= time_hold[j][2]

def comando_quatro(config, config_hold, time_hold):
    request = input().split()
    what_to_do = request[1]
    tables = int(request[3])
    chairs = int(request[6])
    name_area = request[11]
    
    add = 0
    if what_to_do == 'adicionar':
        for i in range(len(config)):
            if name_area == config[i][0] and chairs == config[i][2]:
                config[i][1] += tables
                config_hold[i][1] += tables
                add += 1
        if add == 0:
            config.append([name_area, tables, chairs])
            config_hold.append([name_area, tables, chairs, 0])
        print(f'{tables} mesas de {chairs} cadeiras adicionadas com sucesso na area {name_area}.')
    else:
        for i in range(len(config)):
            if name_area == config[i][0] and chairs == config[i][2]:
                config[i][1] -= tables
                config_hold[i][1] -= tables
        print(f'{tables} mesas de {chairs} cadeiras removidas com sucesso na area {name_area}.')
        
    j = 0
    for j in range(len(time_hold)):
        time_hold[j][0] -= 1
        if time_hold[j][0] == 0:
            config_hold[time_hold[j][1]][1] += 1
            config_hold[time_hold[j][1]][3] -= time_hold[j][2]
            

#####################################################################################################
######################################## main function ##############################################
#####################################################################################################

people_count = 0

config = configuracao()

config_hold = deepcopy(config)
for l in range(len(config_hold)):
    config_hold[l].append(0)

time_hold = []

while True:
    comando = int(input())
    if comando == -1:
        comando_menos_um(config, people_count)
        break
    elif comando == 1:
        people_count = comando_um(config_hold, time_hold, people_count)
    elif comando == 2:
        comando_dois(config, config_hold, time_hold)
    elif comando == 3:
        comando_tres(config, config_hold, time_hold)
    else:
        comando_quatro(config, config_hold, time_hold)