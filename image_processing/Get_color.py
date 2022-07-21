#######GETCOLOR
# compare rgb values and return color name
def getcolor(r,g,b): 
    if (r >= 80 and r <= 230 ) and (g >= 20 and g <= 175) and (b > 15 and b < 130):
        return 'b'
    elif (r >= 148 and r <= 250 ) and (g >= 140 and g < 250) and (b >= 140 and b < 250):
        return 'w'
    elif (r >= 0 and r <= 100 ) and (g > 130 and g < 255) and (b > 150 and b < 255):
        return 'y'
    elif (r > 0 and r <= 75 ) and (g >= 79 and g <= 130) and (b > 125 and b < 255):
        return 'o'
    elif (r >= 10 and r <= 70 ) and (g >= 20 and g < 79) and (b >= 90 and b < 255):
        return 'r'
    elif (r >= 20 and r <= 116 ) and (g > 60 and g <= 235) and (b > 20  and b <= 170):
        return 'g'
    elif (r >= 0 and r <= 30 ) and (g > 0 and g <= 30) and (b > 0  and b <= 30):
        return 'd'
    else:
        return

####GET AUTUMN COLOR
#we assume r=0, b=255
#g is current g value
#min is the min g value of the image
#max is the max g value of the image
#n number of shades we want to use
def autumn_color(g, gmin, gmax, n):
    step= (gmax-gmin)/n
    for i in range(n-1):
        if (g>=gmin+i*step and g<gmin+(i+1)*step):
            return (0, (gmin+i*step+gmin+(i+1)*step)/2, 255)
