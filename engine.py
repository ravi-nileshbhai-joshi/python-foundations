def recommend(avg_energy, avg_focus):
    if avg_energy >= 7 and avg_focus >= 7:
        return "Deep Work"
    elif avg_energy >= 7 and avg_focus < 7:
        return "Learning / Physical Work"
    elif avg_energy >=4 and avg_focus >=4:
        return "Light Work"
    else:
        return "Rest & Reset"
    