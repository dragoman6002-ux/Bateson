class EnhancedPiCore(PiCore):
    """
    Enhanced version of PiCore with PPRIP resonance analysis.
    """
    def __call__(self, manifold) -> CoreMetric:
        # Original implementation
        cycles = manifold.pi_resonant_cycles()
        best = min((abs(hr-1.0), L) for L,hr in cycles)[0] if cycles else 1.0
        
        # PPRIP enhancement: analyze graph for π-resonance
        min_dev_pi = float('inf')
        for cycle in nx.cycle_basis(manifold.G):
            L = len(cycle)
            k_opt = round(L / (2 * PI))
            dev = abs(L - 2 * PI * k_opt)
            if dev < min_dev_pi:
                min_dev_pi = dev
        
        # Combine both metrics
        combined_metric = (best + min_dev_pi) / 2
        return CoreMetric(combined_metric, 0.05, "π")

class EnhancedPhiCore(PhiCore):
    """
    Enhanced version of PhiCore with PPRIP φ-optimization analysis.
    """
    def __call__(self, manifold) -> CoreMetric:
        # Original implementation
        err = manifold.golden_adjacency()
        
        # PPRIP enhancement: analyze node states for φ-optimization
        node_states = manifold.get_node_states()
        if node_states:
            # Analyze growth rate of cumulative sum of state magnitudes
            state_mags = [np.linalg.norm(s) for s in node_states]
            cumsum = np.cumsum(state_mags)
            if len(cumsum) >= 2 and cumsum[-2] != 0:
                growth_rate = cumsum[-1] / cumsum[-2]
                dev_phi = abs(growth_rate - PHI)
                # Combine both metrics
                combined_metric = (err + dev_phi) / 2
            else:
                combined_metric = err
        else:
            combined_metric = err
        
        return CoreMetric(combined_metric, 0.1, "φ")

class EnhancedOmegaCore(OmegaCore):
    """
    Enhanced version of OmegaCore with PPRIP complexity analysis.
    """
    def __call__(self, manifold) -> CoreMetric:
        # Original implementation
        omega = manifold.omega_complexity()
        
        # PPRIP enhancement: variance of node states
        node_states = manifold.get_node_states()
        if node_states:
            omega_proxy = float(np.var(np.concatenate([s.flatten() for s in node_states])))
            # Combine both metrics
            combined_metric = (omega + omega_proxy) / 2
        else:
            combined_metric = omega
        
        return CoreMetric(combined_metric, 1e6, "Ω")

class EnhancedBetaCore(BetaCore):
    """
    Enhanced version of BetaCore with PPRIP topological analysis.
    """
    def __call__(self, manifold) -> CoreMetric:
        # Original implementation
        b1 = manifold.betti1()
        
        # PPRIP enhancement: cycle basis size
        beta1_proxy = len(nx.cycle_basis(manifold.G))
        
        # Combine both metrics
        combined_metric = float(b1 > 0 and beta1_proxy > 0)
        return CoreMetric(combined_metric, 1.0, "β")
