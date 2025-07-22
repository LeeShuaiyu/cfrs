from setuptools import setup, find_packages

setup(
    name='cfrs',
    version='0.1.0',
    description='CFRS: Characteristic Function-based Random Sampling Library',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'scipy',
    ],
    python_requires='>=3.7',
    url='https://github.com/yourusername/cfrs',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
) 