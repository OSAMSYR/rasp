from bluetooth import *
class blue_handler:
    def __init__(self):
        self.device_list={}

        self.socket_list=[]
        self.port=1
        self.target_name="syr"
        
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
            print("done")
            data=""
            recv_data = sock.recv(1024)
            recv_data= recv_data +sock.recv(1024)
            print(recv_data)
        except btcommon.BluetoothError as err:
            print('An error occurred : %s ' % err)
            pass

        sock.close()
        return data

    # To do receive, need addr to do it

# test
a=blue_handler()

print(a.receive("98:D3:71:FD:7C:04"))
