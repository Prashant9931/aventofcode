from collections import Counter


class SecurityThroughObscurity:

    def __init__(self, input_file_name):
        self.result_sum=0
        self.input_file_lst=[]
        self.input_file_name=input_file_name

    def read_input_file(self):
        file=open(self.input_file_name)
        self.input_file_lst=[line for line in file]
        return self.input_file_lst

    def get_result(self):
        return self.result_sum

    def calculate_sum_for_real_rooms(self):
        self.input_file_lst=self.read_input_file()
        for line in self.input_file_lst:
            encrypted_name = line.strip().split("-")
            room = ''.join(encrypted_name[:-1])
            sector_id = int(encrypted_name[-1].split("[")[0])
            checksum = encrypted_name[-1].split("[")[1].replace("]", "")
            rooms=''.join([st[0] for st in sorted(Counter(room).most_common(),
                                                  key=lambda x: (-x[1], x[0]))])[0:5]
            if rooms==checksum:
                self.result_sum+=sector_id


obj=SecurityThroughObscurity('input.txt')
obj.calculate_sum_for_real_rooms()
result_sum=obj.get_result()
print(result_sum)


