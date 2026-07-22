class Circle :
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self ):
        self.Radius = float(input("Enter radius of circle : "))
    

    def CalculateArea(self ):
        self.Area = self.Radius * self.Radius * Circle.PI 
        
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print ("Radius : ", self.Radius)
        print("Area : ", self.Area)
        print("Cicumference : ",self.Circumference)
        print()

def main():

    size = int(input("Enter number of circles : "))
    Objects = []

    for i in range(size):
        print("\nEnter details for Circle", i +1)

        obj = Circle()

        obj.Accept()
        obj.CalculateArea()
        obj.CalculateCircumference()
        Objects.append(obj)

    print("\n--------Circle Details--------\n")

    for obj in Objects : 
        obj.Display()

if __name__ == "__main__":
    main()