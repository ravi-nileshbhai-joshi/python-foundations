def compute_average(sessions):
    total_energy = sum(s["energy"] for s in sessions)
    total_focus = sum(s["focus"] for s in sessions)

    avg_energy = total_energy / len(sessions)
    avg_focus = total_focus / len(sessions)

    return avg_energy, avg_focus
def analyze_trends(sessions):
    if len(sessions) < 5:
        return "Not enough data yet."
    
    recent = sessions[-5:]
    avg_energy = sum(s["energy"] for s in recent) / 5
    avg_focus = sum(s["focus"] for s in recent) / 5

    if avg_energy < 4 or avg_focus < 4:
        return "Risk of burnout. Take recovery time."
    elif avg_energy > 7 and avg_focus > 7:
        return "Strong performance trend."
    else:
        return "Stable performance"
    
def performance_score(avg_energy, avg_focus):
    return round((avg_energy + avg_focus) / 2, 2)

def update_streak(sessions):
    streak = 0
    for s in reversed(sessions):
        if s ["energy"] >= 6 and s["focus"] >=6:
            streak += 1
        else:
            break
        return streak

def session_summary(sessions):
    today = sessions[-5:]
    avg_energy = sum(s["energy"] for s in today) / 5
    avg_focus = sum(s["focus"] for s in today) / 5

    best = max(today, key=lambda s: s["energy"] + s["focus"])
    worst = min(today, key=lambda s: s["energy"] + s["focus"])

    return{
        "avg_energy" : round(avg_energy, 2),
        "avg_focus" : round(avg_focus, 2),
        "best" : best,
        "worst" : worst
    }
