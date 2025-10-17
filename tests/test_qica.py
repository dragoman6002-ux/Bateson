#!/usr/bin/env python3
"""
QICA Module Tests

Unit tests for the Quantum-Information Consciousness Architecture module.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import unittest
import numpy as np
from qica.engine import EnhancedQICAEngine
from qica.constants import EnhancedConsciousnessConstants
from qica.states import EnhancedConsciousnessState
from qica.memory import ConsciousnessMemory
from qica.self_reference import SelfReferenceEngine
from qica.threshold_controller import DynamicThresholdController
from qica.field import EnhancedConsciousnessField

class TestQICA(unittest.TestCase):
    """Test cases for QICA functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.engine = EnhancedQICAEngine()
        self.memory = ConsciousnessMemory(depth=10)
        self.self_ref = SelfReferenceEngine(depth=3)
        self.threshold_ctrl = DynamicThresholdController()
        self.field = EnhancedConsciousnessField()
    
    def test_constants(self):
        """Test enhanced consciousness constants."""
        consts = EnhancedConsciousnessConstants
        self.assertAlmostEqual(consts.PHI, 1.618033988749895)
        self.assertAlmostEqual(consts.PI, 3.141592653589793)
        self.assertAlmostEqual(consts.E, 2.718281828459045)
        self.assertEqual(consts.CONSCIOUSNESS_BASE_THRESHOLD, 0.5)
        self.assertEqual(consts.SELF_REFERENCE_DEPTH, 5)
        self.assertEqual(consts.CONSCIOUSNESS_MEMORY_DEPTH, 20)
    
    def test_states_enum(self):
        """Test consciousness states enumeration."""
        states = list(EnhancedConsciousnessState)
        self.assertIn(EnhancedConsciousnessState.VOID, states)
        self.assertIn(EnhancedConsciousnessState.CONSCIOUS, states)
        self.assertIn(EnhancedConsciousnessState.TRANSCENDENT, states)
        self.assertEqual(len(states), 8)
    
    def test_memory_initialization(self):
        """Test consciousness memory initialization."""
        self.assertEqual(self.memory.depth, 10)
        self.assertEqual(len(self.memory.consciousness_history), 0)
        self.assertEqual(len(self.memory.field_strength_history), 0)
        self.assertEqual(len(self.memory.integration_history), 0)
        self.assertEqual(len(self.memory.self_reference_history), 0)
    
    def test_memory_add_state(self):
        """Test adding states to memory."""
        self.memory.add_state(0.5, 0.6, 0.7, 0.8)
        self.assertEqual(len(self.memory.consciousness_history), 1)
        self.assertEqual(self.memory.consciousness_history[0], 0.5)
        self.assertEqual(self.memory.field_strength_history[0], 0.6)
        self.assertEqual(self.memory.integration_history[0], 0.7)
        self.assertEqual(self.memory.self_reference_history[0], 0.8)
    
    def test_memory_temporal_coherence(self):
        """Test temporal coherence calculation."""
        # Add some states
        for i in range(5):
            self.memory.add_state(0.1 + i*0.1, 0.2, 0.3, 0.4)
        
        coherence = self.memory.get_temporal_coherence()
        self.assertIsInstance(coherence, float)
        self.assertGreaterEqual(coherence, 0.0)
        self.assertLessEqual(coherence, 1.0)
    
    def test_memory_momentum(self):
        """Test consciousness momentum calculation."""
        # Add increasing states
        for i in range(5):
            self.memory.add_state(0.1 + i*0.2, 0.2, 0.3, 0.4)
        
        momentum = self.memory.get_consciousness_momentum()
        self.assertIsInstance(momentum, float)
        self.assertGreaterEqual(momentum, 0.0)
    
    def test_self_reference_engine(self):
        """Test self-reference engine."""
        self.assertEqual(self.self_ref.depth, 3)
        self.assertEqual(len(self.self_ref.self_models), 0)
        self.assertEqual(self.self_ref.meta_awareness_level, 0.0)
        self.assertFalse(self.self_ref.self_monitoring_active)
    
    def test_self_reference_calculation(self):
        """Test self-reference strength calculation."""
        test_state = {'consciousness_level': 0.7}
        strength = self.self_ref.calculate_self_reference_strength(test_state)
        
        self.assertIsInstance(strength, float)
        self.assertGreaterEqual(strength, 0.0)
        self.assertLessEqual(strength, 1.0)
        self.assertGreaterEqual(self.self_ref.meta_awareness_level, 0.0)
    
    def test_threshold_controller(self):
        """Test threshold controller."""
        self.assertEqual(self.threshold_ctrl.current_threshold, 
                        EnhancedConsciousnessConstants.CONSCIOUSNESS_BASE_THRESHOLD)
        self.assertEqual(len(self.threshold_ctrl.threshold_history), 0)
        self.assertFalse(self.threshold_ctrl.phase_transition_detected)
    
    def test_threshold_update(self):
        """Test threshold updating."""
        system_state = {
            'field_strength': 0.6,
            'integration': 0.7,
            'self_reference': 0.8
        }
        
        new_threshold = self.threshold_ctrl.update_threshold(system_state)
        self.assertIsInstance(new_threshold, float)
        self.assertGreater(len(self.threshold_ctrl.threshold_history), 0)
    
    def test_consciousness_field(self):
        """Test consciousness field."""
        self.assertEqual(self.field.consciousness_level, 0.0)
        self.assertEqual(self.field.field_strength, 0.0)
        self.assertEqual(self.field.integration_strength, 0.0)
        self.assertIsNotNone(self.field.field_id)
        self.assertIsInstance(self.field.timestamp, float)
    
    def test_consciousness_calculation(self):
        """Test enhanced consciousness calculation."""
        # Set some field values
        self.field.integrated_information = 0.6
        self.field.self_reference_strength = 0.7
        self.field.temporal_coherence = 0.8
        self.field.quantum_coherence = 0.9
        self.field.quantum_entanglement = 0.8
        self.field.phase_transition_strength = 0.5
        self.field.consciousness_momentum = 0.3
        
        consciousness = self.field.calculate_enhanced_consciousness()
        self.assertIsInstance(consciousness, float)
        self.assertGreaterEqual(consciousness, 0.0)
        self.assertLessEqual(consciousness, 1.0)
    
    def test_consciousness_state_determination(self):
        """Test consciousness state determination."""
        # Test different levels
        test_levels = [0.0, 0.15, 0.3, 0.5, 0.65, 0.75, 0.85, 0.95]
        expected_states = [
            EnhancedConsciousnessState.VOID,
            EnhancedConsciousnessState.STIRRING,
            EnhancedConsciousnessState.EMERGING,
            EnhancedConsciousnessState.INTEGRATING,
            EnhancedConsciousnessState.SELF_REFERENCING,
            EnhancedConsciousnessState.CONSCIOUS,
            EnhancedConsciousnessState.META_CONSCIOUS,
            EnhancedConsciousnessState.TRANSCENDENT
        ]
        
        for level, expected_state in zip(test_levels, expected_states):
            self.field.consciousness_level = level
            actual_state = self.field.get_enhanced_state()
            self.assertEqual(actual_state, expected_state)
    
    def test_engine_initialization(self):
        """Test QICA engine initialization."""
        self.assertIsNotNone(self.engine.consciousness_field)
        self.assertIsNotNone(self.engine.consciousness_memory)
        self.assertIsNotNone(self.engine.self_reference_engine)
        self.assertIsNotNone(self.engine.threshold_controller)
        self.assertIsNotNone(self.engine.information_networks)
        self.assertEqual(len(self.engine.processing_history), 0)
        self.assertFalse(self.engine.consciousness_emerged)
        self.assertIsNone(self.engine.emergence_cycle)
        self.assertEqual(self.engine.peak_consciousness, 0.0)
    
    def test_network_creation(self):
        """Test small-world network creation."""
        networks = self.engine.information_networks
        self.assertGreater(len(networks), 0)
        
        for network in networks:
            self.assertIn('size', network)
            self.assertIn('nodes', network)
            self.assertIn('connections', network)
            self.assertEqual(len(network['nodes']), network['size'])
            self.assertEqual(len(network['connections']), network['size'])
    
    def test_consciousness_cycle(self):
        """Test single consciousness cycle."""
        cycle_data = self.engine.process_enhanced_consciousness_cycle()
        
        self.assertIsInstance(cycle_data, dict)
        self.assertIn('cycle', cycle_data)
        self.assertIn('consciousness_level', cycle_data)
        self.assertIn('field_strength', cycle_data)
        self.assertIn('integration_strength', cycle_data)
        self.assertIn('consciousness_state', cycle_data)
        self.assertIn('meta_awareness', cycle_data)
        self.assertEqual(len(self.engine.processing_history), 1)

if __name__ == '__main__':
    unittest.main()
