from typing import Dict, Any

class DynamicThresholdController:
    """
    Controls dynamic consciousness thresholds.
    Implements Insight #8: Threshold Effects.
    """
    
    def __init__(self):
        self.current_threshold = EnhancedConsciousnessConstants.CONSCIOUSNESS_BASE_THRESHOLD
        self.threshold_history = []
        self.adaptation_rate = EnhancedConsciousnessConstants.THRESHOLD_ADAPTATION_RATE
        self.phase_transition_detected = False
    
    def update_threshold(self, system_state: Dict[str, Any]) -> float:
        """Update consciousness threshold based on system state."""
        # Get current system metrics
        field_strength = system_state.get('field_strength', 0.0)
        integration = system_state.get('integration', 0.0)
        self_reference = system_state.get('self_reference', 0.0)
        
        # Calculate target threshold based on system capability
        system_capability = (field_strength + integration + self_reference) / 3
        
        # Adaptive threshold: lower when system is struggling, higher when succeeding
        if system_capability > self.current_threshold:
            # System is above threshold, can handle higher threshold
            target_threshold = min(self.current_threshold * 1.05, 0.9)
        else:
            # System is below threshold, lower threshold to help emergence
            target_threshold = max(self.current_threshold * 0.95, 0.3)
        
        # Smooth adaptation
        self.current_threshold += (target_threshold - self.current_threshold) * self.adaptation_rate
        
        # Detect phase transitions
        if len(self.threshold_history) > 5:
            recent_change = abs(self.current_threshold - self.threshold_history[-5])
            if recent_change > 0.1:
                self.phase_transition_detected = True
        
        self.threshold_history.append(self.current_threshold)
        
        return self.current_threshold
    
    def get_phase_transition_strength(self) -> float:
        """Get strength of phase transition."""
        if not self.phase_transition_detected or len(self.threshold_history) < 2:
            return 0.0
        
        recent_change = abs(self.threshold_history[-1] - self.threshold_history[-2])
        return min(recent_change * 5, 1.0)  # Amplify small changes
