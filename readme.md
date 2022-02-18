# pycolours

-- this readme isn't finished! i'll be back to finish it soon!

I take particular interest in digital media, from audio processing to photo and video.

In this program, I sought to implement various mathematical conversion algorithms for RGB & HSV colour formats.

##  RGB & HSV

![rgb-cube](https://miro.medium.com/max/1400/1*W30TLUP9avQwyyLfwu7WYA.jpeg)

### RGB

Digital colour is represented using only the three primary colours; **red**, **green**, and **blue**.

A single pixel, being nothing but a combination of these three values, can be represented as a cube with the RGB coordinates varying from 0-255.

### HSV

HSV is an alternative method of representing digital colour. instead of coordinates within our hypothetical RGB cube, the HSV method defines coordinates within a cylinder. **Hue** defines the angle, as measured from within the centre of the cylinder, that the **saturation** and **value** coordinates occur. **Saturation**, a value from 0 - 1, defines the location between the centre of the cylinder and the edge of it, and the **value** represents the vertical coordinate.

## RGB -> HSV

My implementation of the following RGB -> HSV algorithm involves multiple functions, each to define a hue, saturation, and value. Each of these functions expects an array of values between 0 - 1; the arithmetic needs our RGB values of 0 - 255 to be converted to a decimal between 0 - 1. Thus we create a fractional representation of the RGB value passed as `rgb_frac`, and send this to our functions.

```python
def rgb_to_hsv(rgb):
    rgb_frac = [ rgb[0] / 255, rgb[1] / 255, rgb[2] / 255 ]
    # each subsequent helper function expects R'G'B', not RGB.
    h = generate_hue( rgb_frac )
    s = generate_sat(max( rgb_frac), max( rgb_frac ) - min( rgb_frac ))
    v = max( rgb_frac )
    return [h,s,v]
```

### Hue Generation

Hue generation is a quite involved process. There are various outcomes, depending on which value within the fractional RGB array passed to it is the largest. There are functions defined for each case.

<img src="https://www.rapidtables.com/convert/color/rgb-to-hsv/hue-calc2.gif" alt="RGB->HSV Hue" style=""/>

As can be observed above, depending on which RGB field is our largest value, we perform varying arithmetic on the other two RGB fields, along with out chroma/delta value.

```python
def generate_hue(rgb):
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
```

For the following sub-functions, we assume the following:

R, G and B are the Red, Green and Blue values from our RGB array respectively.

C, also represented as delta, dlt, or Δ, is the difference between the maximum and minumum values in our RGB array.

#### Max = R

If our maximum RGB value is R, we multiply 60 by (G - B) / C, taking the remainder of the aforementioned operation when it is divided by 6.

```python
def max_r(r,g,b,dlt):
    return 60 * ( ( ( g - b ) / dlt ) % 6 )
```

#### Max = G

If our maximum RGB value is G, we multiply 60 by (B - R) / C.

```python
def max_g(r,g,b,dlt):
    return  60 * ( ( ( b - r ) / dlt ) + 2 )
```

#### Max = B

```python
def max_b(r,g,b,dlt):
    return 60 * ( ( ( r - g ) / dlt ) + 4 )
```

### Saturation Generation

To create a saturation value, we create C (chroma) by dividing the maximum value by the minimum value, from those within our RGB array. If the Value (or maximum value from RGB) is zero, the saturation value we return is zero. Otherwise, we calculate saturation by dividing chroma (C) by the maximum value (V).

<img src="https://github.com/letsbefriendzz/pycolours/blob/master/_readme_source/rgb-hsv-scalc.PNG" alt="RGB->HSV Sat" style="height:20%; width:20%;"/>

```python
def generate_sat(cmax, dlt):
    if cmax == 0:
        return cmax
    else:
        return dlt / cmax
```

### Value Generation

The Value field is the easiest to populate. As established, we take the RGB values passed and divide them by 255, converting them from a range of 0 - 255 to 0 - 1. Then, from these decimal values, we take the largest among them, and this is the value.

<img src="https://github.com/letsbefriendzz/pycolours/blob/master/_readme_source/rgb-hsv-vcalc.PNG" alt="RGB->HSV Sat" style="height:20%; width:20%;"/>

Really, the below function isn't necessary; you could just perform this operation within the parent rgb_to_hsv function. For legibility's sake, however, I've kept it.

```python
def generate_val(rgb):
    return max(rgb)
```

## HSV -> RGB

Given an HSV value, using the following function, we can determine that

`(RGB) = f(5) x 255, f(3) x 255, f(1) x 255`

<img src="https://github.com/letsbefriendzz/pycolours/blob/master/_readme_source/hsv-rgb-fn.PNG" alt="HSV->RGB f(n)" style="height:20%; width:20%;"/>

This is very straight forward to implement. We create a function with two parameters; hsv, a three element array representing hue, saturation and value, and n, to sub into our function.

```python
def hsv_func(hsv, n):
    return hsv[2] - ( hsv[2] * hsv[1] ) * max( 0, min(calc_k(hsv[0], n), 4 - calc_k(hsv[0], n), 1) )
```

Where `k` is

<img src="https://github.com/letsbefriendzz/pycolours/blob/master/_readme_source/hsv-rgb-k.PNG" alt="HSV->RGB K" style="height:20%; width:20%;"/>

Even simpler to implement, `calc_k` takes a hue value and an n value, and performs the above arithmetic.

```python
def calc_k(h, n):
    return ( n + ( h / 60 ) ) % 6
```
