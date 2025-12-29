from storage import load_sessions
from storage import save_sessions
from analytics import compute_average
from engine import recommend
from analytics import analyze_trends
from analytics import performance_score
from analytics import update_streak
from analytics import session_summary

sessions = []
sessions = load_sessions()

for i in range (5):
 energy = int(input("Rate your energy (1-10): "))
 focus = int(input("Rate you focus (1-10): "))

 session = {"energy" : energy , "focus" : focus}
 sessions.append(session)
 
save_sessions(sessions)

avg_energy , avg_focus = compute_average(sessions)
Performance_score = performance_score(avg_energy, avg_focus)
recommendation = recommend(avg_energy, avg_focus)
trend_message = analyze_trends(sessions)
streak = update_streak(sessions)
summary = session_summary(sessions)


print("Trend:", trend_message)
print("Performance Score:",  Performance_score)
print("Current Streak: ", streak)
print("Today's Summary: ", summary)





