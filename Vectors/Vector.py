from dataclasses import dataclass, is_dataclass

def determinant2D(matrix):
    isSquareMatrix = len(matrix) == 2 and len(matrix[0]) == 2 and len(matrix[1]) == 2 
    assert isSquareMatrix 
    return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

@dataclass
class Vector3D:
    x: float 
    y: float
    z: float


class Vector():
    def __init__(self, x, y, z):
        assert isinstance(x, float)
        assert isinstance(y, float)
        assert isinstance(z, float)
        self.vec = Vector3D(x, y, z)
    
    def vector_multiplication(self, vec):
        assert isinstance(vec, Vector3D)
        
        
        m1 = [
            [self.vec.y, self.vec.z],
            [vec.y, vec.z]
            ]

        m2 = [
            [self.vec.x, self.vec.z],
            [vec.x, vec.z]
            ]

        m3 = [
            [self.vec.x, self.vec.y],
            [vec.x, vec.y]
            ]

        return Vector3D(determinant2D(m1), -determinant2D(m2), determinant2D(m3))

    def scal_mul(self,vec):
        assert isinstance(vec, Vector3D)
        return self.vec.x * vec.x + self.vec.y + vec.y + self.vec.z + vec.z

    def add_by_num(self,number):
        assert isinstance(number, float), "Only Vector3D"
        return Vector3D(self.vec.x+ number,self.vec.y+ number,self.vec.z+ number,)

    def mul_by_num(self,number):
        assert isinstance(number, float)
        return Vector3D(self.vec.x*number,self.vec.y*number,self.vec.z*number,)

    def addVecs(self,vec):
        assert isinstance(vec, Vector3D)
        return Vector3D(self.vec.x+vec.x,self.vec.y+vec.y,self.vec.z+vec.z,)

    
vec1 = Vector(4.0, 6.0, 10.0) 
vec2 = (1.0,3.0,7.0)
print(Vector.vector_multiplication(vec2))