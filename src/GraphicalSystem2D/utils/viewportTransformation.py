from structures.Window import Window

import consts


# transforms the positions in the window to a Viewport usable
def viewportTransformation(x, y, window: Window):
    return _transformPoint(x, y, window)


def _transformPoint(x, y, window: Window) -> list:
    """Given the points world coordinates, returns them transformed to viewport"""
    scalling_x = (consts.VIEWPORT_X_MAX - consts.VIEWPORT_X_MIN) / (
        window.xw_max - window.xw_min
    )
    xv = consts.VIEWPORT_X_MIN + (x - window.xw_min) * scalling_x

    scalling_y = (consts.VIEWPORT_Y_MAX - consts.VIEWPORT_Y_MIN) / (
        window.yw_max - window.yw_min
    )
    yv = consts.VIEWPORT_Y_MIN + (y - window.yw_min) * scalling_y

    return round(xv), round(yv)


def transformToWorldCoordinates(x: float, y: float, window: Window):
    """When structures are created using mouse, the coordinates are already relative to the viewport
    returns the (x, y) coordinates converted to world coordinates
    """
    xw = window.xw_min + (
        ((x - consts.VIEWPORT_X_MIN) * (window.xw_max - window.xw_min))
        / (consts.VIEWPORT_X_MAX - consts.VIEWPORT_X_MIN)
    )
    yw = window.yw_min + (
        ((y - consts.VIEWPORT_Y_MIN) * (window.yw_max - window.yw_min))
        / (consts.VIEWPORT_Y_MAX - consts.VIEWPORT_Y_MIN)
    )

    return xw, yw
