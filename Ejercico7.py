class Estrella:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "(" + self.x + "," + self.y + "," + self.z +")"

    def galaxia(self):
        if self.x > 0 and self.y > 0 and self.z > 0:
            return print("cuadrante I")
        elif self.x < 0 and self.y < 0 and self.z < 0:
            return print("Cuadrante II")
        else:
            return print("Cuadrante III")
        
A = Estrella(1,1,1)
A.galaxia()