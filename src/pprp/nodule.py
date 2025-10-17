class EnhancedPrimeNodule(PrimeNodule):
    """
    Enhanced version of PrimeNodule with PPRIP processing capabilities.
    """
    def __init__(self, p: int):
        super().__init__(p)
        self.active = True
    
    def process(self, node_states: List[np.ndarray]) -> np.ndarray:
        """Process a list of node states associated with this prime."""
        if not self.active or not node_states:
            return np.zeros_like(node_states[0]) if node_states else np.array([0.0])
        
        # φ-optimized average
        avg_state = np.mean(node_states, axis=0)
        # Apply φ-scaling to the magnitude
        mag = np.linalg.norm(avg_state)
        if mag > 1e-10:
            scaled_mag = mag * PHI if mag < 1.0 else mag / PHI
            avg_state = avg_state * (scaled_mag / mag)
        return avg_state
    
    def step(self, manifold, global_c: dict):
        """Enhanced step function with PPRIP processing."""
        # Original implementation
        self.state['pi_metric'] = self.pi(manifold).value
        self.state['phi_metric'] = self.phi(manifold).value
        self.state['active'] = global_c.get('prime_mask', 0) & (1 << self.p) != 0
        
        # PPRIP enhancement: process assigned node states
        node_assignment = manifold.assign_nodes_to_primes()
        if self.p in node_assignment:
            node_ids = node_assignment[self.p]
            node_states = [manifold.get_node_states()[manifold.G.nodes().index(nid)] 
                          for nid in node_ids if nid in manifold.G.nodes()]
            processed_state = self.process(node_states)
            self.state['processed_state'] = processed_state
            
            # Update node states (simplified: average processed state with current state)
            for nid in node_ids:
                if nid in manifold.G.nodes():
                    idx = manifold.G.nodes().index(nid)
                    current_state = manifold.get_node_states()[idx]
                    new_state = 0.5 * (current_state + processed_state)
                    manifold.get_node_states()[idx] = new_state
