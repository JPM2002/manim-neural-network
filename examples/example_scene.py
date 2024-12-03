from manim import *
from manim_neural_network.neural_network import NeuralNetworkMobject

class ExampleScene(Scene):
    def construct(self):
        neural_network = NeuralNetworkMobject([3, 5, 2])
        neural_network.move_to(ORIGIN)

        self.play(FadeIn(neural_network))
        self.wait(1)
