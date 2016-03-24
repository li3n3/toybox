def point_in_rectangle(point, rectangle):
"""point given as [px, py]
   rectangle lower-left and upper-right given as [[llx, lly], [urx, ury]]
"""
    # get the point's coordinates into better variables
    px = point[0]
    py = point[1]

    # do the same for the rectangle
    llx = rectangle[0][0]
    lly = rectangle[0][1]
    urx = rectangle[1][0]
    ury = rectangle[1][1]

    if (px >= llx and px <= urx) and (py >= lly and py <= ury):
        return True
    else:
        return False
