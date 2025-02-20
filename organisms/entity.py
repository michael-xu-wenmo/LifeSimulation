from abc import ABC, abstractmethod

# an abstract class used as a template to create different species

# Receptors (inner attributes) passively receives input from the Loc (e.g. surrounding entities density; the sensitivities are determined by gene)

# Potentially a way to simulate learning as well as natural selection? The time complexity will be insane.

# Prameters to the input layor (receptor neuron) (in_feature = <Whatever receptors are activated>, out_feature = <Whatever width are setted by gene>)
# Forward through the hidden layors (relay neuron) (depth determined by gene; weight determined by gene)
# But what algorithm should be used (Synapse connectivity)? Linear or none Linear (Relu, Sigmoid, or what)? Determined by gene?
# Output layor (effector neurones) (out_feature = <Whatever effectors are activated>)

# Effectors (methods) determin output (e.g. the directions; performance determined by gene)

# GENE ENCODING:
# "{Receptor stats}|{Input layor}|{Hidden layor}|{Output layor}|{Effector stats}"
# Receptors: b"\{GlOBAL_POSITION}\{SIGHT}\{REACH}\" Could add more in the futur
# Input Layor: b"\{Output Width}\{Wiring Matrix}"
# Hidden Lyour: b"\{Depth}\{Wiring Matrix}"
# Output Layour: b"\"{Wiring Matrix}"
# Effectors: b"\{MOVE}\{EAT}\{KILL}" Could add more in the futur

SENSORS: list[str] = ["sight", "reach", "global_position"]
# global_position: if <128 then off else on
# sight: the Locs around it that it can see (see meaning have access to the Loc's information which includes the entity it stores and the entity's geter functions)
# reach: the Locs around it that it can reach(hence apply its effectors of "eat" and "kill")

EFFECTORS: list[str]= ["move", "eat", "reproduce", "kill"]
# move: the range it can go each round
# eat: the nutrition multiplier it gets from food
# reproduce: the number of offsprings one can reproduce 

class Entity(ABC):

    def __init__(self, genome: str, pos: tuple[int,int], disabled: list[str] = []):
        # god defined attribute:
        self.genome: str = genome # Sets the hyperparameters of the nn and other attributes according to the genome
        self.pos: tuple[int, int] = pos # a utility attribute that only the World/Loc should access. The entity itself shouldn't use it.
 
        self.points = 0 # inner stat

        sensor_code, input_code, hidden_code, output_code, effector_code = self.genome.split('|')
        # sensors created with corresponding sensor strengths
        sensor_code = bytes.fromhex(sensor_code)
        self.sensor_attri: dict[str, int] = {SENSORS[sensor_count]: sensor_code[sensor_count] for sensor_count in range(len(sensor_code)) if SENSORS[sensor_count] not in disabled}
        self.sensor: dict[str, list] = {SENSORS[sensor_count]: [] for sensor_count in range(len(sensor_code)) if SENSORS[sensor_count] not in disabled}

        # effectors created with corresponding effector strength
        effector_code = bytes.fromhex(effector_code)
        self.effectors_attri: dict[str, int] = {EFFECTORS[effector_count]: effector_code[effector_count] for effector_count in range(len(effector_code)) if EFFECTORS[effector_count] not in disabled}
        self.effectors: dict[str, list] = {EFFECTORS[effector_count]: [] for effector_count in range(len(effector_code)) if EFFECTORS[effector_count] not in disabled}

        # Neurons (unimplemented yet :( )
    
    # seter function to give input

    def receive(self, sensor:str, value:list) -> dict[str, list]:
        self.sensor[sensor] = value
        return self.sensor

    # geter functions
    def get_genome(self) -> str:
        return self.genome
    
    def get_pos(self) -> tuple[int, int]:
        return self.pos
    
    def get_points(self) -> int:
        return self.points
    
    def get_sensor_attri(self, sensor:str) -> int:
        return self.sensor_attri[sensor]
    
    def get_effectors_attri(self, effector:str)  -> int:
        return self.effectors_attri[effector]
    
    @abstractmethod
    def __call__(self) -> dict[str, list]:
        return self.effectors