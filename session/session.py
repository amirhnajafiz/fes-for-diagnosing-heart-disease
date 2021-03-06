from decimal import Decimal


"""
Session class.
    - fields:
        - range: type list [begin, end, middle]
        - base function left (a, b)
        - base function right (a , b)
        - right range value
        - left range value

"""
class Session:
    def __init__(self):  # constructor
        # session range
        self.range = [0, 0, 0]
        # session base functions
        self.lbf = dict(a=1, b=0)
        self.rbf = dict(a=1, b=0)
        # session range values
        self.rrv = 0
        self.lrv = 0
    
    def Range(self, newRange):  # setting the session range
        self.range = newRange

        self.__left_function(lin_equ((self.range[0], 0), (self.range[2], 1)))
        self.__right_function(lin_equ((self.range[2], 1), (self.range[1], 0)))

        return self
    
    def __left_function(self, value):  # setting the left function 
        self.lbf.update(dict(a=value[0], b=value[1]))

        return self

    def __right_function(self, value):  # setting the right function
        self.rbf.update(dict(a=value[0], b=value[1]))

        return self 

    def LeftValue(self, value):  # setting the left value range
        self.lrv = value

        return self
    
    def RightValue(self, value):  # setting the right value range
        self.rrv = value

        return self
    
    def CheckPoint(self, x, y):  # check if a given point is inside the session or not
        return (x >= self.range[0] and x <= self.range[1]) and (self.Input(x) >= y and y >= 0)

    def Input(self, x):  # calculating the output of session
        # check the single value sessions
        if self.range[0] == self.range[1]:
            if self.range[0] == x:
                return 1
            else:
                return 0
        # check the range value sessions
        if x <= self.range[0]:  # left 
            return self.lrv
        elif x > self.range[0] and x < self.range[2]:  # middle left
            return self.lbf.get('a') * Decimal(x) + self.lbf.get('b')
        elif x >= self.range[2] and x < self.range[1]:  # middle right
            return self.rbf.get('a') * Decimal(x) + self.rbf.get('b')
        elif x >= self.range[1]:  # right
            return self.rrv

    def Info(self):  # getting the info of our session
        return dict(
            Range=self.range,
            LeftBaseFunction=self.lbf,
            RightBaseFunction=self.rbf,
            LeftRangeValue=self.lrv,
            RightRangeValue=self.rrv
        )


def lin_equ(l1, l2):  # calculating the line from two points
    if l2[0] - l1[0] == 0:
        return 0, 1
    m = Decimal((l2[1] - l1[1])) / Decimal(l2[0] - l1[0])
    c = (Decimal(l2[1]) - (m * Decimal(l2[0])))
    return m, c
