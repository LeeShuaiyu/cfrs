# CFRS: Characteristic Function-based Random Sampling Library

## Overview
CFRS is a Python library for generating random samples from distributions specified by their characteristic functions (CFs). It supports custom CFs, flexible sampling frequency, and provides visualization tools for both the generated samples and the target density. The library is suitable for simulating increments of Lévy processes and other distributions where only the CF is known.

## Installation

### From GitHub (recommended for latest version)
```bash
git clone https://github.com/yourusername/cfrs.git
cd cfrs
pip install .
```

### Directly via pip (if on PyPI)
```bash
pip install cfrs
```

### Development mode (for contributors)
```bash
pip install -e .
```

## Usage Example

```python
import numpy as np
from cfrs.characteristic import StudentTCharFunc
from cfrs.sampling import CFRSSampler
from cfrs.density import compute_target_density
from cfrs.visualization import visualize_results

# 1. Define the characteristic function (Student-t example)
mu = 0.0
sigma = 1.0
nu = 4.0
h = 0.01
char_func = StudentTCharFunc(mu, sigma, nu)

# 2. Generate samples
sampler = CFRSSampler(char_func, h)
samples = sampler.sample(2000)
print(f"Generated {len(samples)} samples.")

# 3. Compute target density (optional)
x_grid = np.linspace(np.min(samples)-1, np.max(samples)+1, 500)
target_density = compute_target_density(char_func, h, x_grid)

# 4. Visualization
visualize_results(samples, char_func, h)
```

## How It Works
- **CFRS (Characteristic Function-based Random Sampling)** uses the inversion formula and envelope-rejection sampling to generate random variables from a given characteristic function.
- The algorithm numerically inverts the CF to approximate the target density, then uses a carefully constructed envelope function to efficiently accept/reject candidate samples.
- The library is modular: you can plug in any custom CF by subclassing `CharacteristicFunction`.

## Application Scope
- Simulation of increments for Lévy processes and other infinitely divisible distributions.
- Random number generation for distributions where only the CF is available or the PDF is intractable.
- Statistical research, Monte Carlo methods, and computational finance.

## References
- Devroye, L. (1981). On the computer generation of random variables with a given characteristic function. *Computers & Mathematics with Applications*, 7(6), 547-552. [link](https://doi.org/10.1016/0898-1221(81)90014-4)
- Li, S., Wu, Y., & Cheng, Y. (2024). Parameter estimation and random number generation for student Lévy processes. *Computational Statistics & Data Analysis*, 194, 107933. [link](https://doi.org/10.1016/j.csda.2023.107933)

## License
MIT License 