from search import *

# Group Members: Kevin Nguyen, Joshua Duncan, Noah Khayat Albirkdar

# Last updated March 7, 2024


class WolfGoatCabbage(Problem):
    def __init__(self, initial=None, goal=None):
        """Define initial and goal states"""
        if initial is None:
            initial = frozenset({"F", "G", "W", "C"})
        if goal is None:
            goal = frozenset({})
        super().__init__(initial, goal)

    def goal_test(self, state):
        """Check if the current state is the goal state"""
        return state == self.goal

    def result(self, state, action):
        """Given a state and an action, return the new state"""
        new_state = set(state) ^ set(action)
        return frozenset(new_state)

    def actions(self, state):
        """Return possible actions in a given state"""
        available_actions = []
        farmer_location = "F"
        other_objects = set({"G", "W", "C"})

        list = []
        for item in state:
            if not item == "F":
                list.append(item)
        newState = frozenset(list)

        if "F" in state:
            # Farmer is on the left bank, options to move objects from left to right
            for obj in newState:
                if not (obj == "W" and "G" in newState and "C" in newState):
                    available_actions.append(frozenset({farmer_location, obj}))

        else:
            # Farmer is on the right bank, options to move objects from right to left
            for obj in other_objects - state:
                available_actions.append(frozenset({farmer_location, obj}))
            if not frozenset({"W"}) == newState:
                available_actions.append(frozenset({farmer_location}))

        # Filter out actions where the goat and the wolf or the goat and the cabbage are left alone
        for action in available_actions:
            if frozenset({"F"}) == action:
                if "F" in state:
                    available_actions.remove(action)
                elif frozenset({"W"}) == state:
                    available_actions.remove(action)
                elif frozenset({"C"}) == state:
                    available_actions.remove(action)
            if "F" in action and "C" in action:
                if "W" in state and "G" in state:
                    available_actions.remove(action)
            if "F" in action and "W" in action:
                if frozenset({"W", "C"}) == state or frozenset({"C", "W"}) == state:
                    available_actions.remove(action)
        return available_actions


if __name__ == "__main__":

    wgc = WolfGoatCabbage()

    # solution() is a function in class node that returns the sequence of actions
    # its already frozen list
    solution = depth_first_graph_search(wgc).solution()
    opt_sol = [set(state) for state in solution]  # converting each node to normal set
    print(opt_sol)
    solution = breadth_first_graph_search(wgc).solution()
    opt_sol1 = [set(state) for state in solution]
    print(opt_sol1)
