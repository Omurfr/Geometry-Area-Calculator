
print("Area Calculator")

while True:
    print("Square Area: 1  \n"
          "Rectangle Area: 2 \n"
          "Circle Area : 3 \n"
          "Triangle Area : 4 \n"
          "Parallelogram Area : 5"
          )
    try:
        option = float(input("Enter number: "))
    except ValueError:
        print("Invalid ! Enter correct input")
        continue

    if option ==1:
        square = float(input("enter one side length : "))
        square_area = square**2
        print("square area is :", square_area)

    elif option ==2 :
        length = float(input("Enter the length : "))
        width = float(input("Enter the width :  "))
        Rectangle = length* width
        print("Rectangle is : ", Rectangle)

    elif option== 3:
        radius = float (input("Enter the radius of the circle is : "))
        pai = 3.1415
        circle_area= (radius**2)*pai
        print("Circle area is : ",circle_area )

    elif option == 4:
        Base=float(input("Enter Base : "))
        Height = float(input("Enter height : "))
        triangle_area= 0.5* Base* Height
        print("Triangle area is : " ,triangle_area )

    elif option == 5:
        base = float(input("Enter the base : "))
        height = float(input("Enter the height : "))
        Parallelogram_Area = base*height
        print("The area of Parallelogram is : ", Parallelogram_Area)
    else:
        print("Invalid Input")


    exit_option = input("Do you want to exit?(y/n):")

    if exit_option.lower() == "y":
        print("Thank you for using this calculator")
        break

    elif exit_option.lower()== "n":
         print("let's continue:")

    else:
        print("Invalid Input! try again ")


