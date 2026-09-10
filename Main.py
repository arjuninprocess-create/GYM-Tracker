
from inside_menu.employees import employees_menu



print("GYM - Tracker")

input("press any key to get into the GYM tracker:")

print("=" * 35)
print("        MENU OF GYM _TRACKER            ")
print("=" * 35)
print("choose the number you want to go to:")

def menu():
    print("| 1.      MEMBERSHIP               | ")
    print("| 2.      EMPLOYEES                | ")
    print("| 3.      EQUIPMENTS               | ")
    print("| 4.      SERVICES                 | ")
    print("| 5.      EXIT                     | ")

employees_menu()