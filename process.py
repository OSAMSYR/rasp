class data_make:
    def __init__(self):
        self.temp_min=0
        self.hummid_min=0
        self.light_min=0
    def data_masking(self,rough):
        tmp="{0:b}".format(int(rough))
        print(tmp)
        emergency=int(tmp[1],2)
        sleep_state=int(tmp[1:3],2)
        tempor=int(tmp[3:10],2)
        humid=int(tmp[10:17],2)
        light=int(tmp[17:24],2)
        sound=int(tmp[24:],2)

        return [emergency,sleep_state,tempor,humid,light,sound]

