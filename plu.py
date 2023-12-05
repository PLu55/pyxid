import pyxid2

 

 
class CedrusKeyboardDevice(object):
    """A Singelton class that handle the communication with the keyboard.
    Users should not use this class directly, it's used by CedrusKeyboard class.
    There can only be one instance of this class (a Singelton)
    """
    __devices = pyxid2.get_xid_devices()
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CedrusKeyboardDevice, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.device = None
        for dev in CedrusKeyboardDevice.__devices:
            if dev.device_name == 'Cedrus RB-740':
                self.device = dev
                break
        if self.device is None:
            raise Exception('No Cedrus keyboard found!')

if __name__ == '__main__':
    ck = CedrusKeyboard()
    while(True):
        try:
            print(f'Responce: {ck.getResponse()}')
        except TimeOutException:
            print('TimeOut')


