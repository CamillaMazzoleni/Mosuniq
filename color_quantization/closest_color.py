from math import sqrt

#rgb is a tuple of the color that we want to assign to an available color
#AVAILABLE_COLORS is the list of colors available
#color_used is the array of colors we are using in the image. the function put every
def closest_color(rgb, AVAILABLE_COLORS):
    b, g, r =rgb
    #print ("color received " + str(rgb))
    color_diffs = []
    for color in AVAILABLE_COLORS:
        cb, cg, cr = color
        color_diff = sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
        #if (abs(r-cr)<=70 and abs(g-cr)<=70 and abs(b-cb)<=70):
        color_diffs.append((color_diff, color))
    color_min = min(color_diffs)[1]
    #print("color calculated " + str(color_min))
    #color_used.append(color_min)
    return color_min
