from manim import *
import itertools as it

# A customizable Sequential Neural Network
class NeuralNetworkMobject(VGroup):
    def __init__(self, neural_network, **kwargs):
        super().__init__(**kwargs)
        self.layer_sizes = neural_network
        self.neuron_radius = 0.15
        self.neuron_to_neuron_buff = 0.2
        self.layer_to_layer_buff = 1.0
        self.output_neuron_color = WHITE
        self.input_neuron_color = WHITE
        self.hidden_layer_neuron_color = WHITE
        self.neuron_stroke_width = 2
        self.neuron_fill_opacity = 1
        self.edge_color = LIGHT_GREY
        self.edge_stroke_width = 2
        self.add_neurons()
        self.add_edges()
        self.add_to_back(self.layers)

    def add_neurons(self):
        layers = VGroup(*[
            self.get_layer(size, index)
            for index, size in enumerate(self.layer_sizes)
        ])
        layers.arrange(RIGHT, buff=self.layer_to_layer_buff)
        self.layers = layers

    def get_nn_fill_color(self, index):
        if index == 0:
            return self.input_neuron_color
        elif index == len(self.layer_sizes) - 1:
            return self.output_neuron_color
        else:
            return self.hidden_layer_neuron_color

    def get_layer(self, size, index=-1):
        layer = VGroup()
        neurons = VGroup(*[
            Circle(
                radius=self.neuron_radius,
                stroke_color=self.get_nn_fill_color(index),
                stroke_width=self.neuron_stroke_width,
                fill_color=BLACK,
                fill_opacity=self.neuron_fill_opacity,
            )
            for _ in range(size)
        ])
        for neuron in neurons:
            neuron.z_index = 1  # Ensure neurons are in front of edges
        neurons.arrange(DOWN, buff=self.neuron_to_neuron_buff)
        layer.neurons = neurons
        layer.add(neurons)
        return layer


    def add_edges(self):
        self.edge_groups = VGroup()
        for l1, l2 in zip(self.layers[:-1], self.layers[1:]):
            edge_group = VGroup()
            for n1, n2 in it.product(l1.neurons, l2.neurons):
                edge = Line(
                    n1.get_center(),
                    n2.get_center(),
                    stroke_color=self.edge_color,
                    stroke_width=self.edge_stroke_width,
                )
                edge.z_index = 0  # Set edges to a lower z-index
                edge_group.add(edge)
            self.edge_groups.add(edge_group)
        self.add(self.edge_groups)  # Add edges first



    def label_inputs(self, label):
        for i, neuron in enumerate(self.layers[0].neurons):
            text = MathTex(f"{label}_{{{i + 1}}}")
            text.set_height(0.3)
            text.next_to(neuron, LEFT)
            self.add(text)

    def label_outputs(self, label):
        for i, neuron in enumerate(self.layers[-1].neurons):
            text = MathTex(f"{label}_{{{i + 1}}}")
            text.set_height(0.3)
            text.next_to(neuron, RIGHT)
            self.add(text)


# Need to add this

    def label_layers(self, labels, input_size=0.4, hidden_size=0.25, output_size=0.4):
        """
        Adds labels above each layer to describe its role, with specific sizes for input, hidden, and output layers.
        Default values are used if no specific size is provided.
        """
        label_objects = VGroup()  # Group all labels to manage them together
        for i, (label_text, layer) in enumerate(zip(labels, self.layers)):
            label = Text(label_text)
            
            # Set the size based on the layer type
            if i == 0:  # Input layer
                label.scale(input_size)
            elif i == len(self.layers) - 1:  # Output layer
                label.scale(output_size)
            else:  # Hidden layers
                label.scale(hidden_size)
            
            label.next_to(layer, UP)  # Place the label above the layer
            label_objects.add(label)  # Add the label to the group

        self.add(label_objects)  # Add the group of labels to the scene
        return label_objects  # Return the labels for further animation if needed