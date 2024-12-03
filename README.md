Manim Neural Network
A customizable neural network visualization library for Manim Community Edition.

Installation
System Requirements
Linux: Before installing, ensure xdg-utils is installed. This is required for Manim Community Edition to open rendered videos automatically. Install it using:
sudo apt install xdg-utils
Windows: No additional system-level dependencies are required beyond Manim Community Edition.
For both Linux and Windows, you need to install the Manim Community Edition. Follow the official instructions here: Manim Installation Guide.

Install the Package
Once Manim is installed, you can install this package using pip:

pip install manim-neural-network==0.1.0
This package extends Manim by providing tools to easily create and visualize neural networks.

Usage
After installing, you can use the library in your Python scripts. Here's an example:

from manim import *
from manim_neural_network.neural_network import NeuralNetworkMobject

class ExampleScene(Scene):
    def construct(self):
        # Define a neural network with 3 input neurons, 5 hidden neurons, and 2 output neurons
        neural_network = NeuralNetworkMobject([3, 5, 2])
        self.add(neural_network)
Running the Example
Save the script (e.g., example.py) and run it in the terminal using Manim:

manim -pql example.py ExampleScene
-pql: Play the animation in low quality after rendering.
Replace example.py with the name of your file and ExampleScene with your class name if different.
Features
Easily define and visualize fully connected neural networks.
Customize neuron and edge properties like colors, radius, and spacing.
Label input and output neurons programmatically.
Requirements
Python 3.7 or later
Manim Community Edition (v0.17 or later)
Install Manim using:

pip install manim
For more details, visit the Manim Community Documentation.

Example Output
Here is an example visualization generated using this library:

3-5-2 Neural Network

