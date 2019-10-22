class data_make:
    def __init__(self):
        self.temp_min=0
        self.light_min=0
        self.temp_th=5
        self.light_th=0


    def data_masking(self,rough):
        tmp="{0:b}".format(int(rough))
        emergency=int(tmp[1],2)
        sleep_state=int(tmp[2:4],2)
        tempor=int(tmp[4:11],2)
        tempor= tempor/4+10
        humid=int(tmp[11:18],2)
        light=int(tmp[18:25],2)
        sound=int(tmp[25:],2)

        return [emergency,sleep_state,tempor,humid,light,sound]

    def data_min_making(self, dict):
        # dict={name:[data]}
        self.temp_min=0
        self.light_min=0
        for name in dict.keys():
            self.temp_min += dict.get(name)[2]
            self.light_min+=dict.get(name)[4]

        self.temp_min=self.temp_min/len(dict.keys())
        self.light_min = self.light_min / len(dict.keys())

    def state_make(self,name,list):
        #list=[data]
        state=name
        if abs(list[2]-self.temp_min)>self.temp_th:
            list[1] = 3
        if abs(list[4]-self.light_min)>self.light_th:
            list[4]= 1 if list[4]-self.light_min >0 else 0
        for data in list:
            state= state+" "+str(data)
        return state

# test code
# a=data_make()
# data={"syr1":[0,0,20,40,30,40],"syr2":[0,0,30,20,30,40],"syr3":[0,0,38,20,30,40]}
# a.data_min_making(data)

