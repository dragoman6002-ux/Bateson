#!/usr/bin/env python3
"""
PPRP Module Tests

Unit tests for the Pi-Phi-Prime Resonant Information Processor module.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import unittest
import numpy as np
from pprp.options import PPRIPOptions
from pprp.system_api import EnhancedCGOSSyscall

class TestPPRP(unittest.TestCase):
    """Test cases for PPRIP functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.options = PPRIPOptions(
            initial_num_nodes=10,  # Small for testing
            thresh_omega=0.5,
            thresh_beta1=1,
            coupling_strength=1.0
        )
        self.syscall = EnhancedCGOSSyscall(self.options)
    
    def test_options_initialization(self):
        """Test PPRIPOptions initialization."""
        self.assertEqual(self.options.initial_num_nodes, 10)
        self.assertEqual(self.options.thresh_omega, 0.5)
        self.assertEqual(self.options.thresh_beta1, 1)
        self.assertEqual(self.options.coupling_strength, 1.0)
    
    def test_syscall_initialization(self):
        """Test EnhancedCGOSSyscall initialization."""
        self.assertIsNotNone(self.syscall.M)
        self.assertIsNotNone(self.syscall.nodules)
        self.assertIsNotNone(self.syscall.cores)
        self.assertEqual(len(self.syscall.cores), 4)  # Pi, Phi, Omega, Beta
    
    def test_graph_structure(self):
        """Test graph initialization."""
        G = self.syscall.M.G
        self.assertGreater(G.number_of_nodes(), 0)
        self.assertGreaterEqual(G.number_of_edges(), G.number_of_nodes())  # Should have cycles
    
    def test_prime_generation(self):
        """Test prime number generation."""
        primes = self.syscall.M.primes
        self.assertIn(2, primes)
        self.assertIn(3, primes)
        self.assertIn(5, primes)
        self.assertLessEqual(max(primes), self.options.initial_num_nodes)
    
    def test_node_states(self):
        """Test node state initialization."""
        states = self.syscall.M.get_node_states()
        self.assertEqual(len(states), self.syscall.M.G.number_of_nodes())
        for state in states:
            self.assertEqual(len(state), 4)  # 4D state vectors
            self.assertTrue(all(isinstance(x, (int, float)) for x in state))
    
    def test_process_numeric_input(self):
        """Test processing numeric input."""
        result = self.syscall.process_input(3.14159)
        self.assertIn('input_data', result)
        self.assertIn('input_resonance_metrics', result)
        self.assertIn('system_metrics', result)
        self.assertIn('graph_info', result)
        self.assertIn('emergence_detected', result)
    
    def test_process_string_input(self):
        """Test processing string input."""
        result = self.syscall.process_input("test string")
        self.assertIsInstance(result, dict)
        self.assertIn('input_data', result)
    
    def test_system_metrics(self):
        """Test system metrics calculation."""
        result = self.syscall.process_input(1.0)
        metrics = result['system_metrics']
        self.assertIn('Ω', metrics)
        self.assertIn('β', metrics)
        self.assertIsInstance(metrics['Ω'], (int, float))
        self.assertIsInstance(metrics['β'], (int, float))
    
    def test_graph_info(self):
        """Test graph information."""
        result = self.syscall.process_input(1.0)
        graph_info = result['graph_info']
        self.assertIn('nodes', graph_info)
        self.assertIn('edges', graph_info)
        self.assertIn('num_nodes', graph_info)
        self.assertIn('num_edges', graph_info)
    
    def test_emergence_detection(self):
        """Test emergence detection."""
        # Process multiple inputs to potentially trigger emergence
        for i in range(5):
            result = self.syscall.process_input(float(i))
            if result['emergence_detected']:
                self.assertIn('insight', result)
                self.assertIsInstance(result['insight'], str)
                break
    
    def test_prime_assignment(self):
        """Test prime-to-node assignment."""
        assignment = self.syscall.M.assign_nodes_to_primes()
        self.assertIsInstance(assignment, dict)
        for prime, nodes in assignment.items():
            self.assertIsInstance(prime, int)
            self.assertIsInstance(nodes, list)
            for node in nodes:
                self.assertIsInstance(node, int)

if __name__ == '__main__':
    unittest.main()
