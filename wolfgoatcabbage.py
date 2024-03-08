from search import *

# Group Members: Kevin Nguyen, Joshua Duncan, Noah Khayat Albirkdar

# Last updated March 7, 2024


class WolfGoatCabbage(Problem):
    def __init__(self, initial=None, goal=None):
        """Initialize the problem with optional initial and goal states.
        The default initial state has the farmer (F), goat (G), wolf (W), and cabbage (C) on one side.
        The goal state is to have all moved to the opposite side, represented as an empty set.
        """
        if initial is None:
            initial = frozenset({"F", "G", "W", "C"})
        if goal is None:
            goal = frozenset({})
        super().__init__(initial, goal)

    def goal_test(self, state):
        """Check if the current state matches the goal state."""
        return state == self.goal

    def result(self, state, action):
        """Given a state and an action, compute and return the new state after applying the action.
        The action effectively moves the farmer and optionally one other item across the river.
        """
        new_state = set(state) ^ set(action)
        return frozenset(new_state)

    def actions(self, state):
        """Determine possible actions given the current state.
        An action is defined as the farmer moving across the river, optionally with one item.
        """
        available_actions = []
        farmer_location = "F"
        other_objects = set({"G", "W", "C"})

        # Remove the farmer to identify which objects are on the same side
        objects_on_same_side = [item for item in state if item != "F"]
        newState = frozenset(objects_on_same_side)

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
        valid_actions = []
        for action in available_actions:
            # If the action is just moving the farmer and not allowed by the state, skip it
            if action == frozenset({"F"}) and (
                state in [frozenset({"W"}), frozenset({"C"})]
            ):
                continue
            # Skip moving the cabbage with the farmer if both wolf and goat are present
            elif "F" in action and "C" in action and "W" in state and "G" in state:
                continue
            # Skip moving the wolf with the farmer if both wolf and cabbage are together without the goat
            elif (
                "F" in action
                and "W" in action
                and state in [frozenset({"W", "C"}), frozenset({"C", "W"})]
            ):
                continue
            else:
                valid_actions.append(action)
        return valid_actions


if __name__ == "__main__":

    wgc = WolfGoatCabbage()

    # Use depth-first and breadth-first search strategies to find a solution
    solution_dfs = depth_first_graph_search(wgc).solution()  # Find solution using DFS
    opt_sol_dfs = [
        set(state) for state in solution_dfs
    ]  # Convert each action set to a normal set for readability
    print("DFS Solution:", opt_sol_dfs)

    solution_bfs = breadth_first_graph_search(wgc).solution()  # Find solution using BFS
    opt_sol_bfs = [
        set(state) for state in solution_bfs
    ]  # Convert each action set to a normal set for readability
    print("BFS Solution:", opt_sol_bfs)
