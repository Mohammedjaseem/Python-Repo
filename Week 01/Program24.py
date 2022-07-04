class Area:
    def circle():
        pi = 3.14
        radius = float(input("\nEnter the radius of the circle: "))
        area = pi * radius * radius
        print("\nThe area of the circle is: ", area)
    
    def square():
        width = float(input("\nEnter the width/length of the square: "))
        area = width * width
        print("\nThe area of the square is: ", area)

    def rectangle():
        width = float(input("\nEnter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        area = width * height
        print("\nThe area of the rectangle is: ", area)

    def triangle():
        base = float(input("\nEnter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = (base * height) / 2
        print("\nThe area of the triangle is: ", area)


def main():
    print("""Choose Shape:
    1. Circle
    2. Square
    3. Rectangle
    4. Triangle""")
    choice = int(input("\nEnter the number of the shape you want to calculate the area of: "))
    if choice == 1:
        Area.circle()
    elif choice == 2:
        Area.square()
    elif choice == 3:
        Area.rectangle()
    elif choice == 4:
        Area.triangle()
    else:
        print("\nInvalid choice")


# class myClass inherits from Area
class MyClass(Area):
    main()
  



