
def read_text(path, AVAILABLE_COLORS, COLORTABLE):
    with open(path) as input_file:
        for line in input_file:
            r_available, g_available, b_available, colorname, colornr = (item.strip() for item in line.split(';', 4))
            color= int(b_available),int(g_available), int(r_available)
            colortable = colornr, colorname, color
            COLORTABLE.append(colortable)
            #print (r_available, g_available, b_available)
            AVAILABLE_COLORS.append(color)


