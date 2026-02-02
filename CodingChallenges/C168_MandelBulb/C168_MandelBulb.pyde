import py5_tools

py5_tools.processing.download_library("PeasyCam")

from peasy import PeasyCam

DIM = 128
n = 8
max_iter = 20
bulb = []

def setup():
    size(600, 600, P3D)
    PeasyCam(get_current_sketch(), 600)

    start = millis()
    for i in range(DIM):
        for j in range(DIM):
            edge = False
            for k in range(DIM):
                x = map(i, 0, DIM-1, -1, 1)
                y = map(j, 0, DIM-1, -1, 1)
                z = map(k, 0, DIM-1, -1, 1)
                v = (x, y, z)

                if calc_iterations(v):
                    if not edge:
                        edge = True
                        bulb.append(v)
                else:
                    edge = False

    print(millis() - start)


def draw():
    background(0)
    stroke(255)
    strokeWeight(1)

    for p in bulb:
        x, y, z = p
        point(x * 200, y * 200, z * 200)


def calc_iterations(v):
    x, y, z = v
    zeta = (0, 0, 0)
    for _ in range(max_iter):
        r, theta, phi = cart_to_polar(zeta)
        if r > 2:
            break

        nx = pow(r, n) * sin(theta * n) * cos(phi * n)
        ny = pow(r, n) * sin(theta * n) * sin(phi * n)
        nz = pow(r, n) * cos(theta * n)
        zeta = (nx + x, ny + y, nz + z)
    else:
        return True

    return False


def cart_to_polar(vec):
    x, y, z = vec
    x2 = x * x
    y2 = y * y
    r = sqrt(x2 + y2 + z * z)
    theta = atan2(sqrt(x2 + y2), z)
    phi = atan2(y, x)

    return (r, theta, phi)
