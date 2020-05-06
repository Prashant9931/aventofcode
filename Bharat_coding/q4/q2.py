class SecurityThroughObscurity:

    def __init__(self, input_file_name):
        self.result_string="northpole"
        self.input_file_lst=[]
        self.input_file_name=input_file_name
        self.ord_val=ord('a')

    def read_input_file(self):
        file=open(self.input_file_name)
        self.input_file_lst=[line for line in file]
        return self.input_file_lst

    def find_sector_id(self):
        self.input_file_lst=self.read_input_file()
        for line in self.input_file_lst:
            encrypted_name = line.strip().split("-")
            room = ''.join(encrypted_name[:-1])
            sector_id = int(encrypted_name[-1].split("[")[0])
            result_st = ''.join(''.join(chr(((sector_id+ (ord(j) - self.ord_val)) % 26) + self.ord_val) for j in i
                     ) for i in room)
            if self.result_string in result_st:
                print(sector_id)


obj=SecurityThroughObscurity('input.txt')
obj.find_sector_id()









