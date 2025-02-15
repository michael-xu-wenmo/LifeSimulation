import matplotlib.pyplot as plt
import json
import os

class Displays:
    def __init__(self, directory, world):
        
        self.directory = directory
        self.world = world

        # initiate the folder
        try:
            print("Initialise directory...")
            os.mkdir(self.directory)
            jsons_dir = self.directory + "/rounds_json"
            frames_dir = self.directory + "/rounds_frames"
            os.mkdir(jsons_dir)
            os.mkdir(frames_dir)
        except FileExistsError:
            print("Directory Exits")

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

    def export_round(self):
        round_data = self.world.export()
        round = round_data['round']
        file_name = f"{self.directory}/rounds_json/round_{round}.json"

        with open(file_name, "w", encoding="utf-8") as record_file:
            record_file.write(json.dumps(round_data))
            record_file.close()
    
    # generate the frames used to create the sim video in a seperate folder
    def gen_frames(self):
        # get world size
        with open(f"{self.directory}/world_config.json", "r", encoding="utf-8") as config_file:
            config = json.loads(config_file.read())
            config_file.close()
        x_range, y_range = config["world_size"] # to spec the x and y bounds of the plot
        round_files = os.listdir(f"{self.directory}/rounds_json/") # a list of all the round files

        for round_file_name in round_files:
            with open(f"{self.directory}/rounds_json/{round_file_name}", "r", encoding='utf-8') as round_file:
                round_data = json.loads(round_file.read())
                round_file.close()

            # unfinished

    # use the previously generated frames to create a sim video
    def gen_video(self):
        pass

    # export a picture of the population graph
    def gen_pop_graph(self):
        pass