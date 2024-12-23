print("hello")
a = int(input("Enter longueur: "))
b = float(input("Enter largeur: "))
surface = input("Choose rectangle or triangle: ")

if surface == "rectangle":
    print("Surface rectangle:", a * b)
elif surface == "triangle":
    print("Surface triangle:", (a * b) / 2)
else:
    print("Invalid choice !. Please choose rectangle or triangle")
