from setuptools import setup, find_packages

setup(
    name="manim-neural-network",
    version="0.1.0",
    description="A library for visualizing neural networks in Manim",
    author="Javier Pozo Miranda",
    author_email="jdp5958@psu.edu",
    url="https://github.com/JPM2002/manim-neural-network",
    packages=find_packages(),
    install_requires=[
        "manim",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
