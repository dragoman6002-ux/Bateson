from typing import Dict, Any, List
from enum import Enum
import datetime

class MemoryType(Enum):
    WORKING = "working"
    EPISODIC = "episodic"
    PROCEDURAL = "procedural"

class MemoryHierarchy:
    def __init__(self):
        self.working_memory = {}
        self.episodic_memory = []
        self.procedural_memory = []
        self._learning_phase_active = True
    
    def write_to_procedural(self, template: Dict[str, Any]):
        if not self._learning_phase_active:
            raise PermissionError("Procedural memory writes only allowed during learning phase")
        self.procedural_memory.append(template)
    
    def retrieve_context(self, query: str) -> Dict[str, Any]:
        # Simplified semantic search
        relevant_memories = [m for m in self.episodic_memory if query.lower() in m.get('content', '').lower()]
        return {'relevant_memories': relevant_memories[:3]}
