import datetime
now = datetime.datetime.now()

numberPlate = ["P11-09", "J12-32", "J62-59"] 

print('Voer hier uw nummerplaat in:')
x = input()

if x in numberPlate:

    if now.hour>=7 and now.hour<=12:
        print("Goedemorgen! Welkom bij Fonteyn Vakantieparken")
    elif now.hour>=12 and now.hour<=18:
        print("Goedemiddag! Welkom bij Fonteyn Vakantieparken")
    elif now.hour>=18 and now.hour<=23:
        print("Goedeavond! Welkom bij Fonteyn Vakantieparken")

else:
    print ("verkeerde kenteken")