import datetime
from typing import Dict, Any, List
from enum import Enum

class LogicalType(Enum):
    OBJECT_LEVEL = "Object Level"
    META_LEVEL = "Meta Level"
    META_META_LEVEL = "Meta-Meta Level"

class ProvenanceNode:
    def __init__(self, node_id: str, content: str, node_type: str, logical_type: LogicalType):
        self.node_id = node_id
        self.content = content
        self.type = node_type
        self.logical_type = logical_type
        self.metadata = {
            'timestamp': datetime.datetime.now().isoformat(),
            'energy_used': 0.0
        }

class ProvenanceGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = []
    
    def add_node(self, node: ProvenanceNode):
        self.nodes[node.node_id] = node
    
    def create_edge(self, source_id: str, target_id: str, edge_type: str):
        self.edges.append({
            'source': source_id,
            'target': target_id,
            'type': edge_type,
            'timestamp': datetime.datetime.now().isoformat()
        })
    
    def get_subgraph(self, node_ids: List[str]) -> Dict[str, Any]:
        return {
            'nodes': {nid: self.nodes[nid] for nid in node_ids if nid in self.nodes},
            'edges': [e for e in self.edges if e['source'] in node_ids or e['target'] in node_ids]
        }
