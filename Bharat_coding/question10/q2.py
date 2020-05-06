from collections import defaultdict


class BalanceBots:
    def __init__(self, file_name):
        self.microchips_value = [17, 61]
        self.bots_lst = defaultdict(list)
        self.result=defaultdict(list)
        self.filename = file_name

    def read_input(self):
        f = open(self.filename)
        instructions_string = []
        for line in f:
            instructions_string.append(line)
        return instructions_string

    def is_proceed(self, temp_bot: str):
        if len(self.bots_lst[temp_bot]) == 2:
            return 1
        else:
            return 0

    def is_done(self, temp_bot: str):
        if self.bots_lst[temp_bot] == self.microchips_value:
            return 1

    def handle_robot(self, input_string: list):
        for string in input_string:
            keys = string.split()
            if keys[0] == 'value':
                val, bot = int(keys[1]), keys[-1]
                self.bots_lst[bot].append(val)
                self.bots_lst[bot].sort()
                if self.bots_lst[bot] == self.microchips_value:
                    break

            elif keys[0] == 'bot':
                bot = keys[1]
                if self.is_proceed(bot):
                    if keys[5] == 'bot':
                        self.bots_lst[keys[6]].append(self.bots_lst[bot][0])
                        self.bots_lst[keys[6]].sort()
                    else:
                        self.result[keys[6]].append(self.bots_lst[bot][0])

                    if keys[-2] == 'bot':
                        self.bots_lst[keys[-1]].append(self.bots_lst[bot][1])
                        self.bots_lst[keys[-1]].sort()
                    else:
                        self.result[keys[-1]].append(self.bots_lst[bot][0])

                else:
                    input_string.append(string)

            else:
                raise Exception("Invalid input")
        return self.result


if __name__ == "__main__":
    code_obj = BalanceBots("input.txt")
    input_file = code_obj.read_input()
    output = code_obj.handle_robot(input_file)
    print(output['0'][0] * output['1'][0] * output['2'][0])
