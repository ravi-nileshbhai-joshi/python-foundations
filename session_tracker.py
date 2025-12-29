import json 
sessions = []

with open("sessions.json", "r") as file:
   sessions = json.load(file)

new_sessions = []                    

for i in range(5):
     energy = int(input("Rate your energy (1-10): "))
     focus = int(input("Rate your focus (1-10): "))

     session = {"energy": energy, "focus": focus}
     sessions.append(session)
     new_sessions.append(session)

with open("sessions.json", "w") as file:
     json.dump(sessions, file, indent=4)
          
print (sessions)

total_energy = sum(s["energy"] for s in sessions)
total_focus = sum(s["focus"] for s in sessions)

avg_energy = total_energy / len(session)
avg_focus = total_focus / len(session)
if avg_energy >=7 and avg_focus >= 7:
    recommendation = "Deep work"
elif avg_energy >= 7 and avg_focus < 7:
    recommendation = "Learning / Physical"
elif avg_energy >= 4 and avg_focus >= 4:
    recommendation = "Light work"
else:
    recommendation = "Rest & Reset"

print("System Recommendation:",recommendation)
