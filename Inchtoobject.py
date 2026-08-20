class Dimension:
    def __init__(self, inches):
        if inches >= 0:
            self.feet = inches // 12
            self.inches = inches % 12
        else:
            self.feet = -1
            self.inches = -1
 
d1 = Dimension(25)
print(d1.feet)    # Output: 2
print(d1.inches)  # Output: 1
 
d2 = Dimension(-1)
print(d2.feet)    # Output: -1
print(d2.inches)  # Output: -1
