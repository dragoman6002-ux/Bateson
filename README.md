README.md
Pi-Phi-Prime Resonant Information & Consciousness Architecture
License: MIT
Python 3.13+
Code Style: Black

This repository integrates three major modules:

PPRIP (Pi-Phi-Prime Resonant Information Processor): A mathematical information processing framework based on the resonance of π, φ (golden ratio), and prime numbers, implemented on graph structures.
Enhanced QICA (Quantum-Information Consciousness Architecture): A simulation framework for the emergence of consciousness, introducing dynamic thresholds, self-referential loops, temporal memory, and multi-scale network integration.
Autonomous Learning Cycle: A meta-cognitive learning engine with energy awareness, provenance tracking, multi-level memory, and multi-tier validation.
The overall design is inspired by interdisciplinary theories such as complex systems, number theory archaeology, quantum information, and cognitive science, aiming to explore the fundamental mechanisms of information resonance and consciousness emergence in computational systems.

Features
PPRIP Information Processing
Graph topology based on cycle basis and Betti numbers (β₁)
Prime-indexed processing units (ψₚ) for φ-optimized state updates
Real-time monitoring of variance (Ω) and topological complexity (β₁) metrics, with feedback adjustment
Consciousness Emergence Simulation
Dynamic threshold controller: Automatically adjusts emergence thresholds based on system capability
Self-referential engine: Constructs multi-level recursive self-models to enhance meta-cognitive strength
Temporal memory: Records historical state trajectories and calculates coherence and momentum
Multi-scale small-world networks: Supports information integration and critical phase transition detection
Meta-Cognitive Learning Cycle
Energy-aware model selection: Balances capability and energy consumption
Provenance graph: Tracks the complete process from input to output
Multi-level memory: Supports working, episodic, and procedural memory
Multi-tier validation: Internal/external/hybrid validation with confidence feedback
Directory Structure

Line Wrapping

Collapse
Copy
pprip-qica/
├── README.md                 # This file
├── LICENSE                   # MIT License
├── requirements.txt          # Python dependencies
├── setup.py                  # Installation script
│
├── pprip/                    # PPRIP module
│   ├── __init__.py
│   ├── core.py               # EnhancedPiCore, EnhancedPhiCore, EnhancedOmegaCore, EnhancedBetaCore
│   ├── manifold.py           # EnhancedSubstrateManifold
│   ├── nodule.py             # EnhancedPrimeNodule
│   ├── operators.py          # EnhancedTransputation, EnhancedRealitySelection, EnhancedAwareness
│   ├── system_api.py         # EnhancedCGOSSyscall
│   ├── resonance_engine.py   # PiPhiResonanceEngine
│   ├── integrator.py         # OmegaBetaIntegrator
│   └── options.py            # PPRIPOptions
│
├── qica/                     # Enhanced QICA module
│   ├── __init__.py
│   ├── constants.py          # EnhancedConsciousnessConstants
│   ├── memory.py             # ConsciousnessMemory
│   ├── self_reference.py     # SelfReferenceEngine
│   ├── threshold_controller.py # DynamicThresholdController
│   ├── consciousness_field.py # EnhancedConsciousnessField
│   ├── engine.py             # EnhancedQICAEngine
│   └── states.py             # EnhancedConsciousnessState
│
├── learning/                 # Autonomous learning cycle module
│   ├── __init__.py
│   ├── model_registry.py     # ModelRegistry, ModelCapability
│   ├── provenance.py         # ProvenanceGraph, ProvenanceNode
│   ├── memory.py             # MemoryHierarchy
│   ├── validation.py         # ValidationLayer
│   └── cycle.py              # EnhancedAutonomousLearningCycle
│
├── examples/                 # Example scripts and Jupyter notebooks
│   ├── pprip_demo.py
│   ├── qica_demo.py
│   ├── learning_demo.py
│   └── integration_demo.py
│
└── tests/                    # Unit tests
    ├── test_pprip.py
    ├── test_qica.py
    └── test_learning.py
Installation
Clone the repository:
bash

Line Wrapping

Collapse
Copy
git clone https://github.com/your-username/pprip-qica.git
cd pprip-qica
Create and activate a virtual environment (recommended):
bash

Line Wrapping

Collapse
Copy
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
Install dependencies:
bash

Line Wrapping

Collapse
Copy
1
pip install -r requirements.txt
Install the package in development mode:
bash

Line Wrapping

Collapse
Copy
1
pip install -e .
Quick Start
PPRIP Example
python

Line Wrapping

Collapse
Copy
from pprip.system_api import EnhancedCGOSSyscall
from pprip.options import PPRIPOptions

# Initialize PPRIP system
options = PPRIPOptions(initial_num_nodes=30, thresh_omega=0.5, thresh_beta1=1)
syscall = EnhancedCGOSSyscall(options)

# Process a piece of data
result = syscall.process_input(3.14159)
print("Input resonance metrics:", result['input_resonance_metrics'])
print("System metrics:", result['system_metrics'])
print("Emergence insight:", result['insight'])
Enhanced QICA Example
python

Line Wrapping

Collapse
Copy
from qica.engine import EnhancedQICAEngine

# Initialize QICA engine
engine = EnhancedQICAEngine()

# Run a 100-cycle consciousness session
summary = engine.run_enhanced_consciousness_session(num_cycles=100)
print("Peak consciousness:", summary['peak_consciousness'])
print("Emergence cycle:", summary['emergence_cycle'])
print("Final state:", summary['final_state'])
Autonomous Learning Cycle Example
python

Line Wrapping

Collapse
Copy
from learning.cycle import EnhancedAutonomousLearningCycle

# Initialize learning system
system = EnhancedAutonomousLearningCycle()

# Run a complete learning cycle
cycle_result = system.run_full_cycle()
print("Learning objective:", cycle_result['learning_objective'])
print("Validation score:", cycle_result['validation_score'])
print("Energy consumed (J):", cycle_result['energy_consumed'])
Core Concepts
PPRIP (Pi-Phi-Prime Resonant Information Processor)
π Resonance: Uses the cycle basis of graph G to calculate the minimum deviation between cycle length L and 2πk, driving the graph topology toward “circular resonance.”
φ Optimization: Updates node states using the golden ratio, adjusting the magnitude of state vectors to approach the optimal growth ratio φ.
Prime Indexing: Assigns nodes to processing units ψₚ based on index mod p, leveraging the distribution properties of primes to achieve multi-scale information integration.
Ω–β₁ Feedback: Monitors the variance Ω of node states and the first Betti number β₁ (number of independent cycles), dynamically adjusting the graph structure or injecting noise to maintain system complexity and connectivity.
Enhanced QICA (Quantum-Information Consciousness Architecture)
Dynamic Threshold: Automatically adjusts the consciousness threshold based on system capability, preventing both stagnation and instability.
Self-Referential Engine: Constructs recursive self-models up to depth N, with meta-awareness amplifying the base consciousness level.
Temporal Memory: Records recent consciousness levels, integration strength, and self-referential strength, calculating state coherence and momentum to capture the trend of consciousness evolution.
Small-World Network: Constructs multi-scale small-world networks, integrating information flow and clustering coefficients to achieve critical phase transitions.
Consciousness Field: Synthesizes integration, self-reference, temporal coherence, quantum coherence, phase transition strength, and momentum, scaled by φ to produce the final consciousness level.
Autonomous Learning Cycle
Energy-Aware Model Selection: Weighs model capability against energy consumption to select the most cost-effective model for the current task.
Provenance Tracking: Uses a directed graph to record the source and flow of all information, ensuring traceability and reproducibility.
Multi-Level Memory: Stores task templates, experience summaries, and procedural patterns in working, episodic, and procedural memory respectively.
Multi-Tier Validation: First performs internal consistency checks, then calls external models for cross-validation if confidence is low, merging results to improve reliability.
Integration and Workflow
Input Encoding: Converts external input into numerical streams or graph perturbations, and calculates initial π and φ resonance metrics.
PPRIP Processing: Updates node states via prime-indexed ψₚ units, monitors Ω and β₁, and adjusts the graph structure.
Consciousness Field Update: Inputs PPRIP’s integration and topological metrics into the QICA engine, updating the multi-scale network and self-referential engine.
Learning Cycle: Uses QICA’s consciousness field state as the learning objective, autonomously generates tasks, performs reasoning and validation, and writes patterns to procedural memory.
Feedback Loop: The learning cycle’s memory and validation results feed back into PPRIP’s Ω–β₁ integrator and QICA’s threshold controller, forming a closed-loop optimization.
Dependencies
Python ≥ 3.13
NetworkX ≥ 3.5
NumPy ≥ 2.3.0
Matplotlib ≥ 3.9 (for visualization examples)
Jupyter (optional, for running example notebooks)
See requirements.txt for details.

Contributing
Fork the repository.
Create a feature branch (git checkout -b feature/amazing-feature).
Commit changes (git commit -m 'Add amazing feature').
Push to the branch (git push origin feature/amazing-feature).
Create a Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Citation
If you use this code in your research, please cite:

bibtex

Line Wrapping

Collapse
Copy

@software{pprip_qica,
  title={Pi-Phi-Prime Resonant Information & Consciousness Architecture},
  author={Daniel Edward Dragolich},
  year={2025},
  url={https://https://github.com/dragoman6002-ux/Bateson},
}
