class Rectangle:
    def__init__(self, length, width):   # Contructor
        self.length = length
        self.width = width
        
    def area(self):   # Class function
        return self.length * self.width
    
    def perimiter(self):
        return 2 * self.length + self.width
    
length = int(input("Enter length: "))
width = int(input("Enter Width: "))
r = Rectangle(length, width)   # Call class constructor to make new instance
print("Area:", r.area())
print("Perimiter:", r.perimiter())
r,length *= 2
print("Lenth * 2", r.length)

input()