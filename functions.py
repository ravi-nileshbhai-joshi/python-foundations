def recommend(energy, focus):
    
 if energy >=7 and focus >=7:
    return "Deep work"
 elif energy >=7 and focus <7:
     return "Physical task or learning"
 elif energy >=4 and focus >=4:
    return "Light work"
 elif energy <4:
    return "Rest"
 else:
    return "Relax & Rest"
