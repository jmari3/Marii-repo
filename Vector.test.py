import unittest
from Vector import Vector, Vector3D

class TestVector(unittest.TestCase):    
    def test_vector_multiplication(self):
        vec1 = Vector(4.0,6.0,10.0)
        vec2 = Vector(1.0,3.0,7.0)
        vecToTest = Vector3D(12.0,18.0,6.0)
        self.assertEqual(vec1.vector_multiplication(vec2, vecToTest))
    def test_scal_mul(self):
        vec1 = Vector(4.0,6.0,10.0)
        vec2 = Vector(1.0,3.0,7.0)
        vecToTest = Vector3D(4.0,18.0,70.0)
        self.assertEqual(vec1.scal_mul(vec2, vecToTest))
    def test_add_by_num(self):
        vec = Vector(1.0, 3.0, 7.0)
        vecToTest = Vector3D(4.0,6.0,10.0)
        self.assertEqual(vec.add_by_num(3.0), vecToTest)
    def test_mul_by_num(self):
        vec = Vector(1.0, 3.0, 7.0)
        vecToTest = Vector3D(3.0,9.0,21.0)
        self.assertEqual(vec.mul_by_num(3.0), vecToTest)
    def test_addVecs(self):
        vec1 = Vector(4.0,6.0,10.0)
        vec2 = Vector(1.0,3.0,7.0)
        vecToTest = Vector3D(5.0,9.0,17.0)
        self.assertEqual(vec1.addVecs(vec2, vecToTest))
    

if __name__ == "__main__":
    unittest.main()