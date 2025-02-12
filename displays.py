import pandas as pd
import matplotlib.pyplot as plt
import json

# call after every round
def export_round(directory):
    '''Outputs a json file to the given directory containing the data of this round and a map of the distribution of the current population'''
    pass

# Used to import and visualise the results of a simulation

class Display:

    def __init__(self,directory):
        pass
    
    # generate the frames used to create the sim video in a seperate folder
    def gen_frames(self):
        pass

    # use the previously generated frames to create a sim video
    def gen_video(self):
        pass

    # export a picture of the population graph
    def gen_pop_graph(self):
        pass