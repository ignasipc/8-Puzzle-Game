import copy


class State:
    # All possible movements of the blank peace (number '0')
    movements = {
        -3: "UP",
        +1: "RIGHT",
        +3: "DOWN",
        -1: "LEFT"
    }

    # All possible displacements the blank piece can do
    displacements = {
        -3, # Up
        +1, # Right
        +3, # Down
        -1  # Left
    }

    def __init__(self, dimension, combination, solution):
        self.dimension = dimension
        self.combination = combination
        self.solution = solution

        self.moves = []

    def __hash__(self):
        return hash(tuple(self.combination))


    def __eq__(self, other):
        return self.combination == other.combination


    def legal_move(self, displacement) -> bool:
        """
        Determine if a move can be done or not.
        :param displacement: Displacement of the blank peace or 0
        :return: True if the displacement falls between position 0 and the combination's lenth
        """
        if 0 <= self.combination.index(0) + displacement < len(self.combination):
            return True
        return False


    def is_goal(self):
        return self.combination == self.solution


    def transition(self, displacement):
        # If not a legal movement, we return
        if not self.legal_move(displacement):
            return None

        new_state = copy.deepcopy(self)

        # Get the empty piece position and the piece's number that will be moved
        empty_space_pos = new_state.combination.index(0)
        moving_number = new_state.combination[empty_space_pos+displacement]

        # Logical move of the peace
        combination_list = list(new_state.combination)
        combination_list[empty_space_pos] = moving_number
        combination_list[empty_space_pos+displacement] = 0

        # Change new state's combination and add the movement taken
        new_state.combination = combination_list
        new_state.moves.append(self.movements[displacement])

        return new_state


    def generate_children(self):
        generated_states = []

        for movement in self.displacements:
            child = self.transition(movement)

            if child is not None:
                generated_states.append(child)

        return generated_states





