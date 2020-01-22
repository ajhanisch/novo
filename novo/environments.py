class BaseEnvironment:
    def __init__(self):
        pass

class KVMEnvironment(BaseEnvironment):
    def __init__(self):
        super().__init__()
        print('KVMEnvironment object.')