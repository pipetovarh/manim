from manimlib.imports import *
from random import *
fth_font = "EberaNew"
fth_sym = "Petrucci"
media_dir = "./fth/media/"
svg_dir = media_dir + "svg/"
audio_dir = media_dir + "audio/"
img_dir = media_dir + "images/"
PAPER = "#FFFBEA"

FTH_BG = "#0D1117"      #"#0F1114" "#0e1111" 
FTH_TXT = "#FEF9E7"     #"#FFFBEA"
FTH_PAPER = "#FFFBEA"
FTH_COL_A = BLUE # "#EC7063"
FTH_COL_B = BLUE_E
# LETTER_NOTATION = {
#     'A': 9,
#     'B': 10,
#     'C': 0,
#     'D': 1,
#     'E': 4
#     'F': ,
#     'G':
# }

TC = np.array([0, 3, 0])
TL = np.array([-6, 3, 0])
TR = np.array([6, 3, 0])
LE = np.array([-6, 0, 0])
RE = np.array([6, 0, 0])
BC = np.array([0, -3, 0])
BL = np.array([-6, -3, 0])
BR = np.array([6, -3, 0])
TCR = np.array([1, 3, 0])
CR = np.array([1, 0, 0])
BCR = np.array([1, -3, 0])

def find_angle(a_, b_): 
    if (a_ <= b_):
        return math.acos(a_/b_* -1)
    elif (b_ < a_):
        return math.acos(b_/a_)

def linden(axiom, rules, generations = 1):
    out = ""
    for i in range(len(axiom)):
        for j in rules:
            if len(j) != 2:
                raise "rules must only contain size 2 arrays"
            else:
                if axiom[i] == j[0]:
                    out += j[1]
    if generations > 0:
        return linden(out, rules, generations - 1)
    else:
        return out

def distance(L1, L2):
    out = 0
    for i, j in zip(L1, L2):
        out += (i-j)**2
    return np.sqrt(out)

def list_mod(L, M = 12):
    for i, l in enumerate(L):
        L[i] = l % M
    return L

def setT(mset, T = 0, mod = 12):
    for i, num in enumerate(mset):
        mset[i] = (num+T)%mod
    return sorted(mset)

def setI(mset, I = 0, mod = 12):
    for i, num in enumerate(mset):
        mset[i] = (mod-num) % mod
    return setT(sorted(mset), T = I)

def make_comment(t):
    cmt = VGroup()
    txt = Text(t, font = fth_font, stroke_width = 0, color = FTH_TXT).scale(0.35)
    frame = RoundedRectangle(width=txt.get_width() + 0.125, height=txt.get_height() + 0.125, corner_radius=0.02, fill_color = FTH_COL_B, fill_opacity=1, stroke_width=2, stroke_color=FTH_TXT)
    cmt.add(frame, txt).move_to(TR+UR*0.85).align_to(TR+UR*0.65, UR)
    return cmt

def make_footnote(t):
    cmt = VGroup()
    txt = Text(t, font = fth_font, stroke_width = 0, color = FTH_TXT).scale(0.35)
    frame = RoundedRectangle(width=txt.get_width() + 0.125, height=txt.get_height() + 0.125, corner_radius=0.02, fill_color = FTH_COL_B, fill_opacity=1, stroke_width=2, stroke_color=FTH_TXT)
    cmt.add(frame, txt).move_to(BL+DL*0.85).align_to(BL+DL*0.65, DL)
    return cmt

def make_header(t):
    pos = TC + UP*0.7
    txt = Text(t, font = fth_font, stroke_width = 0, color = FTH_COL_A).scale(1).move_to(pos).align_to(pos, UP)
    return txt

def make_text(t, pos = TL, line_index = 0, bullet = True, indent = 0, highlight = {}):
    line = VGroup()
    pt = Text("•", font = fth_font, stroke_width = 0, color = BLUE).scale(0.75).move_to(pos + LEFT*0.2).shift((DOWN * 0.5 * line_index) + DOWN*0.18)
    txt = Text(t, font = fth_font, stroke_width = 0, color = FTH_TXT, t2c = highlight).scale(0.75).move_to(pos).align_to(pos, UL).shift(DOWN * 0.5 * line_index)
    if bullet == True:
        line.add(pt)
    line.add(txt)
    return line.shift(RIGHT*0.5*indent)

def make_score(filedir, scl = 1, caption = " ", pos = ORIGIN):
    score = VGroup()
    mus = SVGMobject(filedir, stroke_width = 1, color = FTH_BG).scale(scl)
    fw = mus.get_width()
    fh = mus.get_height()
    frame = RoundedRectangle(width=fw + 0.5, height=fh + 0.5, corner_radius=0.2, fill_color = FTH_TXT, fill_opacity=1, stroke_width=3, stroke_color = FTH_COL_A).move_to(mus.get_center())
    subtitle = Text(caption, font = fth_font, color = FTH_COL_A).scale(0.55).move_to(frame.get_bottom() + DOWN*0.35)
    score.add(frame, subtitle, mus).move_to(pos)
    return score

class MCircle(VGroup):
    CONFIG = {
        "theta": TAU/12,
        "stored_sets": [],
        "sets": VGroup(),
        "circle": VGroup()
    }
    def __init__(self, mod = 12, radius = 1.5, **kwargs):
        digest_config(self, kwargs)
        super().__init__(**kwargs)
        self.mod = mod
        self.theta = TAU/self.mod
        self.radius = radius
        self.sets = VGroup()
        self.stored_sets.clear()
        self.circle = VGroup(Circle(radius = self.radius, color = RED))
        self.sets = VGroup()
        self.gen_circle()

    def gen_circle(self):
        points = VGroup()
        labels = VGroup()
        for i in range(self.mod):
            tmp_theta = self.theta*-i + PI/2
            xyz = np.array([math.cos(tmp_theta) * self.radius, math.sin(tmp_theta) * self.radius, 0])
            p = Dot(color = RED).move_to(xyz).scale(0.75)
            n = Text(str(i), font = fth_font, color = FTH_TXT).move_to(xyz*1.15).scale(0.5)
            labels.add(n)
            points.add(p)
        self.circle.add(points, labels)
        self.add(self.sets, self.circle)  

    def get_sets(self):
        return self.stored_sets

    def add_set(self, mset, color = YELLOW):
        new_xyz = []
        new_xyz.clear()
        mset = sorted(list_mod(mset, self.mod))
        self.stored_sets.append([mset, color])
        for s in mset:
            new_xyz.append(tuple(self[1][1][s%self.mod].get_center()))
        shape = Polygon(*new_xyz, stroke_width = 1.5, color = color)
        self[0].add(shape)
        return self

    def set_mod(self, val):
        self.mod = val
    
    def reset(self, keep_sets = True):
        temp_pos = self[1].get_center()
        temp_sets = self.stored_sets.copy()
        self.__init__(mod = self.mod)
        if keep_sets:
            for s in temp_sets:
                self.add_set(setT(s[0], 0, self.mod), color = s[1])
        else: 
            self.stored_sets.clear()
            self[0].remove()
        return self.move_to(temp_pos)

    def transpose(self, T, set_index = 0):
        self[0][set_index].rotate(self.theta * -T, about_point = self.get_center())
        new_set = setT(self.stored_sets[set_index][0], T = T, mod = self.mod)
        self.stored_sets[set_index][0] = new_set
        return self
    
    def inversion(self, I = 0, set_index = 0):
        self[0][set_index].flip(UP, about_point = self.get_center())
        new_set = setI(self.stored_sets[set_index][0], mod = self.mod)
        self.stored_sets[set_index][0] = new_set
        return self 

class SetsFromCircle(MCircle):
    def __init__(self, mobject, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.circle = mobject
        for i, s in enumerate(self.circle.get_sets()):
            txt = Text(str(s[0]), font = fth_font, color = s[1]).scale(0.4).align_to(self.circle[1], DL).shift(DOWN*0.2*i + DOWN*0.2)
            self.add(txt)

    def show(self, mobject):
        self.__init__(mobject)

class ModCircle(Square):
    """
        The ModCircle class creates a mod-n circle 
        in which polygon-style sets can be inscribed 
        via the ModSet class
    """
    CONFIG = {
        "radius": 1.5,
        "mod": 12,
        "theta": -TAU/12,
        "txt_size": 0.5,
        "node_size": 1
    }
    def __init__(self, mod = 12, **kwargs):
        digest_config(self, kwargs)
        Square.__init__(self, side_length = self.radius * 3, stroke_opacity = 0, **kwargs) # Frame of ModCircle
        self.set_mod(mod)
        self.draw()
    
    def draw(self):
        # draw() is meant to be used after self.mod has been used
        previous_pos = self.get_center()
        self.reset()
        self.set_theta()
        self.move_to(ORIGIN)
        nodes = VGroup()
        nums = VGroup()
        for i in range(self.mod):
            x = np.cos((self.theta*i) + PI/2) * self.radius
            y = np.sin((self.theta*i) + PI/2) * self.radius
            nodes.add(Dot(color = RED).scale(self.node_size).move_to((x, y, 0)))
            nums.add(Text(str(i), font = fth_font, color = FTH_PAPER).scale(self.txt_size).move_to((x * 1.2, y * 1.2, 0)))
        self.add(Circle(radius = self.radius), nodes, nums)
        self.move_to(previous_pos)

    def reset(self):
        for mo in self:
            for smo in mo:
                mo.remove(smo)
            self.remove(mo)

    def resize(self, num):
        self.radius *= num
        self.txt_size *= num
        self.node_size *= num
        return self

    def set_theta(self):
        self.theta = -TAU/self.mod
        return self

    def set_mod(self, M):
        # set_mod() is meant to be used outside of self.play
        self.mod = M
        return self

    def get_nodes(self):
        return self[2]

    def get_mod(self):
        return self.mod

class ModSet(VGroup):
    """
        The ModSet class creates a geometric representation of 
        a mod-n set in the form of a polygon. This polygon is inscribed 
        inside a ModCircle, which must be given to initiate the class.
    """
    CONFIG = {
        'mset': []
    }
    def __init__(self, circle, mset, color = YELLOW, **kwargs):
        # circle must be an ModCircle class and modset an array of integers
        digest_config(self, kwargs)
        VGroup.__init__(self, **kwargs)
        self.circle = circle.copy()
        self.color = color
        self.set_mset(mset)
        self.reset()
        self.build_shape()

    def draw(self):
        # draw() is meant to be used inside self.play() after set_circle() has been called
        self.reset()
        self.build_shape()

    def build_shape(self):
        vertices = []
        for i in self.mset:
            pos = self.circle.get_nodes()[i].get_center()
            vertices.append(pos)
        shape = Polygon(*vertices, color = self.color, stroke_width = 2)
        self.add(shape)
        
    # Setters
    def set_mset(self, s):
        self.mset = sorted(s)

    def set_circle(self, circle):
        self.circle = circle.copy()
        self.circle.draw()
        self.set_mset(setT(self.mset, T = 0, mod = self.circle.mod))
    
    def reset(self):
        for mo in self:
            for smo in mo:
                mo.remove(smo)
            self.remove(mo)
        self.add(Square(side_length = self.circle[0].side_length, stroke_opacity = 0).move_to(self.circle))

    # Set transformations
    def transposition(self, T):
        self.set_mset(setT(self.mset, T = T, mod = self.circle.mod))
        self.rotate(self.circle.theta * T)

    def inversion(self):
        self.set_mset(setI(self.mset, mod = self.circle.mod))
        self.flip(UP)

    def get_mset(self):
        return [sorted(self.mset), self.color]

class ModText(VGroup):
    def __init__(self, modset, **kwargs):
        digest_config(self, kwargs)
        VGroup.__init__(self, **kwargs)
        self.draw(modset)

    def draw(self, modset):
        self.pos = self.get_center()
        self.reset()
        self.modset = modset.get_mset()
        self.modtext = Text(str(self.modset[0]), font = fth_font, color = self.modset[1]).scale(0.5).move_to(self.pos)
        self.add(self.modtext)

    def reset(self):
        for mo in self:
            for smo in mo:
                mo.remove(smo)
            self.remove(mo)


    







    
    










