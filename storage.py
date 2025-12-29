import json

def load_sessions():
    with open("sessions.json", "r") as file:
        return json.load(file)

def save_sessions(sessions):
    with open("sessions.json", "w") as file:
        json.dump(sessions, file, indent=4)
