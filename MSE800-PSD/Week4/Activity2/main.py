from calculation import RectangleLand

def main():
    print("Enter dimension of the land")

    try:
        l = float(input("Enter the length of the land: "))
        w = float(input("Enter the width of the land: "))

        if l<=0 or w<=0:
            print("invalid dimensions")
            return

        land=RectangleLand(l,w)

        area = land.calculate_area()
        perimeter = land.calculate_perimeter()

        # Output
        print("\n--- Results ---")
        print(f"Total Area: {area:.2f} square units")
        print(f"Total Perimeter: {perimeter:.2f} units")

    except ValueError:
        print("Enter Valid Dimensions")
        
if __name__ == "__main__":
    main()