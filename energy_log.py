energy_log = []
for i in range(5):
 energy = int(input ("Rate your energy level (1-10): "))
 energy_log.append(energy)
total = sum(energy_log)
length = len(energy_log)
average = total / length
highest = max(energy_log)
lowest = min(energy_log)
print ("total", total, "length", length, "average", average, "highest",  highest, "lowest", lowest)
