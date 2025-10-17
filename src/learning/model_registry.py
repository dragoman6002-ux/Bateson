from typing import Dict, Any

class CapabilityVector:
    def __init__(self, math: float = 0.5, code: float = 0.5, logic: float = 0.5, general: float = 0.5):
        self.math = math
        self.code = code
        self.logic = logic
        self.general = general
    
    def compute_match_score(self, query_features: Dict[str, float]) -> float:
        return sum(self.__dict__[key] * value for key, value in query_features.items())

class ModelCapability:
    def __init__(self, id: str, name: str, energy_profile: Dict[str, float]):
        self.id = id
        self.name = name
        self.capability = CapabilityVector(**energy_profile.get('capabilities', {}))
        self.energy_profile = energy_profile.get('energy', {
            'idle': 0.5, 'active': 2.5, 'validation': 1.8
        })

class ModelRegistry:
    def __init__(self):
        self.models = {
            'phi4': ModelCapability('phi4', 'Microsoft Phi-4', {
                'capabilities': {'math': 0.9, 'code': 0.7, 'logic': 0.8, 'general': 0.75},
                'energy': {'idle': 0.6, 'active': 3.2, 'validation': 2.1}
            }),
            'o1': ModelCapability('o1', 'OpenAI o1', {
                'capabilities': {'math': 0.8, 'code': 0.85, 'logic': 0.85, 'general': 0.9},
                'energy': {'idle': 0.8, 'active': 4.5, 'validation': 3.2}
            }),
            'gemini_flash': ModelCapability('gemini_flash', 'Google Gemini Flash', {
                'capabilities': {'math': 0.75, 'code': 0.7, 'logic': 0.7, 'general': 0.9},
                'energy': {'idle': 0.5, 'active': 2.8, 'validation': 2.0}
            })
        }
    
    def select_model(self, query_features: Dict[str, float]) -> ModelCapability:
        best_model = None
        best_score = -1
        
        for model in self.models.values():
            score = model.capability.compute_match_score(query_features)
            energy_cost = model.energy_profile['active']
            adjusted_score = score / (1 + energy_cost)  # Energy-performance tradeoff
            
            if adjusted_score > best_score:
                best_score = adjusted_score
                best_model = model
        
        return best_model
