"""Repeating a beat in a loop."""

__author__ = "730393060"


# Begin your solution here...
counter: int = 0

beat: str = input("What beat do you want to repeat? ")

maximum: int = int(input("How many times do you want to repeat it? "))

final: str = ""

if maximum <= 0:
    print("No beat...")
else:
    if counter == maximum:
        final = final + beat
    else: 
        while counter < maximum:
            final = final + beat + " "
            counter = counter + 1

print(final)