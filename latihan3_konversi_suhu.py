suhu = float(input("Masukkan suhu dalam Celsius: "))

fahrenheit = (suhu * 9/5) + 32
kelvin = suhu + 273.15

print(f"Suhu dalam Fahrenheit: {fahrenheit:.2f} °F")
print(f"Suhu dalam Kelvin: {kelvin:.2f} K")
