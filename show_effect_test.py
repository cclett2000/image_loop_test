##############################################
# name: show_effect_test.py
# programmer: Charles Lett Jr.
# created: 4/20/22
# modified: 4/20/22
# soundtrack for codin!
#   ^ https://www.youtube.com/watch?v=jY6yBTYxLko&t=199s
#     https://www.youtube.com/watch?v=_XJnVPM_F0c;
##############################################

# DESCRIPTION
#   Got bored and started perusing the source files of the game Quake III Arena (developed by ID
#   Software in 1999) and noticed that a lot of the effect textures have multiple files with
#   incrementing numbers. This gave me the idea to see if I could take a set of these textures
#   and create a way of looping them. This will be no where near as nice as how I assume ID software
#   animated effects in game but I feel like it's a nice little thing to test;

# DISCLAIMER
#   All images included in this program were created solely by ID Software and are only included
#   for demonstration purposes.;

# Package(s)
#   - opencv-python (cv2) - computer vision?;

# References
#   - Loop image in same window
#       - https://stackoverflow.com/questions/71704213/cv2-display-images-in-same-window-one-after-the-other;

import cv2
import os

effect_type = 5

# 0 = wait for input, > 0 = change every specified ms
# I assumed that the refresh rate in game is 20fps for flame effect
# so through some quick n' probably wrong calculation I estimated that 53 is
# close enough to simulate 20 fps (53 is for frametime)
#   ^ this could be completely wrong but it looks about what I remember so :P
refresh_rate = 80

def show_norm_fire():
    # variables
    file_path = "img/q3_fire"
    window_name = "Flame Effect Test"

    # generate list of textures in '/q3_fire_blue'
    file_names = os.listdir(os.path.abspath(file_path))

    # create window for use throughout execution
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    # loop for displaying textures
    while True:
        for image in file_names:
            texture = cv2.imread(file_path + "/" + image)
            cv2.imshow(window_name, texture)

            # set delay - 0 = wait for keypress, >0 = delay in ms before next img is displayed
            # only accepts int
            # welp, only way to stop it is to force quit
            cv2.waitKey(refresh_rate)

def show_blue_fire():
    # variables
    file_path = "img/q3_fire_blue"
    window_name = "Blue Flame Effect Test"

    # generate list of textures in '/q3_fire_blue'
    file_names = os.listdir(os.path.abspath(file_path))

    # create window for use throughout execution
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    # loop for displaying textures
    while True:
        for image in file_names:
            texture = cv2.imread(file_path + "/" + image)
            cv2.imshow(window_name, texture)

            # set delay - 0 = wait for keypress, >0 = delay in ms before next img is displayed
            # only accepts int
            # welp, only way to stop it is to force quit
            cv2.waitKey(refresh_rate)

# ow, my eyes
def show_blue_proto():
    # variables
    file_path = "img/q3_proto_blue"
    window_name = "Blue Flame Effect Test"

    # generate list of textures in '/q3_fire_blue'
    file_names = os.listdir(os.path.abspath(file_path))

    # create window for use throughout execution
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    # loop for displaying textures
    while True:
        for image in file_names:
            texture = cv2.imread(file_path + "/" + image)
            cv2.imshow(window_name, texture)

            # set delay - 0 = wait for keypress, >0 = delay in ms before next img is displayed
            # only accepts int
            # welp, only way to stop it is to force quit
            cv2.waitKey(refresh_rate)

def show_zap_scroll():
    # variables
    file_path = "img/q3_zap_scroll"
    window_name = "Blue Flame Effect Test"

    # generate list of textures in '/q3_fire_blue'
    file_names = os.listdir(os.path.abspath(file_path))

    # create window for use throughout execution
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    # loop for displaying textures
    while True:
        for image in file_names:
            texture = cv2.imread(file_path + "/" + image)
            cv2.imshow(window_name, texture)

            # set delay - 0 = wait for keypress, >0 = delay in ms before next img is displayed
            # only accepts int
            # welp, only way to stop it is to force quit
            cv2.waitKey(refresh_rate)

# might be missing some images? still brings me back to
# the days of playing on my dad's computer tho!
def show_tele_blue():
    # variables
    file_path = "img/q3_tele_blue"
    window_name = "Blue Flame Effect Test"

    # generate list of textures in '/q3_fire_blue'
    file_names = os.listdir(os.path.abspath(file_path))

    # create window for use throughout execution
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    # loop for displaying textures
    while True:
        for image in file_names:
            texture = cv2.imread(file_path + "/" + image)
            cv2.imshow(window_name, texture)

            # set delay - 0 = wait for keypress, >0 = delay in ms before next img is displayed
            # only accepts int
            # welp, only way to stop it is to force quit
            cv2.waitKey(refresh_rate)

def show_explosion1():
    # variables
    file_path = "img/q3_explosion1"
    window_name = "Blue Flame Effect Test"

    # generate list of textures in '/q3_fire_blue'
    file_names = os.listdir(os.path.abspath(file_path))

    # create window for use throughout execution
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    # loop for displaying textures
    while True:
        for image in file_names:
            texture = cv2.imread(file_path + "/" + image)
            cv2.imshow(window_name, texture)

            # set delay - 0 = wait for keypress, >0 = delay in ms before next img is displayed
            # only accepts int
            # welp, only way to stop it is to force quit
            cv2.waitKey(refresh_rate)

###############################################

if effect_type == 0: show_norm_fire()
if effect_type == 1: show_blue_fire()
if effect_type == 2: show_blue_proto()
if effect_type == 3: show_zap_scroll()
if effect_type == 4: show_tele_blue()
if effect_type == 5: show_explosion1()