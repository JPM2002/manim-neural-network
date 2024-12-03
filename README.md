# Manim Neural Network

A customizable neural network visualization library for Manim.

## Installation

Clone this repository and add it to your Python path. In  a minute i will make it so we can use pip to install it. BRB

## Usage

```python
from manim_neural_network.neural_network import NeuralNetworkMobject

class ExampleScene(Scene):
    def construct(self):
        neural_network = NeuralNetworkMobject([3, 5, 2])
        self.add(neural_network)

```
To run insert this in the terminal:

```bash
$ manim -pql neural_network.py SimpleNeuralNetworkScene
```
