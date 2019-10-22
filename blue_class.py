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
            print("Retry %s" %self.progress_check)
            if self.progress_check>0:
                self.progress_check -=1
                sock.close()
                self.receive(addr)
        
        sock.close()
        return recv_data
    # To do receive, need addr to do it

# test

