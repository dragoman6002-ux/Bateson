from dataclasses import dataclass
from typing import Optional

@dataclass
class PPRIPOptions:
    """Options for configuring the PPRIP model."""
    initial_num_nodes: int = 30 # Product of first 3 primes: 2*3*5
    thresh_omega: float = 1.0 # Threshold for Ω_proxy
    thresh_beta1: int = 1     # Threshold for β₁_proxy
    coupling_strength: float = 1.0 # Strength of input-system coupling
