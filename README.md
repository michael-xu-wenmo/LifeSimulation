This is a simulation of natural selection. 
There will be entities with different Genes.

There will be a little neuro network for each entity to control their actions.
However, one can also explicitly code the brain of one's species and see if they would do well.

The world object consists of a 2D numpy array to map each Loc (location).
Each location object can hold one food and one entity (Food not implemented yet).

For each round, the Loc will update the receptors in the Entity object (How to optimise???)
Then, each Entity will be given an exclusive time (in some order) to process their reactions (How to optimise??? Should I use multithreading? What is the point of multithreading? There is a GIL anyway).
Then, a request of corresponding reaction will be sent it the Loc.
The world will then resolve the requests in each Loc. 
Then export it's state to a json file.