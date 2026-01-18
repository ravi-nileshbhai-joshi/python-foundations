# main.py 
# ------ IMPORTS --------
from storage import load_sessions
from storage import save_sessions
from analytics import compute_average
from engine import recommend
from analytics import analyze_trends
from analytics import performance_score
from analytics import update_streak
from analytics import session_summary
from datetime import datetime
from analytics import temporal_patterns
from analytics import forecast_state
from reflection import generate_reflection
from moment_engine import classify_moment
from analytics import extract_life_states, classify_life_phase
from response_gate import decide_gate
from tempo import EmotionalTempo
from presence import PresenceEngine
from voice_engine import VoiceEngine
from temporal_engine import TemporalEngine
from greetings import GreetingEngine
from intent_engine import IntentEngine
from identity_engine import IdentityEngine
from reasoning_engine import ReasoningEngine
from narrative_engine import NarrativeEngine
from cognitive_core_v3 import CognitiveCoreV3



# ------ IMPORT ENGINES -------
tempo_engine = EmotionalTempo()
presence_engine = PresenceEngine()
voice = VoiceEngine()
time_engine = TemporalEngine()
greeting_engine = GreetingEngine() 
intent_engine = IntentEngine()
identity_engine = IdentityEngine()
reasoning_engine = ReasoningEngine()
narrative_engine = NarrativeEngine()
cognitive_core = CognitiveCoreV3()




# Test mode
TEST_MODE = True


sessions = []
sessions = load_sessions()

if TEST_MODE:
    # Quick testing input
    value = input("Rate your energy (1-10): ")
    energy = int(value)

    value = input("Rate your focus (1-10): ")
    focus = int(value)

    for i in range(5):
        current_datetime = datetime.now() 
        formatted_time = current_datetime.strftime("%H:%M:%S")

        session_performance = (energy + focus) / 2

        if energy < 4 or focus < 4: 
            risk_level = "High"
        elif energy >= 7 and focus >= 7: 
            risk_level = "Low"
        else :  
            risk_level = "Medium" 

        derived_state = {
            "Perfoemance Score" : round(session_performance, 2),
            "Risk level" : risk_level
        }

        session = {
            "energy": energy,
            "focus": focus,
            "timestamp": formatted_time,
            "derived_state": derived_state
        }

        moment_signature = classify_moment(session, sessions)
        session["moment"] = moment_signature
        sessions.append(session)

else:
    # Full real input mode
    for i in range(5):
        ...
        # (keep your existing original loop here)


current_datetime = datetime.now() 
formatted_time = current_datetime.strftime("%H:%M:%S")

 # Session performance 
session_performance = (energy + focus) / 2
 
 # Risk level logic
if energy < 4 or focus < 4: 
    risk_level = "High"
elif energy >= 7 and focus >= 7: 
    risk_level = "Low"
else :  
    risk_level = "Medium" 
 
 # Derived state
derived_state = {
    "Perfoemance Score" : round(session_performance, 2)  ,
     "Risk level" : risk_level
}

 # Final session object
session = {"energy" : energy ,
            "focus" : focus ,
            "timestamp" : formatted_time,
            "derived_state" : derived_state
}
moment_signature = classify_moment(session, sessions)
session["moment"] = moment_signature
sessions.append(session)
session_include = (formatted_time)


save_sessions(sessions)

# ===================== ANALYSIS / CONTEXT ==========================

pattern_message = temporal_patterns(sessions)
avg_energy , avg_focus = compute_average(sessions)
Performance_score = performance_score(avg_energy, avg_focus)
recommendation = recommend(avg_energy, avg_focus)
trend_message = analyze_trends(sessions)
streak = update_streak(sessions)
summary = session_summary(sessions)

# --- Temporal Engine ---
time_state = time_engine.describe_time()

# --- Greeting Engine ---
greeting = greeting_engine.generate(time_state)
print("\nDestiny:", greeting)

# --- User input ---
user_text = input("\nYou:")

# --- TEMPO ---
current_tempo = tempo_engine.analyze(user_text)

# --- LIFE STATE + PHASE ---
life_states = extract_life_states(sessions)
life_phase = classify_life_phase(life_states)

# --- Forecast State ---
forecast = forecast_state(sessions)
stability = forecast.get("stability", "Stable")
burnout_risk = forecast.get("burnout", "Low")

# --- RESPONSE GATE ---
gate = decide_gate(current_tempo, life_phase, stability, burnout_risk)

# --- PRESENCE ENGINE ---
presence_state = presence_engine.decides(current_tempo, life_phase, stability, burnout_risk)
presence_text = presence_engine.presence_message(presence_state)

# --- User Intent ---
user_intent = intent_engine.detect(
    user_text,
    current_tempo, 
    life_phase, 
    presence_state,
    
)

# --- User identity --- 
user_identity = identity_engine.update(
    user_text,
    user_intent,
    current_tempo,
    stability,
    burnout_risk
)


# ========================  Reasoning Engine Block ===========================

# ------ Emotional State (from Voice Engine) ---------
emotional_state = voice.detect_emotional_state(
    user_identity, current_tempo, life_phase, user_intent
)

# ------------- Load Past Momentum (from previous turns) ---------------------
past_momentum = cognitive_core.emotional_momentum()

# ---- Destiny Reasoning Core -----
reasoning = reasoning_engine.think(
    user_text = user_text,
    tempo = current_tempo,
    life_phase = life_phase,
    intent = user_intent,
    emotional_state = emotional_state,
    identity = user_identity,
    narrative_state = {"momentum": past_momentum}
)

#--------- Extract Language Once ------------- 
language = reasoning.get("language", {})
opener = language.get("opener", "")
support = language.get("support", "")

# --------- Update Cognitive Core with THIS TURN's decision ---------------
cognitive_core.update_state(
    reasoning["understood_user_state"],
    reasoning["primary_goal"]
)

cognitive_core.update(
    reasoning["understood_user_state"],
    reasoning["primary_goal"],
    emotional_state,
    life_phase
)
# ---------------------- Compute NEW Momentum (for next turn) --------------
new_momentum = cognitive_core.emotional_momentum()

# ------------ Guidance object ----------------------
guidance = {
    "momentum": new_momentum,
    "primary_goal": reasoning["primary_goal"],
    "user_state": reasoning["understood_user_state"],
    "life_phase": life_phase
}

# --- Narrative engine ----
narrative_engine.update(user_identity, sessions, life_phase, guidance)
narrative_message = narrative_engine.generate(life_phase, current_tempo)

# --- Reflection message ---
reflection_message = generate_reflection(sessions, forecast)
reflection_message = f"{narrative_message} {reflection_message}".strip()

# ---- Voice Decide -----
voice_mode, question_style, voice_posture = voice.decide(
    current_tempo,
    life_phase,
    gate["mode"],
    presence_state,
    user_intent,
    time_state,
    user_identity
)


# --- Reasoning overrides when safety matters ---
rec_voice = reasoning.get("recommended_voice_mode")
if rec_voice and rec_voice != voice_mode:
    voice_mode = rec_voice

# --------------------- Express Message Function ---------------------
def express(message):
    # 1. Add life-arc meaning first
    message = voice.apply_narrative(
        message,
        user_identity, 
        time_state,
        allow_narrative = reasoning.get("narrative_weight", "NORMAL") != "NONE"
        )

    # 2. Now let Destiny "speak" it
    spoken = voice.speak(
        message, 
        gate["mode"], 
        current_tempo, 
        life_phase
        )

    # 3. Apply emotional presence
    toned = voice.presence_tone(
        spoken, 
        voice_mode, 
        current_tempo, 
        life_phase
        )

    # 4. Shape final human voice
    final = voice.shape(
        toned, 
        voice_mode, 
        question_style, 
        voice_posture
        )

    return final


# ---- Core message begins with Destiny's cognition ----
base_message = f"{opener} {support}".strip()

# ---- Reflection becomes contextual, not dominant ----
if reflection_message:
    base_message = f"{base_message} {reflection_message}".strip()

# ---- Presence wraps everything ----
base_message = f"{presence_text} {base_message}".strip()

# ---- Optional silence handling ----
if gate["mode"] == "QUIET_MODE":
    from silence_engine import SilenceEngine
    silence_engine = SilenceEngine()
    silence_text = silence_engine.message(gate["silence_style"])
    if silence_text.strip():
        base_message = f"{base_message} {silence_text}".strip()


# ---- FINAL VOICE OUTPUT ----
final_message = express(base_message)
print("\nDestiny:", final_message)

# --------- Debug Explanation layer --------
print("Life States:", life_states)
print("Life Phase:", life_phase)
print("Voice Mode:", voice_mode)
print("Question Style:", question_style)
print("Voice Posture:", voice_posture)
print("Emotional State:", emotional_state)
print("Reasoning:", reasoning)



















