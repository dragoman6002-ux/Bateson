from setuptools import setup, find_packages

setup(
    name="pprip-qica",
    version="0.1.0",
    author="Daniel Dragolich",
    author_email="johnmayerdeadandcompany@gmail.com",
    description="A framework integrating number-theoretic resonance with graph-based information processing and meta-cognitive learning",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/your-repo-name",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.13",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    python_requires=">=3.13",
    install_requires=[
        "networkx>=3.5",
        "numpy>=2.3.0",
        "matplotlib>=3.9.0",
        "jupyter",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=22.0",
            "flake8>=4.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "pprip-qica=qica.engine:run_enhanced_qica_demonstration",
        ],
    },
)
