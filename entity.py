from abc import ABC, abstractmethod
import random

# an abstract class used as a template to create different species

# Receptors (inner attributes) passively receives input from the Loc (e.g. surrounding entities density; the sensitivities are determined by gene)

# (Potentially a brain??? How to simulate logical thinking?)

# Prameters to the input layor (receptor neuron) (in_feature = <Whatever receptors are activated>, out_feature = <Whatever width are setted by gene>)
# Forward through the hidden layors (relay neuron) (depth determined by gene; weight determined by gene)
# But what algorithm should be used (Synapse connectivity)? Linear or none Linear (Relu, Sigmoid, or what)? Determined by gene?
# Output layor (effector neurones) (out_feature = <Whatever effectors are activated>)

# Effectors (methods) determin output (e.g. the directions; performance determined by gene)


class Entity(object):
    def __init__(self, genome):
        # god defined attribute:
        self._genome = genome # Sets the hyperparameters of the nn and other attributes according to the genome

        # physical attributes: defined by the gene. The entity cannot even change it.
        self.act_eff_neu = {"move":(0,0)}
        self.act_rec_neu = {"pos":(), "reach":[], "sight":[]}
        self.SIGHT = 1
        self.REACH = 1
        self.SPEED = 1 # locs per round

        # inner state
        self.engery = None

    def do(self):
        # move randomly
        d_x = random.randint(-1,1)
        d_y = random.randint(-1,1)
        x = random.randint(0,self.SPEED) * d_x
        y = random.randint(0,self.SPEED) * d_y
        self.act_eff_neu['move'] = (x,y)
        return self.act_eff_neu