#!/usr/bin/env python3
"""
PPRIP Demonstration Script

This script demonstrates the basic functionality of the Pi-Phi-Prime Resonant 
Information Processor (PPRIP) module.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from pprp.system_api import EnhancedCGOSSyscall
from pprp.options import PPRIPOptions
import numpy as np

def main():
    print("🔢 PPRIP (Pi-Phi-Prime Resonant Information Processor) Demo")
    print("=" * 60)
    
    # Initialize PPRIP system with custom options
    options = PPRIPOptions(
        initial_num_nodes=30,
        thresh_omega=0.5,
        thresh_beta1=1,
        coupling_strength=1.0
    )
    
    syscall = EnhancedCGOSSyscall(options)
    
    print(f"Initial Graph: {syscall.M.G.number_of_nodes()} nodes, {syscall.M.G.number_of_edges()} edges")
    print(f"Primes: {syscall.M.primes}")
    print(f"Thresholds: Ω={options.thresh_omega}, β₁={options.thresh_beta1}")
    print()
    
    # Test inputs
    test_inputs = [
        1.0,                    # Simple number
        1.618033988749895,      # Golden ratio
        3.141592653589793,      # Pi
        "hello world",          # String input
        42,                     # Integer
    ]
    
    print("Processing test inputs:")
    print("-" * 40)
    
    for i, inp in enumerate(test_inputs):
        print(f"Input {i+1}: {inp}")
        
        # Process the input
        result = syscall.process_input(inp)
        
        # Display results
        print(f"  Input π-resonance: {result['input_resonance_metrics']['input_dev_pi']:.4f}")
        print(f"  Input φ-resonance: {result['input_resonance_metrics']['dev_phi_data']:.4f}")
        print(f"  System Ω: {result['system_metrics']['Ω']:.4f}")
        print(f"  System β: {result['system_metrics']['β']:.4f}")
        print(f"  Graph nodes: {result['graph_info']['num_nodes']}")
        print(f"  Graph edges: {result['graph_info']['num_edges']}")
        
        if result['emergence_detected']:
            print(f"  🎯 EMERGENCE: {result['insight']}")
        else:
            print(f"  Status: Processing...")
        print()
    
    # Final system state
    print("Final System State:")
    print("-" * 20)
    final_metrics = {m.axiom_id: m.value for m in [c(syscall.M) for c in syscall.cores]}
    for metric, value in final_metrics.items():
        print(f"  {metric}: {value:.4f}")
    
    print(f"\nEmergence history: {len(syscall.global_c['emergence_history'])} events")
    for event in syscall.global_c['emergence_history']:
        print(f"  Cycle {event['timestamp']}: {event['insight']}")

if __name__ == "__main__":
    main()
