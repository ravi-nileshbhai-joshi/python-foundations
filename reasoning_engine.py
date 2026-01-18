# reasoning_engine.py
from cognitive_core_thinking import CognitiveCore
from language_bank import LANGUAGE_BANK
import random

class ReasoningEngine:
    def __init__(self):
        self.core = CognitiveCore()

    # ---------- User Text Understanding ----------
    def interpret_user_text(self, text: str):
        t = text.lower()

        return {
            "distress": any(w in t for w in ["tired", "stuck", "lost", "hard", "can't", "broken", "empty", "not okay"]),
            "gratitude": any(w in t for w in ["thanks", "thank", "appreciate", "grateful"]),
            "hope": any(w in t for w in ["better", "improving", "good", "ready", "strong"]),
            "uncertainty": any(w in t for w in ["confused", "unsure", "maybe", "don't know"])
        }
    
    # ---------- Select Language -------------------
    def select_language(self, reasoning):
        goal = reasoning["primary_goal"]
        bank = LANGUAGE_BANK.get(goal, {})

        openers = bank.get("openers") or [""]
        support_lines = bank.get("support") or [""]

        opener = random.choice(openers)
        support = random.choice(support_lines)

        return {
            "opener": opener,
            "support": support
        }


    # ---------- Core Cognitive Engine ----------
    def think(self, *, user_text, tempo, life_phase, intent, emotional_state, identity, narrative_state):

        text_signal = self.interpret_user_text(user_text)
        meaning = self.core.compress(user_text, text_signal)
        state = self.core.synthesize(meaning, emotional_state, life_phase)
        guidance = self.core.guide(state)
        momentum = (
            narrative_state.get("momentum", "UNKNOWN")
            if narrative_state is not None
            else "UNKNOWN"
        )


        def attach_language(self,decision):
            decision["language"] = self.select_language(decision)
            return decision

        # Guaranteed complete decision schema
        decision = {
            "primary_goal": "CLARIFY",
            "safety_level": "MEDIUM",
            "emotional_pressure": "MEDIUM",
            "recommended_voice_mode": "GUIDE",
            "allow_silence": False,
            "narrative_weight": "NORMAL",
            "reflection_weight": "MEDIUM",
            "understood_user_state": "NEUTRAL",
            "next_conversation_focus": "UNDERSTANDING"
        }

        # ------------ Apply Cognitive Guidance ----------------
        decision.update({
            "primary_goal": guidance["goal"],
            "recommended_voice_mode": guidance["voice"],
            "allow_silence": guidance["allow_silence"]
        })

        # -------------------------------------
        # 1. Stability & Safety First
        # -------------------------------------
        if (
            life_phase in ["STUCK", "DECLINING"]
            or intent in ["SHARING_BURDEN", "NEEDING_GROUNDING"]
            or emotional_state in ["HEAVY", "FRAGILE"]
            or text_signal["distress"]
        ):
            decision.update({
                "primary_goal": "STABILIZE",
                "safety_level": "HIGH",
                "emotional_pressure": "HIGH",
                "recommended_voice_mode": "ANCHOR",
                "allow_silence": True,
                "narrative_weight": "LIGHT",
                "reflection_weight": "HIGH",
                "understood_user_state": "DISTRESSED",
                "next_conversation_focus": "SAFETY"
            })
            decision["language"] = self.select_language(decision)
            return decision
        
        #------------------------------------------
        # Momentum Override Layer
        # -----------------------------------------
        if momentum == "SINKING":
            decision.update ({
                "primary_goal" : "STABILIZE",
                "recommended_voice_mode": "ANCHOR",
                "narrative_weight": "LIGHT",
                "reflection_weight": "HIGH",
                "understood_user_state": "OVERWHELMED"
            }) 

        elif momentum in ["RISING", "ACCELERATING"] and decision["primary_goal"] != "STABILIZE":
            decision.update({
                "primary_goal": "ENCOURAGE",
                "recommended_voice_mode": "FLOW"
            })



        # --------------------------------------
        # 2. Growth & Momentum Layer
        # --------------------------------------
        if life_phase == "BUILDING" and emotional_state in ["FOCUSED", "CONFIDENT"] and text_signal["hope"]:
            decision.update({
                "primary_goal": "ENCOURAGE",
                "safety_level": "MEDIUM",
                "emotional_pressure": "LOW",
                "recommended_voice_mode": "FLOW",
                "allow_silence": False,
                "narrative_weight": "NORMAL",
                "reflection_weight": "MEDIUM",
                "understood_user_state": "MOTIVATED",
                "next_conversation_focus": "PROGRESSION"
            })
            decision["language"] = self.select_language(decision)
            return decision


        # --------------------------------------
        # 3. Quiet / Overload Protection
        # --------------------------------------
        if tempo == "QUIET" or emotional_state == "QUIET":
            decision.update({
                "primary_goal": "LISTEN",
                "safety_level": "HIGH",
                "emotional_pressure": "LOW",
                "recommended_voice_mode": "WAIT",
                "allow_silence": True,
                "narrative_weight": "NONE",
                "reflection_weight": "LOW",
                "understood_user_state": "OVERWHELMED",
                "next_conversation_focus": "REST"
            })
            decision["language"] = self.select_language(decision)
            return decision
        


        # --------------------------------------
        # 4. Gratitude / Resolution Layer
        # --------------------------------------
        if text_signal["gratitude"]:
            decision.update({
                "primary_goal": "REFLECT",
                "safety_level": "LOW",
                "emotional_pressure": "LOW",
                "recommended_voice_mode": "GUIDE",
                "allow_silence": False,
                "narrative_weight": "LIGHT",
                "reflection_weight": "LIGHT",
                "understood_user_state": "RELIEVED",
                "next_conversation_focus": "INTEGRATION"
            })
            decision["language"] = self.select_language(decision)
            return decision


        # --------------------------------------
        # 5. Default Clarification
        # --------------------------------------
        if text_signal["uncertainty"]:
            decision.update({
                "understood_user_state": "UNCERTAIN",
                "next_conversation_focus": "CLARITY"
            })

        language = self.select_language(decision)
        decision["language"] = language
        decision["momentum"] = momentum

        
        #------- Guarantee complete Cognitive Schema ---------
        decision.setdefault("recommended_voice_mode", "GUIDE")
        decision.setdefault("narrative_weight", "NORMAL")
        decision.setdefault("reflection_weight", "MEDIUM")
        decision.setdefault("allow_silence", False)

        decision["language"] = self.select_language(decision)
        return decision

