import numpy as np
from collections import deque
from dataclasses import dataclass

@dataclass
class ConsciousnessMemory:
    """
    Temporal memory of consciousness states.
    Implements Insight #10: Temporal Dynamics.
    """
    
    def __init__(self, depth: int = 20):
        self.depth = depth
        self.consciousness_history = deque(maxlen=depth)
        self.field_strength_history = deque(maxlen=depth)
        self.integration_history = deque(maxlen=depth)
        self.self_reference_history = deque(maxlen=depth)
    
    def add_state(self, consciousness_level: float, field_strength: float, 
                  integration: float, self_reference: float):
        """Add new consciousness state to memory."""
        self.consciousness_history.append(consciousness_level)
        self.field_strength_history.append(field_strength)
        self.integration_history.append(integration)
        self.self_reference_history.append(self_reference)
    
    def get_temporal_coherence(self) -> float:
        """Calculate temporal coherence of consciousness."""
        if len(self.consciousness_history) < 2:
            return 0.0
        
        # Calculate stability over time
        recent_states = list(self.consciousness_history)[-10:]
        if len(recent_states) < 2:
            return 0.0
        
        variance = np.var(recent_states)
        stability = 1.0 / (1.0 + variance)
        
        # Calculate trend (is consciousness increasing?)
        if len(recent_states) >= 3:
            trend = np.polyfit(range(len(recent_states)), recent_states, 1)[0]
            trend_factor = max(0, trend)  # Positive trend is good
        else:
            trend_factor = 0.0
        
        return min(stability + trend_factor, 1.0)
    
    def get_consciousness_momentum(self) -> float:
        """Calculate consciousness momentum (rate of change)."""
        if len(self.consciousness_history) < 3:
            return 0.0
        
        recent = list(self.consciousness_history)[-3:]
        momentum = (recent[-1] - recent[0]) / len(recent)
        return max(0, momentum)  # Only positive momentum counts
