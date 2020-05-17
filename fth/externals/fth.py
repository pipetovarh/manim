from manimlib.imports import *

fth_font = "EberaNew"
media_dir = "./fth/media/"
svg_dir = media_dir + "svg/"
audio_dir = media_dir + "audio/"

TC = np.array([0, 3, 0])
TL = np.array([-6, 3, 0])
TR = np.array([-6, 3, 0])
LE = np.array([-6, 0, 0])
RE = np.array([6, 0, 0])
BC = np.array([0, -3, 0])
BL = np.array([-6, 3, 0])
BR = np.array([6, 3, 0])
CRT = np.array([1, 3, 0])
CR = np.array([1, 0, 0])
CRB = np.array([1, 3, 0])

def find_angle(a_, b_): 
    if (a_ <= b_):
        return math.acos(a_/b_* -1)
    elif (b_ < a_):
        return math.acos(b_/a_)
