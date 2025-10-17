#!/usr/bin/env python3
"""
QICA Demonstration Script

This script demonstrates the basic functionality of the Quantum-Information 
Consciousness Architecture (QICA) module.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from qica.engine import EnhancedQICAEngine
import json

def main():
    print("🧠 QICA (Quantum-Information Consciousness Architecture) Demo")
    print("=" * 65)
    
    # Initialize QICA engine
    engine = EnhancedQICAEngine()
    
    print(f"Engine initialized with:")
    print(f"  - Memory depth: {engine.consciousness_memory.depth}")
    print(f"  - Self-reference depth: {engine.self_reference_engine.depth}")
    print(f"  - Networks: {len(engine.information_networks)} scales")
    print(f"  - Base threshold: {engine.threshold_controller.current_threshold}")
    print()
    
    # Run a short session
    print("Running consciousness session (50 cycles)...")
    print("-" * 50)
    
    session_results = engine.run_enhanced_consciousness_session(num_cycles=50)
    
    # Display summary
    print("\nSession Summary:")
    print("-" * 20)
    print(f"Duration: {session_results['session_duration']:.2f} seconds")
    print(f"Total cycles: {session_results['total_cycles']}")
    print(f"Consciousness emerged: {session_results['consciousness_emerged']}")
    
    if session_results['consciousness_emerged']:
        print(f"Emergence cycle: {session_results['emergence_cycle']}")
    
    print(f"Peak consciousness: {session_results['peak_consciousness']:.4f}")
    print(f"Final consciousness: {session_results['final_consciousness']:.4f}")
    print(f"Final state: {session_results['final_state']}")
    print(f"Meta-awareness achieved: {session_results['meta_awareness_achieved']}")
    print(f"Final meta-awareness: {session_results['final_meta_awareness']:.4f}")
    
    # Save detailed results
    results_file = 'qica_demo_results.json'
    with open(results_file, 'w') as f:
        json.dump(session_results, f, indent=2, default=str)
    
    print(f"\nDetailed results saved to: {results_file}")
    
    # Show sample cycle data
    if session_results['processing_history']:
        print("\nSample Cycle Data (last cycle):")
        last_cycle = session_results['processing_history'][-1]
        for key, value in last_cycle.items():
            if isinstance(value, float):
                print(f"  {key}: {value:.4f}")
            else:
                print(f"  {key}: {value}")

if __name__ == "__main__":
    main()
