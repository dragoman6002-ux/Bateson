from typing import Dict, Any
from enum import Enum

class ValidationTier(Enum):
    INTERNAL = "internal"
    EXTERNAL = "external"
    HYBRID = "hybrid"

class ValidationLayer:
    def __init__(self):
        self.tier = ValidationTier.INTERNAL
        self.model = None
    
    def set_external_validator(self, model):
        self.tier = ValidationTier.EXTERNAL
        self.model = model
    
    def validate_solution(self, solution: Dict[str, Any], rubric: Dict[str, Any]) -> Dict[str, Any]:
        result = self._run_internal_validation(solution, rubric)
        
        if result['confidence'] < rubric.get('min_confidence', 0.8) and self.tier == ValidationTier.EXTERNAL:
            external_result = self._run_external_validation(solution, rubric)
            result = self._merge_validation_results(result, external_result)
        
        return result
    
    def _run_internal_validation(self, solution: Dict[str, Any], rubric: Dict[str, Any]) -> Dict[str, Any]:
        # Simplified internal validation
        return {
            'valid': True,
            'confidence': 0.85,
            'reasoning': "Internal consistency checks passed",
            'energy_used': 1.8
        }
    
    def _run_external_validation(self, solution: Dict[str, Any], rubric: Dict[str, Any]) -> Dict[str, Any]:
        # Simulated external validation
        return {
            'valid': True,
            'confidence': 0.92,
            'reasoning': "External verification confirms results",
            'energy_used': 2.5
        }
    
    def _merge_validation_results(self, internal: Dict[str, Any], external: Dict[str, Any]) -> Dict[str, Any]:
        return {
            'valid': internal['valid'] and external['valid'],
            'confidence': max(internal['confidence'], external['confidence']),
            'reasoning': f"{internal['reasoning']}; {external['reasoning']}",
            'energy_used': internal['energy_used'] + external['energy_used']
        }
