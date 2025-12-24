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


    def __lt__(self, other):
        return False


    def legal_move(self, displacement) -> bool:
        """
        Determine if a move can be done or not.
        :param displacement: Displacement of the blank peace or 0
        :return: True if the displacement falls between position 0 and the combination's lenth
        """
        zero_index = self.combination.index(0)

        if not (0 <= zero_index + displacement < len(self.combination)):
            return False
        if displacement == -1 and zero_index % 3 == 0:
            return False
        if displacement == 1 and zero_index % 3 == 2:
            return False
        return True


    def is_goal(self):
        return self.combination == self.solution


    def transition(self, displacement):
        # If not a legal movement, we return
        if not self.legal_move(displacement):
            return None

        # Get the empty piece position and the piece's number that will be moved
        empty_space_pos = self.combination.index(0)
        target_pos = empty_space_pos + displacement
        moving_number = self.combination[target_pos]

        # Logical move of the peace
        new_combination = list(self.combination)
        new_combination[empty_space_pos] = moving_number
        new_combination[target_pos] = 0

        # Create the new state
        new_state = State(self.dimension, tuple(new_combination), self.solution)

        # Copy the movement's list to the new state
        new_state.moves = list(self.moves)
        new_state.moves.append(self.movements[displacement])

        return new_state


    def generate_children(self):
        generated_states = []

        for movement in self.displacements:
            child = self.transition(movement)

            if child is not None:
                generated_states.append(child)

        return generated_states


    def manhattan_distance(self):
        distance = 0
        for i in range(len(self.combination)):
            value = self.combination[i]
            if value != 0:
                current_row, current_col = divmod(i, 3)
                target_index = self.solution.index(value)
                target_row, target_col = divmod(target_index, 3)

                distance += abs(current_row - target_row) + abs(current_col - target_col)
        return distance

