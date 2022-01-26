# FILE      : rgb.py
# AUTHOR    : friendzz
# DESC      :
    # this file defines various functions I've written for manipulating rgb values in python.
    # this includes inverting rgb values, converting rgb values to hsv values, and so forth.
"""
            _           __     _                     __               _     
           | |          \ \   | |                    \ \             | |    
  _ __ __ _| |__    _____\ \  | |__  _____   __  _____\ \   _ __ __ _| |__  
 | '__/ _` | '_ \  |______> > | '_ \/ __\ \ / / |______> > | '__/ _` | '_ \ 
 | | | (_| | |_) |       / /  | | | \__ \\ V /        / /  | | | (_| | |_) |
 |_|  \__, |_.__/       /_/   |_| |_|___/ \_/        /_/   |_|  \__, |_.__/ 
       __/ |                                                     __/ |      
      |___/                                                     |___/       
"""

# RGB is defined by three integer values from 0-255. These values represent the share of red, green, and blue hues respectively.
# varying combinations of these RGB values result in a wide array of colours we see as the colourwheel.

# HSV is a different method of defining colour mathematically and digitially. Rather than representing red, green, and blue, hsv
# values represent a hue, saturation, and value. These three integers can be described as a cylinder, where the hue is an angle
# that points from the center of the cylinder (white) outwards, the saturation defining how far from the center we travel width
# wise, and the value defining the location vertically within the cylinder.

# f(n) = V - V*S*max(0, min( k, 4-k, 1 ) )
# k = (n + (h'/60))mod6
# given the above functions, f(5) = R', f(3) = G', f(1) = B'
# therefore RGB = f(5) * 255, f(3) * 255, f(1) * 255
def hsv_func(hsv, n):
    return hsv[2] - ( hsv[2] * hsv[1] ) * max( 0, min(calc_k(hsv[0], n), 4 - calc_k(hsv[0], n), 1) )

# k = (n + (h'/60))mod6
def calc_k(h, n):
    return ( n + ( h / 60 ) ) % 6

# returns an array of integers, being f(n) * 255, where n = 5, 3, 1.
# https://en.wikipedia.org/wiki/HSL_and_HSV#HSV_to_RGB
def hsv_to_rgb(hsv):
    return [  (hsv_func(hsv, 5) * 255), (hsv_func(hsv, 3) * 255), (hsv_func(hsv, 1) * 255) ]

# takes an array of three integers from 0-255, RGB format, and converts it to an HSV format.
# https://en.wikipedia.org/wiki/HSL_and_HSV#From_RGB
# not exactly as described in the wikipedia article, but mostly the same.
def rgb_to_hsv(r,g,b):
    return rgb_to_hsv( [ r,g,b ] )

def rgb_to_hsv(rgb):
    # rgb values are converted from 0-255 range to 0-1 range
    # R'G'B' = RGB / 255
    # rgb_frac = R'G'B'
    rgb_frac = [ rgb[0] / 255, rgb[1] / 255, rgb[2] / 255 ]

    # each subsequent helper function expects R'G'B', not RGB.
    h = generate_hue( rgb_frac )
    s = generate_sat(max( rgb_frac), max( rgb_frac ) - min( rgb_frac ))
    # v = generate_val( rgb_frac ) -- line 64 converted to line 65 because redundancy
    v = max( rgb_frac )

    return [h,s,v]

# V = the largest member of the rgb instance passed, divided by 255
# this function assumes that we're receiving R'G'B' <- (rgb / 255).
# avoid using because redundancy lol
def generate_val(rgb):
    return max(rgb)

# generates the saturation value - if cmax == 0, return 0. otherwise, S=delta/Cmax
# cmax = the largest integer of the rgb values sent, divided by 100.
# cmin = the smallest integer of the rgb values sent, divided by 100.
# delta = cmax - cmins

# todo-make this shit a lambda expression or smth
def generate_sat(cmax, dlt):
    if cmax == 0:
        return cmax
    else:
        return dlt / cmax

# the hue has a convoluted calculation process that I donut uunderstand super well.
# we must defined cmax and cmin as the rgb values / 100 (<- this op performed in the
# parent function) and define the delta as the difference between cmax and cmin.
# varying on which member of the r,g,b values passed is the largest, we call a fucntion.
# these fucntions involve substracting some integers, dividng by the delta, and then
# multiplying by 60 to get an angle value. wild stuff.
def generate_hue(rgb):
    #r = rgb[0]
    #g = rgb[1]
    #b = rgb[2]

    mx = max( rgb )
    mn = min( rgb )
    dlt = mx - mn

    #lol idk what to do in this case
    if dlt == 0:
        dlt = 1

    if mx == rgb[0]:
        return max_r(rgb[0],rgb[1],rgb[2],dlt)
    elif mx == rgb[1]:
        return max_g(rgb[0],rgb[1],rgb[2],dlt)
    elif mx == rgb[2]:
        return max_b(rgb[0],rgb[1],rgb[2],dlt)
    else:
        return -1

# The following three functions are submethods of the generate_hue function.
# there are different equations to implement based on the resultant largest value from the rgb set passed.
def max_r(r,g,b,dlt):
    return 60 * ( ( ( g - b ) / dlt ) % 6 )

def max_g(r,g,b,dlt):
    return  60 * ( ( ( b - r ) / dlt ) + 2 )

def max_b(r,g,b,dlt):
    return 60 * ( ( ( r - g ) / dlt ) + 4 )

"""
            _                             _             _       _                 
           | |                           (_)           | |     | |                
  _ __ __ _| |__    _ __ ___   __ _ _ __  _ _ __  _   _| | __ _| |_ ___  _ __ ___ 
 | '__/ _` | '_ \  | '_ ` _ \ / _` | '_ \| | '_ \| | | | |/ _` | __/ _ \| '__/ __|
 | | | (_| | |_) | | | | | | | (_| | | | | | |_) | |_| | | (_| | || (_) | |  \__ \
 |_|  \__, |_.__/  |_| |_| |_|\__,_|_| |_|_| .__/ \__,_|_|\__,_|\__\___/|_|  |___/
       __/ |                               | |                                    
      |___/                                |_|                                    
"""

def avg_val(a, b):
    return ( int(a) + int(b) ) / 2

def inverse_rgb(rgb):
    return [ int(255 - rgb[0]), int(255 - rgb[1]), int(255 - rgb[2]) ]

def avg_rgb(rgb1, rgb2):
    return [ avg_val( rgb1[0] , rgb2[0] ), avg_val( rgb1[1] , rgb2[1] ), avg_val( rgb1[2] , rgb2[2] ) ]

"""
  _                                       _             _       _                 
 | |                                     (_)           | |     | |                
 | |__  _____   __  _ __ ___   __ _ _ __  _ _ __  _   _| | __ _| |_ ___  _ __ ___ 
 | '_ \/ __\ \ / / | '_ ` _ \ / _` | '_ \| | '_ \| | | | |/ _` | __/ _ \| '__/ __|
 | | | \__ \\ V /  | | | | | | (_| | | | | | |_) | |_| | | (_| | || (_) | |  \__ \
 |_| |_|___/ \_/   |_| |_| |_|\__,_|_| |_|_| .__/ \__,_|_|\__,_|\__\___/|_|  |___/
                                           | |                                    
                                           |_|                                                                                                       
"""

# accepts an [h,s,v] array and an integer to shift the h value by, returns [h,s,v]
def hue_shift(hsv, deg):
    if deg < 0 or deg > 360:
                    raise BaseException("Bad hue val")
    if hsv[0] + deg > 360:
        deg = deg - (360 - hsv[0])
        hsv[0] = 0
    hsv[0] = hsv[0] + deg
    return hsv

# accepts hsv, sat, and mode --
# 0 means assign, 1 means add
def sat_shift(hsv, sat, mode = 0):
    if sat < 0 or sat > 1:
        raise BaseException("Bad sat val")
    
    if mode == 0:
        hsv[1] = sat
    else:
        hsv[1] = hsv[1] + sat
    return hsv