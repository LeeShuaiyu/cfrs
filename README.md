# CFRS

基于特征函数的随机采样与可视化库。

## 功能简介
- 支持通过自定义特征函数、采样频率h和样本数，生成观测增量样本。
- 提供目标密度反演与多种可视化功能。

## 安装
```bash
pip install .
```

## 快速开始
```python
from cfrs.characteristic import StudentTCharFunc
from cfrs.sampling import CFRSSampler
from cfrs.visualization import visualize_results

# 定义特征函数
char_func = StudentTCharFunc(mu=0, sigma=1, nu=4)
h = 0.01
sampler = CFRSSampler(char_func, h)
samples = sampler.sample(1000)

# 可视化
visualize_results(samples, char_func, h)
```

## 许可证
MIT License 