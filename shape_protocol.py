from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable
from typing import Union
import math


@runtime_checkable
class Labeled(Protocol):
    label: str


class Shape(ABC, Labeled):
    def __init__(self):
        self.label: Union[str, None] = None

    @abstractmethod
    def area(self):
        """Compute the area of the shape."""
        pass
  
class Circle(Shape):
    def __init__(self,radius):
        Shape.__init__(self)
        self.radius = radius
        self.label  = "c"

    def area(self)->float:
        return math.pi * self.radius * self.radius
    

class Triangle(Shape): 
    def __init__(self,side1,side2,side3):
        super().__init__()
        self.side1:float = side1
        self.side2:float = side2
        self.side3:float = side3
        self.label = "t"


    def area(self):
        # Heron's Formula:
        #Area = Square root of√s(s - a)(s - b)(s - c) where s is half the perimeter, or (a + b + c)/2.
        s1: float = self.side1
        s2: float = self.side2
        s3: float = self.side3
        p:float = (s1+s2+s3)/2
        return math.sqrt(p*(p-s1)*(p-s2)*(p-s3))
    



def main():
    shapes = [Circle(3), 
              Triangle(3, 4, 6)]
    
    for shape in shapes:
        print(f"Is an instance of Labeled: {isinstance(shape, Labeled)}")
        print(f"{shape.label}\n")

if __name__ == '__main__':
    main()


