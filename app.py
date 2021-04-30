import re, sys
from rover import Rover

def main(files_names):
    if len(files_names) < 1:
        Exception("No file names where given as input")
    output_lines = []
    direction_to_degrees = {"E": 0, "N": 90, "W": 180, "S": 270}
    degrees_to_direction = {0: "E", 90: "N", 180: "W", 270: "S"}

    for files_name in files_names:
        f = open(files_name, "r")
        input = f.read()
        lines = input.split("\n")
        top_corner_coords = lines[0].split(":")[1]
        rovers_names = list(set([re.findall(r'Rover\d', x)[0] for x in lines[1:]]))
        for rover in rovers_names:
            instructions = [line for line in lines if rover in line]
            instructions_tape =  "".join([inst.split(":")[1] for inst in instructions if "Instructions" in inst])
            landing_string = [inst for inst in instructions if "Landing" in inst][0]
            landing_coord =  landing_string.split(":")[1][0:-2]
            landing_direction = landing_string[-1]
            r = Rover(rover, int(landing_coord[0]), int(landing_coord[2]), direction_to_degrees[landing_direction], int(top_corner_coords[0]), int(top_corner_coords[2]))
            r.read_and_follow_instruction_tape(instructions_tape)
            output_lines.append(str(r))

    [print(output_line) for output_line in output_lines]

if __name__ == '__main__':
    files_names = sys.argv[1:]
    main(files_names)
    