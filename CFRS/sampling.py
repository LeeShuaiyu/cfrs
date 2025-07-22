import numpy as np
from .utils import compute_cfrs_constants

class CFRSSampler:
    def __init__(self, char_func, h):
        self.char_func = char_func
        self.h = h
    
    def sample(self, n_samples, max_attempts=None):
        if max_attempts is None:
            max_attempts = n_samples * 50
        c, k, _, _ = compute_cfrs_constants(self.char_func, self.h, u_max=3, n_points=500)
        if c < 1e-8 or k < 1e-8:
            raise ValueError(f"Constants too small: c={c}, k={k}")
        accepted_samples = []
        attempts = 0
        while len(accepted_samples) < n_samples and attempts < max_attempts:
            v1 = np.random.uniform(-1, 1)
            v2 = np.random.uniform(-1, 1)
            if abs(v2) < 1e-6:
                v2 = 1e-6 * np.sign(v2)
            y = np.sqrt(k/c) * v1 / v2
            if np.abs(y) > 5:
                attempts += 1
                continue
            target_val = np.abs(self.char_func.phi_h(y, self.h))
            envelope_val = min(c, k / (y**2 + 1e-8))
            if envelope_val < 1e-12:
                attempts += 1
                continue
            accept_prob = min(target_val / envelope_val, 1.0)
            u = np.random.uniform(0, 1)
            if u <= accept_prob:
                accepted_samples.append(y)
            attempts += 1
        if len(accepted_samples) < n_samples:
            raise RuntimeError(f"Only {len(accepted_samples)} samples generated after {attempts} attempts.")
        return np.array(accepted_samples) 