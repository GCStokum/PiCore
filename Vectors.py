class v3d(object):
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

    # overload []
    def __getitem__(self, index):
        return (self.x, self.y, self.z)[index]

    # overload set []
    def __setitem__(self ,key, val):
        if (key == 0):
            self.x = val
        elif (key == 1):
            self.y = val
        elif (key == 2):
            self.z = val
        #TODO: Default should throw excetion

class v2d(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # overload []
    def __getitem__(self, index):
        return (self.x, self.y)[index]

    # overload set []
    def __setitem__(self ,key, val):
        if (key == 0):
            self.x = val
        elif (key == 1):
            self.y = val
        #TODO: Default should throw excetion
