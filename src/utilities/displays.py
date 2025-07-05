from worldobj import World
from utilities import progress_bar

import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
import json
import os

# A class used to record the simulation to a given folder.

class Displays:
    def __init__(self, directory, world: World):
        self.directory = directory
        self.world = world

        # initialise the folder
        count = 1
        while os.path.exists(self.directory):
            print(f'Directory "{self.directory}" already exists - Renaming to "{directory}({count})"')
            self.directory = f"{directory}({count})"
            count += 1

        print("Initialising directory - ", end = '')
        os.mkdir(self.directory)
        jsons_dir = self.directory + "/rounds_json"
        frames_dir = self.directory + "/rounds_frames"
        os.mkdir(jsons_dir)
        os.mkdir(frames_dir)

        # create a world_config file
        file_name = self.directory + "/world_config.json"
        with open(file_name, "w", encoding="utf-8") as config_file:
            config_file.write(json.dumps({
                "world_size": (self.world.width, self.world.height)
            }))
            config_file.close()
        
        # create a .gitignore
        file_name = self.directory + "/.gitignore"
        with open(file_name, "w", encoding="utf-8") as gitignore:
            gitignore.write("*")
            gitignore.close()
        
        print(f'Directory {self.directory} initialised')

    def export_round(self):
        round_data = self.world.export()
        round = round_data['round']
        file_name = f"{self.directory}/rounds_json/round_{round}.json"

        with open(file_name, "w", encoding="utf-8") as record_file:
            record_file.write(json.dumps(round_data))
            record_file.close()
    
    # generate the frames used to create the sim video in a seperate folder
    def gen_frames(self, identifier = None): 
        print("Generating frames:")
        # get world size
        with open(f"{self.directory}/world_config.json", "r", encoding="utf-8") as config_file:
            config = json.loads(config_file.read())
            config_file.close()
        x_range, y_range = config["world_size"] # to spec the x and y bounds of the plot
        round_files = os.listdir(f"{self.directory}/rounds_json/") # a list of all the round files

        count = 0
        total = len(round_files)
        for round_file_name in round_files:
            count += 1
            progress_bar(count,total)
            with open(f"{self.directory}/rounds_json/{round_file_name}", "r", encoding='utf-8') as round_file:
                round_data = json.loads(round_file.read())
                round_file.close()

            round_num = round_data['round']
            round_pop = round_data['population']                        

            colors = []
            markers: list[MarkerStyle]= []
            for entity in round_data["entities"]:
                if entity[2] == 0:
                    colors.append("red")
                    #markers.append(MarkerStyle("cross"))
                else:
                    colors.append("#"+entity[0][:6])
                    #markers.append(MarkerStyle("dot"))

            frame, axs = plt.subplots(1,1)
            frame.suptitle(f"Round: {round_num} | Population: {round_pop}")
            axs.set_xlim(0, x_range)
            axs.set_ylim(0, y_range)
            x = list(map(lambda entities: entities[1][0], round_data["entities"]))
            y = list(map(lambda entities: entities[1][1], round_data["entities"]))

            axs.scatter(x,y, s = 1, c = colors)
            

            frame.savefig(f"{self.directory}/rounds_frames/frame_{round_num}")
            plt.close(frame)
            del frame
            del axs
        print(f'\nDone - Frames exported to "{self.directory}/rounds_frames"')

    # use the previously generated frames to create a sim video
    def gen_video(self, fps: int):
        image_files = [f"{self.directory}/rounds_frames/frame_{frame}.png" for frame in range(len(os.listdir(f"{self.directory}/rounds_frames")))]
        clip = ImageSequenceClip(image_files, fps=fps)
        clip.write_videofile(f"{self.directory}/sim_recording.mp4", codec='libx264')

    # export a picture of the population graph
    def gen_pop_graph(self, identifier = None):
        print("Generating population graph - ", end = '')
        rounds = []
        population_change = []
        round_files = os.listdir(f"{self.directory}/rounds_json/") # a list of all the round files
        for round_file_name in round_files:
            with open(f"{self.directory}/rounds_json/{round_file_name}", "r", encoding='utf-8') as round_file:
                round_data = json.loads(round_file.read())
                round_file.close()

            round_num = round_data['round']
            round_pop = round_data['population']
            rounds.append(round_num)
            population_change.append(round_pop)
        
        graph, axs = plt.subplots(1,1)
        graph.suptitle("Population graph")
        axs.plot(rounds, population_change)
        axs.set_ylabel("Population")
        axs.set_xlabel("Rounds")
        graph.savefig(f"{self.directory}/population_graph")
        plt.close(graph)
        print(f'Graph generated in "{self.directory}"')