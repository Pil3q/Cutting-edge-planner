import matplotlib.pyplot as plt


def check_cut_placement(dimensions_of_the_material, dimensions_of_the_cuts):
    sorted_cuts = sorted(dimensions_of_the_cuts.items(), key=lambda x: x[1][0] * x[1][1], reverse=True)
    material_width, material_height = dimensions_of_the_material
    remaining_material = [[0, 0, material_width, material_height]]
    cut_placements = {}

    for cut_name, cut_dimensions in sorted_cuts:
        for i, (x, y, w, h) in enumerate(remaining_material):
            if cut_dimensions[0] <= w and cut_dimensions[1] <= h:
                cut_placements[cut_name] = [(x, y), (x + cut_dimensions[0], y), (x + cut_dimensions[0], y + cut_dimensions[1]), (x, y + cut_dimensions[1])]
                if cut_dimensions[0] == w and cut_dimensions[1] == h:
                    del remaining_material[i]
                else:
                    if cut_dimensions[0] == w:
                        remaining_material[i] = [x, y + cut_dimensions[1], w, h - cut_dimensions[1]]
                    elif cut_dimensions[1] == h:
                        remaining_material[i] = [x + cut_dimensions[0], y, w - cut_dimensions[0], h]
                    else:
                        remaining_material[i] = [x + cut_dimensions[0], y, w - cut_dimensions[0], cut_dimensions[1]]
                        remaining_material.append([x, y + cut_dimensions[1], w, h - cut_dimensions[1]])
                break
        else:
            return "Material too small"

    output = "Optimal Placement:\n"
    for cut_name, coordinates in cut_placements.items():
        output += f"{cut_name}:\n"
        for coordinate in coordinates:
            output += f"        {coordinate}\n"

    # Visualize the cut placements
    fig, ax = plt.subplots()
    ax.set_xlim(0, material_width)
    ax.set_ylim(0, material_height)
    ax.set_aspect('equal')

    for cut_name, coordinates in cut_placements.items():
        xs = [coord[0] for coord in coordinates]
        ys = [coord[1] for coord in coordinates]
        ax.fill(xs, ys, alpha=0.5, label=cut_name)
        ax.text(xs[0] + 5, ys[0] + 5, cut_name)

    plt.legend()
    plt.show()

    return output


# Example usage
dimensions_of_the_material = [105, 68]
dimensions_of_the_cuts = {
    "A": [52.5, 41],
    "B": [41, 17],
    "C": [53, 7],
    "D": [52.5, 41],
    "E": [41, 17]
}

result = check_cut_placement(dimensions_of_the_material, dimensions_of_the_cuts)
print(result)
