from blue_class import blue_handler
from process import data_make
class main:
    def __init__(self):
        self.device_addr={}

        self.rough_data={}
        self.masked_data={}
        self.state=""
        # key is name and value is list of data

        self.blue_handle=blue_handler()
        self.data_handle=data_make()

    def initial_process(self):
        #self.blue_handle.find()
        self.blue_handle.device_list={"SYR_2":"98:D3:71:FD:7C:04","SYR_3":"98:D3:91:FD:84:13"}
        self.device_addr=self.blue_handle.device_list
        # find complete


    def data_processing(self):
        # get data on device_addr
        for name in self.device_addr.keys():
            self.rough_data[name]= self.blue_handle.receive(self.device_addr.get(name))
            print(self.rough_data)
            self.masked_data[name]=self.data_handle.data_masking(self.rough_data.get(name))
            print(self.masked_data)

        self.data_handle.data_min_making(self.masked_data)

    def data_save(self):
        state_string=""
        for name in self.device_addr.keys():
            file_name="./data/"+name+".txt"
            data_string=""
            state_string=self.data_handle.state_make(name,self.masked_data.get(name)) + "\n"
            for val in self.masked_data.get(name):
                data_string=data_string+" " + val
            with open(file_name, "a+") as f:
                f.write(data_string)
        state_string



    def start(self):

        self.initial_process()
        self.data_processing()
        self.data_save()





# test code
# a=main()
# a.start()


        
