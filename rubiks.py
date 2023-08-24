#!/usr/bin/env python3

import copy
import re


class RubiksCube:
    def __init__(self):
        self.rubecode = re.compile(pattern=r'([MESURFDLBurfdlb])([\d]?)(\'?)')

        self.reset()

    def grid(self, prefix, x, y):
        matrix = []

        for i in range(x):
            row = []

            for j in range(y):
                cell_value = f"{prefix}-{i}{j}"
                row.append(cell_value)

            matrix.append(row)

        return matrix

    def reset(self):
        # Initialize a solved Rubik's Cube
        self.faces = {
            'F': self.grid("G", 3, 3),
            'B': self.grid("B", 3, 3),
            'L': self.grid("O", 3, 3),
            'R': self.grid("R", 3, 3),
            'U': self.grid("W", 3, 3),
            'D': self.grid("Y", 3, 3)
        }

    def rotate(self, face, reverse):
        from_copy = copy.deepcopy(self.faces)

        match face.upper():
            case "U":
                if reverse:
                    self.faces["B"] = from_copy["U"]
                    self.faces["D"] = from_copy["B"]
                    self.faces["F"] = from_copy["D"]
                    self.faces["U"] = from_copy["F"]

                    self.faces["B"] = self.rotate_90_degrees(self.faces["B"] , turns=2)
                    self.faces["D"] = self.rotate_90_degrees(self.faces["D"] , turns=2)
                    self.faces["L"] = self.rotate_90_degrees(self.faces["L"] , turns=1, ccw=True)
                    self.faces["R"] = self.rotate_90_degrees(self.faces["R"] , turns=1, ccw=False)
                else:
                    self.faces["B"] = from_copy["D"]
                    self.faces["D"] = from_copy["F"]
                    self.faces["F"] = from_copy["U"]
                    self.faces["U"] = from_copy["B"]

                    self.faces["B"] = self.rotate_90_degrees(self.faces["B"] , turns=2)
                    self.faces["L"] = self.rotate_90_degrees(self.faces["L"] , turns=1, ccw=False)
                    self.faces["R"] = self.rotate_90_degrees(self.faces["R"] , turns=1, ccw=True)
                    self.faces["U"] = self.rotate_90_degrees(self.faces["U"] , turns=2)
            case "R":
                if reverse:
                    self.faces["B"] = from_copy["R"]
                    self.faces["F"] = from_copy["L"]
                    self.faces["L"] = from_copy["B"]
                    self.faces["R"] = from_copy["F"]

                    self.faces["D"] = self.rotate_90_degrees(self.faces["D"] , turns=1, ccw=False)
                    self.faces["U"] = self.rotate_90_degrees(self.faces["U"] , turns=1, ccw=True)
                else:
                    self.faces["B"] = from_copy["L"]
                    self.faces["F"] = from_copy["R"]
                    self.faces["L"] = from_copy["F"]
                    self.faces["R"] = from_copy["B"]

                    self.faces["D"] = self.rotate_90_degrees(self.faces["D"] , turns=1, ccw=True)
                    self.faces["U"] = self.rotate_90_degrees(self.faces["U"] , turns=1, ccw=False)
            case "F":
                # Default - no face rotation
                pass
            case "D":
                if reverse:
                    self.faces["F"] = from_copy["U"]
                    self.faces["U"] = from_copy["B"]
                    self.faces["B"] = from_copy["D"]
                    self.faces["D"] = from_copy["F"]

                    self.faces["B"] = self.rotate_90_degrees(self.faces["B"] , turns=2)
                    self.faces["U"] = self.rotate_90_degrees(self.faces["U"] , turns=2)
                    self.faces["L"] = self.rotate_90_degrees(self.faces["L"] , turns=1, ccw=False)
                    self.faces["R"] = self.rotate_90_degrees(self.faces["R"] , turns=1, ccw=True)
                else:
                    self.faces["F"] = from_copy["D"]
                    self.faces["D"] = from_copy["B"]
                    self.faces["B"] = from_copy["U"]
                    self.faces["U"] = from_copy["F"]

                    self.faces["B"] = self.rotate_90_degrees(self.faces["B"] , turns=2)
                    self.faces["D"] = self.rotate_90_degrees(self.faces["D"] , turns=2)
                    self.faces["L"] = self.rotate_90_degrees(self.faces["L"] , turns=1, ccw=True)
                    self.faces["R"] = self.rotate_90_degrees(self.faces["R"] , turns=1, ccw=False)
            case "L":
                if reverse:
                    self.faces["F"] = from_copy["R"]
                    self.faces["R"] = from_copy["B"]
                    self.faces["B"] = from_copy["L"]
                    self.faces["L"] = from_copy["F"]

                    self.faces["U"] = self.rotate_90_degrees(self.faces["U"] , turns=1, ccw=False)
                    self.faces["D"] = self.rotate_90_degrees(self.faces["D"] , turns=1, ccw=True)
                else:
                    self.faces["F"] = from_copy["L"]
                    self.faces["L"] = from_copy["B"]
                    self.faces["B"] = from_copy["R"]
                    self.faces["R"] = from_copy["F"]

                    self.faces["U"] = self.rotate_90_degrees(self.faces["U"] , turns=1, ccw=True)
                    self.faces["D"] = self.rotate_90_degrees(self.faces["D"] , turns=1, ccw=False)
            case "B":
                    self.faces["F"] = from_copy["B"]
                    self.faces["B"] = from_copy["F"]
                    self.faces["L"] = from_copy["R"]
                    self.faces["R"] = from_copy["L"]

                    self.faces["U"] = self.rotate_90_degrees(self.faces["U"] , turns=2)
                    self.faces["D"] = self.rotate_90_degrees(self.faces["D"] , turns=2)

    def display(self, debug):
        for face, rows in self.faces.items():
            for row in rows:
                if debug:
                    print(f"{face}: {' '.join(row)}")
                else:
                    print(f"{face}: {' '.join(elem.split('-')[0] for elem in row)}")

            print()

    def rotate_90_degrees(self, matrix, turns=None, ccw=None):
        if ccw is None:
            ccw = False

        if turns is None:
            turns = 1

        rotated_matrix = [[0] * 3 for _ in range(3)]

        for _ in range(turns):
            for i in range(3):
                for j in range(3):
                    if ccw:
                        rotated_matrix[i][j] = matrix[j][2 - i]
                    else:
                        rotated_matrix[i][j] = matrix[2 - j][i]

            matrix = copy.deepcopy(rotated_matrix)

        return rotated_matrix

    def turn(self, face, direction, depth):
        from_copy = copy.deepcopy(self.faces)

        if depth > 1:
            double_turn = True
        else:
            double_turn = False

        match direction:
            case "cw":
                match face:
                    case "M":
                        for num in range(3):
                            self.faces["F"][num][1] = from_copy["U"][num][1]
                            self.faces["U"][num][1] = from_copy["B"][num][1]
                            self.faces["B"][num][1] = from_copy["D"][num][1]
                            self.faces["D"][num][1] = from_copy["F"][num][1]

                    case "E":
                        for num in range(3):
                            self.faces["F"][1][num] = from_copy["R"][1][num]
                            self.faces["R"][1][num] = from_copy["B"][1][num]
                            self.faces["L"][1][num] = from_copy["F"][1][num]
                            self.faces["B"][1][num] = from_copy["L"][1][num]

                    case "S":
                        for num in range(3):
                            self.faces["U"][1][num] = from_copy["R"][num][1]
                            self.faces["R"][num][1] = from_copy["D"][1][num]
                            self.faces["D"][1][num] = from_copy["L"][num][1]
                            self.faces["L"][num][1] = from_copy["U"][1][num]

                    case _:
                        # Front-face turn, so handle the edges here
                        to_faces = ["U", "R", "D", "L"]

                        for to_face in to_faces:
                            match to_face:
                                case "U":
                                    for num in range(3):
                                        self.faces[to_face][2][num] = from_copy["L"][2 - num][2]

                                        if double_turn:
                                            self.faces[to_face][1][num] = from_copy["L"][2 - num][1]

                                case "R":
                                    for num in range(3):
                                        self.faces[to_face][num][0] = from_copy["U"][2][num]

                                        if double_turn:
                                            self.faces[to_face][num][1] = from_copy["U"][1][num]

                                case "D":
                                    for num in range(3):
                                        self.faces[to_face][0][num] = from_copy["R"][2 - num][0]

                                        if double_turn:
                                            self.faces[to_face][1][num] = from_copy["R"][2 - num][1]

                                case "L":
                                    for num in range(3):
                                        self.faces[to_face][num][2] = from_copy["D"][0][num]

                                        if double_turn:
                                            self.faces[to_face][num][1] = from_copy["D"][1][num]

                        self.faces["F"] = self.rotate_90_degrees(self.faces["F"] , turns=1, ccw=False)

            case "ccw":
                match face:
                    case "M":
                        for num in range(3):
                            self.faces["F"][num][1] = from_copy["U"][num][1]
                            self.faces["U"][num][1] = from_copy["B"][num][1]
                            self.faces["B"][num][1] = from_copy["D"][num][1]
                            self.faces["D"][num][1] = from_copy["F"][num][1]

                    case "E":
                        for num in range(3):
                            self.faces["F"][1][num] = from_copy["L"][1][num]
                            self.faces["L"][1][num] = from_copy["B"][1][num]
                            self.faces["R"][1][num] = from_copy["F"][1][num]
                            self.faces["B"][1][num] = from_copy["R"][1][num]

                    case "S":
                        for num in range(3):
                            self.faces["U"][1][num] = from_copy["L"][num][1]
                            self.faces["R"][num][1] = from_copy["U"][1][num]
                            self.faces["D"][1][num] = from_copy["R"][num][1]
                            self.faces["L"][num][1] = from_copy["D"][1][num]

                    case _:
                        # Front-face turn, so handle the edges here
                        to_faces = ["U", "R", "D", "L"]

                        for to_face in to_faces:
                            match to_face:
                                case "U":
                                    for num in range(3):
                                        self.faces[to_face][2][num] = from_copy["R"][num][0]

                                    if double_turn:
                                        self.faces[to_face][1][num] = from_copy["R"][num][1]

                                case "R":
                                    for num in range(3):
                                        self.faces[to_face][num][0] = from_copy["D"][0][2 - num]

                                    if double_turn:
                                        self.faces[to_face][num][1] = from_copy["D"][1][2 - num]

                                case "D":
                                    for num in range(3):
                                        self.faces[to_face][0][num] = from_copy["L"][num][2]

                                    if double_turn:
                                        self.faces[to_face][1][num] = from_copy["L"][num][1]

                                case "L":
                                    for num in range(3):
                                        self.faces[to_face][num][2] = from_copy["U"][2][2 - num]

                                    if double_turn:
                                        self.faces[to_face][num][1] = from_copy["U"][1][2 - num]


                        self.faces["F"] = self.rotate_90_degrees(self.faces["F"] , turns=1, ccw=True)

    def move(self, moves):
        # Perform a move on the Rubik's Cube
        for move in moves.split(" "):
            try:
                face, turns, direction = self.rubecode.match(move).groups()
            except AttributeError:
                print(f"Error: Please use the standard Cube Move Notation format. Skipping: '{move}'")
            else:
                if turns:
                    turns = int(turns)
                else:
                    turns = 1

                if direction:
                    direction = "ccw"
                else:
                    direction = "cw"

                if face.islower():
                    double_turn = 2
                else:
                    double_turn = 1

                # Make it so the face I'm working on is in front of me
                self.rotate(face=face, reverse=False)

                for _ in range(turns):
                    self.turn(face, direction, double_turn)

                # Now, switch it back to how it was
                self.rotate(face=face, reverse=True)


if __name__ == "__main__":
    # Samples to check:
    # https://ruwix.com/puzzle-scramble-generator/?type=rubiks-cube

    rubiks_cube = RubiksCube()

    while True:
        move = input("Move: ")
        rubiks_cube.reset()

        rubiks_cube.move(move)

        print(f"\nAfter move: \"{move}\"")
        rubiks_cube.display(debug=False)
