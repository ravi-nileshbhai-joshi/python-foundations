sessions = []
for i in range(5):
     energy = int(input("Rate your energy (1-10): "))
     focus = int(input("Rate your focus (1-10): "))
     session = {}
     session["energy"] = energy
     session["focus"] = focus
     sessions.append(session)
print(sessions)
