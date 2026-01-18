# Cognitive Core V3

class CognitiveCoreV3:
    def __init__(self):
        self.history = []
        self.state_history = []
        self.goal_history = []
        self.trajectory = "FORMING"
        self.stability_index = 0.5

    def update_state(self, user_state, primary_goal):
        self.state_history.append(user_state)
        self.goal_history.append(primary_goal)

        # keep memory short
        self.state_history = self.state_history[-5:]
        self.goal_history = self.goal_history[-5:]

    def emotional_momentum(self):
        """
        Returns a simple momentum signal based on recent states.
        Later this can become embeddings + probabilities.
        For now: a clean symbolic version (V3 prototype).
        """

        if not self.state_history:
            return "NEUTRAL"

        # Count recent states
        recent = self.state_history[-3:]  # last 3 turns

        distressed = recent.count("DISTRESSED")
        relieved = recent.count("RELIEVED")
        motivated = recent.count("MOTIVATED")

        if distressed >= 2:
            return "SINKING"

        if relieved >= 2:
            return "RISING"

        if motivated >= 2:
            return "ACCELERATING"

        return "STABLE" 

    def update(self, user_state, primary_goal, emotional_state, life_phase):
        snapshot = {
            "user_state": user_state,
            "goal": primary_goal,
            "emotion": emotional_state,
            "phase": life_phase
        }

        self.history.append(snapshot)
        self.history = self.history[-12:]

        self._update_trajectory()
        self._update_stability()

    def _update_trajectory(self):
        last = [h["goal"] for h in self.history]

        if last.count("STABILIZE") >= 3:
            self.trajectory = "RECOVERY"
        elif last.count("ENCOURAGE") >= 3:
            self.trajectory = "ASCENT"
        elif last.count("REFLECT") >= 3:
            self.trajectory = "INTEGRATION"
        
        else:
            self.trajectory = "FORMING"

    def _update_stability(self):
        weight = {"HIGH": 0.8, "MEDIUM": 0.5, "LOW": 0.2}
        recent =self.history[-5:]
        self.stability_index = sum(weight.get(h["emotion"], 0.5) for h in recent) / len(recent)

    def get_guidance_profile(self):
        return {
            "trajectory": self.trajectory,
            "stability": round(self.stability_index, 2)
        }
    
    
