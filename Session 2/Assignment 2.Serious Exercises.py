
hei_cm = int(input("Height (cm) ="))
mass_kg = int(input("Weight (kg) ="))

hei_m = hei_cm / 100
                
bmi = mass_kg/(hei_m * hei_m)

if bmi <16:
    print ("Severely underweight")
elif  bmi <= 18.5:
    print ("Underweight")
elif  bmi <= 25:
    print ("Normal")
elif  bmi <= 30:
    print ("Overweight")
else:
    print ("Obese")
             

