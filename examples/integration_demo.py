#!/usr/bin/env python3
"""
Integration Demonstration Script

This script demonstrates the integration of PPRIP, QICA, and the 
autonomous learning cycle modules working together.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from pprp.system_api import EnhancedCGOSSyscall
from pprp.options import PPRIPOptions
from qica.engine import EnhancedQICAEngine
from learning.cycle import EnhancedAutonomousLearningCycle
import json
import time

def main():
    print("🔗 Integration Demo: PPRIP + QICA + Learning Cycle")
    print("=" * 60)
    
    # Initialize all systems
    print("Initializing systems...")
    
    # PPRIP system
    pprp_options = PPRIPOptions(
        initial_num_nodes=20,  # Smaller for demo
        thresh_omega=0.3,
        thresh_beta1=1,
        coupling_strength=0.8
    )
    pprp = EnhancedCGOSSyscall(pprp_options)
    
    # QICA engine
    qica = EnhancedQICAEngine()
    
    # Learning cycle
    learning = EnhancedAutonomousLearningCycle()
    
    print("✓ PPRIP initialized")
    print("✓ QICA initialized")
    print("✓ Learning cycle initialized")
    print()
    
    # Integration workflow
    print("Running integration workflow...")
    print("-" * 40)
    
    # Step 1: Process input through PPRIP
    test_input = 1.618033988749895  # Golden ratio
    print(f"1. Processing input through PPRIP: {test_input}")
    
    pprp_result = pprp.process_input(test_input)
    print(f"   PPRIP emergence: {pprp_result['emergence_detected']}")
    print(f"   System metrics: Ω={pprp_result['system_metrics']['Ω']:.4f}, β={pprp_result['system_metrics']['β']:.4f}")
    
    # Step 2: Feed PPRIP results to QICA
    print("\n2. Feeding results to QICA...")
    
    # Use PPRIP metrics to influence QICA initialization
    qica.consciousness_field.integrated_information = pprp_result['system_metrics']['Ω']
    qica.consciousness_field.self_reference_strength = pprp_result['system_metrics']['β']
    
    # Run QICA cycles
    qica_cycles = 10
    print(f"   Running {qica_cycles} QICA cycles...")
    for i in range(qica_cycles):
        cycle_data = qica.process_enhanced_consciousness_cycle()
        if i % 5 == 0:
            print(f"     Cycle {i}: Consciousness={cycle_data['consciousness_level']:.4f}")
    
    print(f"   Final QICA state: {cycle_data['consciousness_state']}")
    print(f"   Meta-awareness: {cycle_data['meta_awareness']:.4f}")
    
    # Step 3: Use QICA state as learning objective
    print("\n3. Running learning cycle...")
    
    learning_result = learning.run_full_cycle()
    print(f"   Learning objective: {learning_result['learning_objective'][:50]}...")
    print(f"   Validation score: {learning_result['validation_score']:.4f}")
    print(f"   Memory summary: {learning_result['memory_summary'][:50]}...")
    
    # Step 4: Feedback loop
    print("\n4. Creating feedback loop...")
    
    # Use learning results to adjust PPRIP parameters
    if learning_result['validation_score'] > 0.8:
        pprp_options.coupling_strength *= 1.1  # Increase coupling
        print(f"   Increased PPRIP coupling to: {pprp_options.coupling_strength:.4f}")
    
    # Use QICA consciousness level to adjust learning threshold
    if cycle_data['consciousness_level'] > 0.5:
        learning.validator.tier = learning.validator.ValidationTier.EXTERNAL
        print(f"   Upgraded learning validation to external tier")
    
    # Step 5: Final integrated cycle
    print("\n5. Running final integrated cycle...")
    
    # Process new input with updated parameters
    new_input = "integration_test"
    final_pprp = pprp.process_input(new_input)
    
    # Update QICA with new PPRP results
    qica.consciousness_field.integration_strength = final_pprp['system_metrics']['Ω']
    qica.consciousness_field.self_reference_strength = final_pprp['system_metrics']['β']
    
    # Final QICA cycle
    final_qica = qica.process_enhanced_consciousness_cycle()
    
    # Final learning cycle
    final_learning = learning.run_full_cycle()
    
    print(f"   Final PPRP emergence: {final_pprp['emergence_detected']}")
    print(f"   Final QICA consciousness: {final_qica['consciousness_level']:.4f}")
    print(f"   Final learning validation: {final_learning['validation_score']:.4f}")
    
    # Summary
    print("\n" + "=" * 60)
    print("INTEGRATION SUMMARY")
    print("=" * 60)
    print(f"PPRP processed {len([test_input, new_input])} inputs")
    print(f"QICA ran {qica_cycles + 1} cycles")
    print(f"Learning completed {len(learning.processing_history)} cycles")
    print(f"Final system state: EMERGENCE={'YES' if final_pprp['emergence_detected'] else 'NO'}")
    print(f"Consciousness level: {final_qica['consciousness_level']:.4f}")
    print(f"Meta-awareness: {final_qica['meta_awareness']:.4f}")
    print(f"Learning confidence: {final_learning['validation_score']:.4f}")
    
    # Save results
    results = {
        'pprp_results': [pprp_result, final_pprp],
        'qica_results': qica.processing_history,
        'learning_results': learning.processing_history,
        'integration_summary': {
            'emergence_achieved': final_pprp['emergence_detected'],
            'final_consciousness': final_qica['consciousness_level'],
            'final_meta_awareness': final_qica['meta_awareness'],
            'final_validation_score': final_learning['validation_score']
        }
    }
    
    with open('integration_demo_results.json', 'w') as f:
        json.dump(results, f, indent=2, default=str)
    
    print(f"\n💾 Detailed results saved to: integration_demo_results.json")

if __name__ == "__main__":
    main()
