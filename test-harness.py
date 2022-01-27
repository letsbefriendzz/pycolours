from ctypes.wintypes import WORD
from re import X
import cv2, imutils
from rgb import *

#this whole function assumes constant size between frames
#it actually forces it
#get ready to get your aspect ratios ruined lmao
WIDTH = 1024
HEIGHT = 768

# x / y
# 0 x 0 @ top left corner
PIXEL_COORDS = [0, 150]

def hue_shift_frame(frame, deg=30):
    pixel_diff = 2
    x_index = 0
    while(x_index < HEIGHT):
        y_index = 0
        while(y_index < WIDTH):
            frame[x_index][y_index] = hsv_to_rgb( hue_shift( rgb_to_hsv( frame[x_index][y_index] ), deg ) )
            y_index += pixel_diff
        x_index += pixel_diff
        cv2.imshow('hue_shift_frame', frame)
        key = cv2.waitKey(250)

def avg_frames(frame1, frame2):
    
    cv2.imshow('frame1', frame1)
    key = cv2.waitKey(250)
    cv2.imshow('frame2', frame2)
    key = cv2.waitKey(250)

    x_index = 0
    while(x_index < HEIGHT):
        y_index = 0
        while(y_index < WIDTH):
            frame1[x_index][y_index] = avg_rgb(frame1[x_index][y_index], frame2[x_index][y_index])
            y_index += 1
        x_index += 1

    cv2.imshow('video', frame1)
    key = cv2.waitKey(12) & 0xFF

def avg_frame_testharness():
    vid1 = cv2.VideoCapture("F:\_PIRACY\TV\Corner Gas\s1\Corner.Gas.s01e01.Ruby.Reborn.avi") #replace name with 0 for webcam????
    vid2 = cv2.VideoCapture("F:\_PIRACY\TV\Corner Gas\s1\Corner.Gas.s01e06.World's.Biggest.Thing.avi")

    while(vid1.isOpened() and vid2.isOpened()):
        #read a frame from the videos
        _,frame1 = vid1.read()
        _,frame2 = vid2.read()
        
        #resize the frames to a happy size
        frame1 = imutils.resize(frame1, width=WIDTH, height=HEIGHT)
        frame2 = imutils.resize(frame2, width=WIDTH, height=HEIGHT)

        if frame1[0][0][0] > 75:
            avg_frames(frame1, frame2)

def hue_shift_testharness():
    vid1 = cv2.VideoCapture(0) #replace name with 0 for webcam????
    print('capture started')

    while(vid1.isOpened()):
        _,frame1 = vid1.read()
        frame1 = imutils.resize(frame1, width=WIDTH, height=HEIGHT)
        if frame1[0][0][0] > 150:
            hue_shift_frame(frame1, 90)

def display_cam():
    cam = cv2.VideoCapture(0)

    while cam.isOpened():
        _,frame = cam.read()
        frame = imutils.resize(frame, width=400)
        cv2.imshow('cam', frame)
        cv2.waitKey(1)

def main():
    hue_shift_testharness()


main()