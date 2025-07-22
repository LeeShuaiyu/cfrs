import numpy as np

def compute_target_density(char_func, h, x_grid, u_max=8):
    n_points = 512
    u_vals = np.linspace(-u_max, u_max, n_points)
    phi_vals = char_func.phi_h(u_vals, h)
    phi_vals = np.where(np.isfinite(phi_vals), phi_vals, 0)
    densities = np.zeros_like(x_grid, dtype=float)
    for i, x in enumerate(x_grid):
        integrand = phi_vals * np.exp(-1j * u_vals * x)
        integral = np.trapz(integrand, u_vals)
        density_val = np.real(integral) / (2 * np.pi)
        densities[i] = max(density_val, 0)
    if len(densities) > 5:
        window = 3
        smoothed = np.zeros_like(densities)
        for i in range(len(densities)):
            start = max(0, i - window//2)
            end = min(len(densities), i + window//2 + 1)
            smoothed[i] = np.mean(densities[start:end])
        densities = smoothed
    total_area = np.trapz(densities, x_grid)
    if total_area > 1e-8:
        densities = densities / total_area
    return densities 