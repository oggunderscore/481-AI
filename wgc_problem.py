from search import *

# Standardized Templated Design generated by Copilot
# Group Members: Kevin Nguyen, Joshua Duncan, Noah Khayat Albirkdar

# Last updated March 4, 2024


class WolfGoatCabbage(Problem):
    def __init__(self, initial=None, goal=None):
        """Define initial and goal states"""
        """define initial and goal states as frozensets or tuple to match sets in DFS """
        if initial is None:
            #frozenset making the normal set as tuple(unchanged set like shit )
            #initial = {"F", "G", "W", "C"}
            initial = frozenset({"F", "G", "W", "C"}) # or use tuple(sorted(["F", "G", "W", "C"]))
        if goal is None:
            #goal = {}
            goal = frozenset({})
        super().__init__(initial, goal)

    def goal_test(self, state):
        """Check if the current state is the goal state"""

        return state == self.goal

    def result(self, state, action):
        """Given a state and an action, return the new state"""
        """the state has to be returned frozenset or tuple like to be compatible with set in DFS"""
        # convert frozenset to normal set to update it because tuple/frozenset is fixed 
        #adding new line state_set = set(state)
        state_set = set(state)
        new_state = set(state_set) ^ set(action)
        #return new_state
        return frozenset(new_state) # or tuple(sorted(new_state)) it has to be sorted 

    def actions(self, state):
        """Return possible actions in a given state"""
        available_actions = []
        farmer_location = "F"
        other_objects = set(state) - {"F"}

        if "F" in state:
            # Farmer is on the left bank, options to move objects from left to right
            #for obj in other_objects:
                #available_actions.append({farmer_location, obj})
            available_actions = [{farmer_location} | {obj} for obj in other_objects] + [{"F"}]
        else:
            # Farmer is on the right bank, options to move objects from right to left
            #for obj in other_objects:
                #available_actions.append({farmer_location, obj})
            available_actions = [{farmer_location} | {obj} for obj in other_objects] + [{"F"}]


        # Filter out actions where the goat and the wolf or the goat and the cabbage are left alone
        valid_actions = []
        for action in available_actions:
            new_state = set(state) ^ set(action)
            #if ("G" in action and "W" in action) or ("G" in action and "C" in action):
                #available_actions.remove(action)
            if not ("G" in new_state and "W" in new_state) and not ("G" in new_state and "C" in new_state):
                valid_actions.append(action)

        return available_actions


# Test Example usage:
#initial_state = {"F", "G", "W", "C"}
# goal_state = {"G", "W", "C", "F"}
#wgc = WolfGoatCabbage()
#print(wgc.actions(initial_state))
#state_1 = wgc.result(initial_state, {"F", "G"})
#print(state_1)
#print(wgc.result(wgc.result(initial_state, {"F", "G"}), {"F"}))
#state_2 = wgc.result(state_1, {})
#print(state_2)
#state_2 = wgc.result(state_1, {"F"})
#print(state_2)

#state_3 = wgc.result(state_2, {"F", "C"})
#print(state_3)
#state_4 = wgc.result(state_3, {"F", "G"} )
#print(state_4)
#state_5 = wgc.result(state_4, {"F", "W"})
#print(state_5)
#state_6 = wgc.result(state_5, "F")
#print(state_6)
#state_7 = wgc.result(state_6, {"F", "G"})
#print(state_7)
#print(wgc.goal_test({}))

# This needs to be fixed somehow...
# print(depth_first_graph_search(wgc).solution())

if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    #solution() is a function in class node that returns the sequence of actions  
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    #solution = breadth_first_graph_search(wgc).solution()
    #print(solution)
