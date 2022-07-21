#returns colornames
def color_name (rgb, colortable):
    b, g, r= rgb
    for colors in colortable:
        colornr, colorname, color = colors
        b_available, g_available, r_available= color
        if r==r_available and g==g_available and b==b_available:
            return colorname

#returns colornr
def color_nr(rgb,colortable):
    b, g, r = rgb
    for colors in colortable:
        colornr, colorname, color = colors
        b_available, g_available, r_available = color
        if r == r_available and g == g_available and b == b_available:
            return colornr

def assign_color_nr(rgb, colortable,i):
    b, g, r = rgb
    j=0
    for colors in colortable:
        colornr, colorname, color = colors
        b_available, g_available, r_available = color
        if r == r_available and g == g_available and b == b_available:
            return j
        j+=1
            #print ("ok"+str(i))