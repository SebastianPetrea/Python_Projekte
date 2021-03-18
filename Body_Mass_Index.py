"""Body-Mass-Index"""
korpergewicht = float(input("Geben Sie ihren Körpergewicht ein:"))
korpergrosse = float(input("Geben Sie ihre Körpergröße in Meter an:"))
ergebnis = (korpergrosse * korpergrosse) #/ korpergewicht
end_ergebnis = korpergewicht / ergebnis
print("Sie haben eine BMI von",end_ergebnis)
