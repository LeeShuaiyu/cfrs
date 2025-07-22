import numpy as np

class CharacteristicFunction:
    """特征函数基类"""
    def phi(self, u):
        raise NotImplementedError
    
    def phi_h(self, u, h):
        """h时间步长的特征函数"""
        return np.power(self.phi(u), h)

class StudentTCharFunc(CharacteristicFunction):
    """简化但稳定的Student-t特征函数实现"""
    def __init__(self, mu, sigma, nu):
        self.mu = mu
        self.sigma = sigma
        self.nu = nu
    
    def phi(self, u):
        u = np.asarray(u)
        result = np.zeros_like(u, dtype=complex)
        zero_mask = (np.abs(u) < 1e-12)
        result[zero_mask] = 1.0
        nonzero_mask = ~zero_mask
        if np.any(nonzero_mask):
            u_nz = u[nonzero_mask]
            phase = 1j * u_nz * self.mu
            scaled_u = self.sigma * u_nz
            abs_scaled_u = np.abs(scaled_u)
            if self.nu > 2:
                effective_var = self.nu / (self.nu - 2)
                gaussian_part = np.exp(-0.5 * effective_var * scaled_u**2)
                tail_correction = np.power(1 + abs_scaled_u**2 / self.nu, -self.nu/4)
                amplitude = gaussian_part * tail_correction
            else:
                amplitude = np.power(1 + abs_scaled_u**2, -self.nu/2)
            result[nonzero_mask] = np.exp(phase) * amplitude
        return result 