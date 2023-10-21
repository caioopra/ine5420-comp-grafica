from structures.Line import Line
from structures.Point import Point

def liang_barsky(line: Line, window_max: Point = Point(1, 1), window_min: Point = Point(-1, -1),) -> Line | None:

    point1, point2 = line.getPoints()

    xw_min, yw_min = window_min.getCoordinates()
    xw_max, yw_max = window_max.getCoordinates()

    delta_x = point2.getNormalX() - point1.getNormalX()
    delta_y = point2.getNormalY() - point1.getNormalY()

    p = [- delta_x, delta_x, - delta_y, delta_y]
    q = [point1.getNormalX() - xw_min, xw_max - point1.getNormalX(), point1.getNormalY() - yw_min, yw_max - point1.getNormalY()]

    for i in range(4):
        if p[i] == 0 and q[i] < 0:
            return None

    pq = list(zip(p, q))
    negativos = [(q / p) for (p, q) in pq if p < 0]
    zeta_1 = max(0, max(negativos, default=0))
    positivos = [(q / p) for (p, q) in pq if p > 0]
    zeta_2 = min(1, min(positivos, default=1))

    # se zeta 1 > zeta 2, a linha ta completamente fora
    if zeta_1 > zeta_2:
        return None

    new_x1 = point1.getNormalX() + zeta_1 * delta_x
    new_y1 = point1.getNormalY() + zeta_1 * delta_y

    new_x2 = point1.getNormalX() + zeta_2 * delta_x
    new_y2 = point1.getNormalY() + zeta_2 * delta_y

    point1.setNormalCoordinates(new_x1, new_y1)
    point2.setNormalCoordinates(new_x2, new_y2)
    return line