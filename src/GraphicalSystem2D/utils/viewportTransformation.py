from structures.Window import Window

import consts


# transforms the positions in the window to a Viewport usable
def viewportTransformation(x, y, window: Window):
    return _transformPoint(x, y, window)

def _transformPoint(x, y, window: Window) -> list:
    """ Given the points world coordinates, returns them transformed to viewport
    """
    x_vp = (
        (x - window.xw_min) / (window.xw_max - window.xw_min)
    ) * consts.VIEWPORT_WIDTH
    y_vp = (
        1 - ((y - window.yw_min) / (window.yw_max - window.yw_min))
    ) * consts.VIEWPORT_HEIGHT
    
    return x_vp, y_vp


def transformToWorldCoordinates(x: float, y: float, window: Window):
    """When structures are created using mouse, the coordinates are already relative to the viewport
    returns the (x, y) coordinates converted to world coordinates
    """
    xw = ((x * (window.xw_max - window.xw_min)) / consts.VIEWPORT_WIDTH) + window.xw_min
    yw = (
        -(y / consts.VIEWPORT_HEIGHT - 1) * (window.yw_max - window.yw_min)
        + window.yw_min
    )

    return xw, yw
