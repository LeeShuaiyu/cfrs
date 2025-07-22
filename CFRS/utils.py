import numpy as np

def compute_cfrs_constants(char_func, h, u_max=5, n_points=1000):
    u_grid = np.linspace(-u_max, u_max, n_points)
    du = u_grid[1] - u_grid[0]
    phi_h_vals = char_func.phi_h(u_grid, h)
    phi_h_vals = np.where(np.isfinite(phi_h_vals), phi_h_vals, 0)
    phi_h_vals = np.where(np.abs(phi_h_vals) > 1e-15, phi_h_vals, 0)
    c = np.trapz(np.abs(phi_h_vals), u_grid) / (2 * np.pi)
    phi_h_real = np.real(phi_h_vals)
    d2_real = np.gradient(np.gradient(phi_h_real, du), du)
    k = np.trapz(np.abs(d2_real), u_grid) / (2 * np.pi)
    c = np.clip(c, 1e-6, 100)
    k = np.clip(k, 1e-6, 1000)
    return c, k, u_grid, phi_h_vals

def envelope_function(x, c, k):
    return np.minimum(c, k / (x**2 + 1e-10)) 