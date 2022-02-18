# pycolours

I take particular interest in digital media, from audio processing to photo and video.

In this program, I sought to implement various mathematical conversion algorithms for RGB & HSV colour formats.

##  RGB

Digital colour is represented using only the three primary colours; **red**, **green**, and **blue**.

A single pixel, being nothing but a combination of these three values, can be represented as a cube with the RGB coordinates varying from 0-255.

## HSV

HSV is an alternative method of representing digital colour. instead of coordinates within our hypothetical RGB cube, the HSV method defines coordinates within a cylinder. **Hue** defines the angle, as measured from within the centre of the cylinder, that the **saturation** and **value** coordinates occur. **Saturation**, a value from 0 - 1, defines the location between the centre of the cylinder and the edge of it, and the **value** represents the vertical coordinate.

![rgb-cube](https://miro.medium.com/max/1400/1*W30TLUP9avQwyyLfwu7WYA.jpeg)

## RGB -> HSV

## HSV -> RGB

Given an HSV value, using the following function, we can determine that

`(RGB) = f(5) x 255, f(3) x 255, f(1) x 255`

<img src="https://github.com/letsbefriendzz/pycolours/blob/master/_readme_source/hsv-rgb-fn.PNG" alt="HSV->RGB f(n)" style="height:50%; width:50%;"/>

This is very straight forward to implement. We create a function with two parameters; hsv, a three element array representing hue, saturation and value, and n, to sub into our function.

```python
def hsv_func(hsv, n):
    return hsv[2] - ( hsv[2] * hsv[1] ) * max( 0, min(calc_k(hsv[0], n), 4 - calc_k(hsv[0], n), 1) )
```

Where `k` is

<img src="https://github.com/letsbefriendzz/pycolours/blob/master/_readme_source/hsv-rgb-k.PNG" alt="HSV->RGB K" style="height:50%; width:50%;"/>

Even simpler to implement, `calc_k` takes a hue value and an n value, and performs the above arithmetic.

```python
def calc_k(h, n):
    return ( n + ( h / 60 ) ) % 6
```
