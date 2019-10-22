from bluetooth import *
class blue_handler:
    def __init__(self):
        self.device_list={}

        self.socket_list=[]
        self.port=1
        self.target_name="syr"
        self.progress_check=3
        
    def find(self):
        # syr_1
        # syr_2
        device= discover_devices()
        for bdaddr in device:
            if lookup_name(bdaddr)[0:3]==self.target_name:
                # name get syr
                self.device_list[lookup_name(bdaddr)]=bdaddr


    def receive(self, addr):
        valid_check=3

        while valid_check>0:

        #addr need bdarr
            recv_data=None
            sock=None
            data=""

            try:
                sock=BluetoothSocket(RFCOMM )
                sock.connect((addr,self.port))
                print("connect %s"%addr)
                recv_data=""
                while recv_data == "":

                    recv_data = sock.recv(1024)
                    recv_data= recv_data +sock.recv(1024)
                print(recv_data)
            except btcommon.BluetoothError as err:
                print('An error occurred : %s ' % err)
                print("Retry %s" %valid_check)
                valid_check-=1
                sock.close()
            if recv_data != None 2**31 <= int("{0:b}".format(int(recv_data)),2)  < 2**32:
                valid_check=0
            sock.close()
        return recv_data
    # To do receive, need addr to do it

# test

