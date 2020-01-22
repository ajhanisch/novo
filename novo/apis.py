class BaseApi:
    def __init__(self):
        pass

class KVMApi(BaseApi):
    def __init__(self):
        super().__init__()
        print('KVMApi object.')