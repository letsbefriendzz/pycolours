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

![HSV->RGB Function](https://user-images.githubusercontent.com/89048358/154717357-9776405d-56e2-4c9a-b4a2-ba97fa2531ac.png)

Where `k` is

![HSV->RGB K Definition](https://user-images.githubusercontent.com/89048358/154717524-256f803e-2e31-43c8-a098-b9ba0e262040.png)
