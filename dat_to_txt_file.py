def add_zcoords(input_file, output_file, z):
    """Function that takes the .dat file and adds a defined z coodinate to it"""

    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    with open(output_file, 'w') as f:
        for line in lines:
            x, y = map(float, line.split())
            f.write(f'{x} {y} {z}')

add_zcoords()