from console import main as console
from window import main as window

if int(input("Консоль(0) или Окно(1)? ")):
    print("Выбрано окно!")
    window()
print("Выбрана консоль!")
console()




