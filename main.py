from Puzzle import Puzzle

def main():
    dimension = [3,3]   # 3x3 Puzzle

    combination = [3,7,2,5,4,0,6,8,1]
    solution_combination = [1,2,3,4,5,6,7,8,0]

    Puzzle(dimension, combination, solution_combination)

if __name__ == "__main__":
    main()