#
# Typ danych: napisy (stringnapis1 = "")
#
napis1 = "ala ma kota"
napis2 = 'ala ma kota'
napis3 = 'a to jest "cudzysłów" '
napis4 = "A to jest \"cudzysłów\" "
napis5 = "Znaki specjalne: \t \n \r "

dlugosc = len(napis1)
print("Długość zmiennej napis 1 to:", dlugosc, "znaków")

# wiek = input("Podaj wiek:")
# print("Twój wiek to:", wiek.strip())

print("Hello" + "World")

# print(s.capitalize())
# print(s.upper())
# print(s.lower())
# print(s.title())
# print(s.swapcase())
# print(s.center(100))

a = "Hello"
b = "ALX"
print(f"{a} {b} {2 + 3}")

x = input("podaj wartość x")
x = int(x)
print(x, type(x))
