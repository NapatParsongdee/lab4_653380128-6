# Lab#4 - Boundary Value Analysis
# SC353201 Software Quality Assurance
# Semester 1/2567
# Instructor: Chitsutha Soomlek
# นายณภัทร ประสงค์ดี 653380128-6
import pytest
import sys
sys.path.insert(0, r'C:\Users\GraphicDesign\Desktop\Lab4_653380128-6\quadrilateral\source')

from findQuadrilateral import Quadrilateral

def test_run(top, left_side, bottom, right_side, expected_type):
   quad = Quadrilateral(top, left_side, bottom, right_side)
   assert quad.classify() == expected_type

def testcase_1():
    test_run(100, 100, 100, 100, "Square")

def testcase_2():
   test_run(100, 100, 100, 0, "Trapezoid")
    
def testcase_3():
    test_run(100, 100, 100, 1, "Trapezoid")
    
def testcase_4():
    test_run(100, 100, 100, 2, "Trapezoid")
    
def testcase_5():
    test_run(100, 100, 100, 199, "Trapezoid")
    
def testcase_6():
    test_run(100, 100, 100, 200, "Trapezoid")
    
def testcase_7():
    test_run(100, 100, 100, 201, "Trapezoid")
    
def testcase_8():
    test_run(100, 100, 0, 100, "Trapezoid")
    
def testcase_9():
    test_run(100, 100, 1, 100, "Trapezoid")
    
def testcase_10():
    test_run(100, 100, 2, 100, "Trapezoid")
    
def testcase_11():
    test_run(100, 100, 199, 100, "Trapezoid")
    
def testcase_12():
    test_run(100, 100, 200, 100, "Trapezoid")
    
def testcase_13():
    test_run(100, 100, 201, 100, "Trapezoid")
    
def testcase_14():
    test_run(100, 0, 100, 100, "Trapezoid")
    
def testcase_15():
    test_run(100, 1, 100, 100, "Trapezoid")
    
def testcase_16():
    test_run(100, 2, 100, 100, "Trapezoid")
    
def testcase_17():
    test_run(100, 199, 100, 100, "Trapezoid")
    
def testcase_18():
    test_run(100, 200, 100, 100, "Trapezoid")
    
def testcase_19():
    test_run(100, 201, 100, 100, "Trapezoid")

def testcase_20():
   test_run(0, 100, 100, 100, "Trapezoid")
    
def testcase_21():
    test_run(1, 100, 100, 100, "Trapezoid")
    
def testcase_22():
    test_run(2, 100, 100, 100, "Trapezoid")
    
def testcase_23():
    test_run(199, 100, 100, 100, "Trapezoid")
    
def testcase_24():
    test_run(200, 100, 100, 100, "Trapezoid")
    
def testcase_25():
    test_run(201, 100, 100, 100, "Trapezoid")
    


if __name__ == "__main__":
    pytest.main()