from collections import defaultdict


def read_input(filename):
    f = open(filename)
    instructions_string = []
    for line in f:
        instructions_string.append(line)
    return instructions_string


def is_proceed(temp_bots: list, temp_bot: str):
    if len(temp_bots[temp_bot]) == 2:
        return 1
    else:
        return 0


def is_done(temp_bots: list, temp_bot: str):
    if temp_bots[temp_bot] == VICTORY:
        return 1


def handle_robot(input_string: list, bots_lst: defaultdict):
    for string in input_string:
        keys = string.split()
        if keys[0] == 'value':
            val, bot = int(keys[1]), keys[-1]
            bots_lst[bot].append(val)
            bots_lst[bot] = sorted(bots_lst[bot])
            if bots_lst[bot] == VICTORY:
                break

        elif keys[0] == 'bot':
            bot = keys[1]
            if is_proceed(bots_lst, bot):
                if keys[5] == 'bot':
                    bots_lst[keys[6]].append(bots_lst[bot][0])
                    bots_lst[keys[6]] = sorted(bots_lst[keys[6]])
                    if is_done(bots_lst, bot):
                        break

                if keys[-2] == 'bot':
                    bots_lst[keys[-1]].append(bots_lst[bot][1])
                    bots_lst[keys[-1]] = sorted(bots_lst[keys[-1]])
                    if is_done(bots_lst, bot):
                        break
            else:
                input_string.append(string)

        else:
            raise Exception('bad command')
    return bots_lst


VICTORY = [17, 61]
bots = defaultdict(list)
input_file = read_input('input.txt')
bots = handle_robot(input_file, bots)
for i, b in bots.items():
    if sorted(b) == VICTORY:
        print(i, b)
