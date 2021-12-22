from collections import Counter


def part1(areas):
    return len(get_cubes_on(areas))


def part2(areas):
    return get_cubes_optimized(areas)


def get_cubes_on(areas):
    cubes_on = set()
    for status, x, y, z in areas:
        if is_inside(*x) and is_inside(*y) and is_inside(*z):
            for i in range(x[0], x[1] + 1):
                for j in range(y[0], y[1] + 1):
                    for k in range(z[0], z[1] + 1):
                        if status == 'on':
                            cubes_on.add((i, j, k))
                        else:
                            if (i, j, k) in cubes_on:
                                cubes_on.remove((i, j, k))
    return cubes_on


def get_cubes_optimized(areas):
    preprocessed = [(1 if status == 'on' else -1, (min(x[0], x[1]), min(y[0], y[1]), min(z[0], z[1])),
                     (max(x[0], x[1]), max(y[0], y[1]), max(z[0], z[1]))) for status, x, y, z in areas]

    cubes = Counter()
    for status, (x_1, y_1, z_1), (x_2, y_2, z_2) in preprocessed:
        new_cubes = Counter()
        for (new_x_1, new_x_2, new_y_1, new_y_2, new_z_1, new_z_2), n_status in cubes.items():
            dx_1, dx_2 = max(x_1, new_x_1), min(x_2, new_x_2)
            dy_1, dy_2 = max(y_1, new_y_1), min(y_2, new_y_2)
            dz_1, dz_2 = max(z_1, new_z_1), min(z_2, new_z_2)
            if dx_1 <= dx_2 and dy_1 <= dy_2 and dz_1 <= dz_2:
                new_cubes[(dx_1, dx_2, dy_1, dy_2, dz_1, dz_2)] -= n_status
        if status > 0:
            new_cubes[(x_1, x_2, y_1, y_2, z_1, z_2)] = status
        cubes.update(new_cubes)
    count = 0
    for cube, status in cubes.items():
        count += (area(*cube) * status)
    return count


def is_inside(x1, x2):
    return -50 <= x1 <= 50 and -50 <= x2 <= 50


def area(x_1, x_2, y_1, y_2, z_1, z_2):
    return (x_2 - x_1 + 1) * (y_2 - y_1 + 1) * (z_2 - z_1 + 1)
