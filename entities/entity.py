from abc import ABC, abstractmethod

# an abstract class used as a template to create different species

# Receptors (methods) get input (e.g. surrounding entities density; the sensitivities are determined by gene)

# (Potentially a brain??? How to simulate logical thinking?)

# Prameters to the input layor (receptor neuron) (in_feature = <Whatever receptors are activated>, out_feature = <Whatever width are setted by gene>)
# Forward through the hidden layors (relay neuron) (depth determined by gene; weight determined by gene)
# But what algorithm should be used (Synapse connectivity)? Linear or none Linear (Relu, Sigmoid, or what)? Determined by gene?
# Output layor (effector neurones) (out_feature = <Whatever effectors are activated>)

# Effectors (methods) determin output (e.g. the directions; performance determined by gene)


class Entity(ABC):
    def __init__(self, genome: bytes):
        self.genome = genome
        # Set the hyperparameters of the nn and other attributes according to the genome:
    
    def inherit_from(self, parent_gene): # a method to make sure it inherits genes from its parent
        pass

    def check_surrounding(self):
        pass
