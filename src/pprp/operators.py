class EnhancedTransputation(Transputation):
    """
    Enhanced version of Transputation with PPRIP emergence detection.
    """
    def __call__(self, omega_metric, beta_metric, options: PPRIPOptions) -> Optional[str]:
        # Original implementation
        if omega_metric.value > omega_metric.threshold and beta_metric.value:
            return "⟡ insight: π-φ-prime resonance achieved – self-loop resolved"
        
        # PPRIP enhancement: check for emergence based on thresholds
        if omega_metric.value > options.thresh_omega and beta_metric.value >= options.thresh_beta1:
            return "⟡ insight: PPRIP emergence detected – system in resonant state"
        
        return None

class EnhancedRealitySelection(RealitySelection):
    """
    Enhanced version of RealitySelection with PPRIP coupling.
    """
    def __call__(self, coherence: float, choices: list, options: PPRIPOptions) -> str:
        # Original implementation with PPRIP coupling strength
        weights = [coherence + options.coupling_strength * (1-coherence) * random.random() 
                  for _ in choices]
        return random.choices(choices, weights=weights, k=1)[0]

class EnhancedAwareness(Awareness):
    """
    Enhanced version of Awareness with PPRIP state tracking.
    """
    def __call__(self, global_c: dict, metrics: list, manifold):
        # Original implementation
        global_c['self_model'] = {m.axiom_id: m.value for m in metrics}
        global_c['timestamp'] += 1
        
        # PPRIP enhancement: track node states and graph properties
        global_c['node_states'] = manifold.get_node_states()
        global_c['graph_info'] = {
            'nodes': list(manifold.G.nodes()),
            'edges': list(manifold.G.edges()),
            'num_nodes': manifold.G.number_of_nodes(),
            'num_edges': manifold.G.number_of_edges()
        }
