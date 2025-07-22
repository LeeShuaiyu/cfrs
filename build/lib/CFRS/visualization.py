import numpy as np
import matplotlib.pyplot as plt
from .density import compute_target_density
from scipy import stats

def visualize_results(samples, char_func, h):
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    # 1. Histogram vs Target Density
    ax1 = axes[0, 0]
    x_grid = np.linspace(np.min(samples) - 1, np.max(samples) + 1, 1000)
    target_density = compute_target_density(char_func, h, x_grid)
    ax1.hist(samples, bins=50, density=True, alpha=0.7, color='skyblue', label='CFRS Sample Histogram')
    ax1.plot(x_grid, target_density, 'r-', linewidth=2, label='Target Density')
    ax1.set_xlabel('x')
    ax1.set_ylabel('Density')
    ax1.set_title(f'CFRS Sample Histogram vs Target Density (h={h})')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    # 2. QQ Plot
    ax2 = axes[0, 1]
    stats.probplot(samples, dist="norm", plot=ax2)
    ax2.set_title('Q-Q Plot (vs Normal Distribution)')
    ax2.grid(True, alpha=0.3)
    # 3. Sample Trajectory (Cumulative Sum)
    ax3 = axes[1, 0]
    cumsum = np.cumsum(samples[:1000])
    ax3.plot(cumsum, 'b-', alpha=0.7)
    ax3.set_xlabel('Time Step')
    ax3.set_ylabel('Cumulative Value')
    ax3.set_title('Sample Path (Cumulative Sum)')
    ax3.grid(True, alpha=0.3)
    # 4. Characteristic Function Visualization
    ax4 = axes[1, 1]
    u_vals = np.linspace(-5, 5, 1000)
    phi_1 = [char_func.phi(u) for u in u_vals]
    phi_h = [char_func.phi_h(u, h) for u in u_vals]
    ax4.plot(u_vals, np.real(phi_1), 'g-', label=f'Re(phi_1(u))')
    ax4.plot(u_vals, np.real(phi_h), 'r-', label=f'Re(phi_{h}(u))')
    ax4.set_xlabel('u')
    ax4.set_ylabel('phi(u)')
    ax4.set_title('Characteristic Function')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show() 