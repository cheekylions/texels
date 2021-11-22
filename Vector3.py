class Vector3:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
        self._list = [x,y,z]
        
    def __getattr__(self,name):
        return getattr(self._list,name)
        
    def __repr__(self):
        return self._list
        
    def __string__(self):
        return "(" + str(x) + "," + str(y) + "," + str(z) + ")"