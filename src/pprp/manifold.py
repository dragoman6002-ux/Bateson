import networkx as nx
import numpy as np
import math
from typing import Dict, List, Any, Tuple, Optional, Callable
from dataclasses import dataclass

PI = math.pi
PHI = (1 + math.sqrt(5)) / 2

@dataclass
class PPRIPOptions:
    """Options for configuring the PPRIP model."""
    initial_num_nodes: int = 30 # Product of first 3 primes: 2*3*5
    thresh_omega: float = 1.0 # Threshold for Ω_proxy
    thresh_beta1: int = 1     # Threshold for β₁_proxy
    coupling_strength: float = 1.0 # Strength of input-system coupling

class EnhancedSubstrateManifold(SubstrateManifold):
    """
    Enhanced version of SubstrateManifold with PPRIP capabilities.
    """
    def __init__(self, n: int = 30, k: int = 4, options: Optional[PPRIPOptions] = None):
        super().__init__(n, k)
        self.options = options or PPRIPOptions()
        self.node_states = [np.random.rand(4) for _ in self.G.nodes()] # 4D state vector per node
        self.primes = self._generate_primes_up_to(n)
        self._initialize_with_cycles()
    
    def _generate_primes_up_to(self, n: int) -> List[int]:
        """Sieve of Eratosthenes."""
        sieve = [True] * (n + 1)
        sieve[0:2] = [False, False]
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                sieve[i*i::i] = [False] * len(sieve[i*i::i)]
        return [i for i, is_prime in enumerate(sieve) if is_prime]
    
    def _initialize_with_cycles(self):
        """Ensure the graph has cycles for β₁ > 0."""
        if len(nx.cycle_basis(self.G)) == 0:
            # Create a cycle if none exists
            nodes = list(self.G.nodes())
            for i in range(len(nodes)):
                self.G.add_edge(nodes[i], nodes[(i+1) % len(nodes)])
    
    def assign_nodes_to_primes(self) -> Dict[int, List[int]]:
        """Assign nodes to primes based on index modulo p."""
        assignment = {p: [] for p in self.primes}
        for i, node in enumerate(self.G.nodes()):
            for p in self.primes:
                if i % p == 0:
                    assignment[p].append(node)
        return assignment
    
    def update_node_states(self, new_states: List[np.ndarray]):
        """Update the states of all nodes."""
        if len(new_states) == len(self.node_states):
            self.node_states = new_states
    
    def get_node_states(self) -> List[np.ndarray]:
        """Get the current states of all nodes."""
        return self.node_states
