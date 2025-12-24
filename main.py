from Puzzle import Puzzle

def main():
    dimension = [3,3]   # 3x3 Puzzle

    combination = [8,7,5,
                   1,0,4,
                   2,6,3]

    solution_combination = [1,2,3,
                            4,5,6,
                            0,7,8]

    Puzzle(dimension, combination, solution_combination)

if __name__ == "__main__":
    main()