def recommend(name):
    
    energy = int(input(name + " Rate your energy (1-10:) "))
    focus = int(input(name + " Rate your focus (1-10): "))

    if energy >=7 and focus >=7:
     print(name, " Deep work")
    elif energy >=7 and focus <7:
     print(name, " Physical task or learning")
    elif energy >=4 and focus >=4:
     print(name, " Light work")
    elif energy <4:
     print(name, " Rest")
    else:
     print(name, " Relax and reset")

name = input("Enter your name: ")
print("Hello", name) 
print("from your first function")
recommend(name)
