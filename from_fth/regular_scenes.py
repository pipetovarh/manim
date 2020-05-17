from manimlib.imports import *

fth_font = "EberaNew"
offset = [0,0.2,0]
redcol = RED_E
grid = ScreenGrid()
svgdir = "/Users/felipetovarhenao/ManimInstall/manim-master/media/designs/svg_images/"
snddir = "./media/designs/sounds/"
def find_angle(a_, b_): 
    if (a_ <= b_):
        return math.acos(a_/b_* -1)
    elif (b_ < a_):
        return math.acos(b_/a_)

class OpeningTitle(Scene): 
    CONFIG  = {
        "camera_config":{"background_color": BLACK}
    }
    def construct(self):
        mycolors = [BLUE, TEAL, GREEN, YELLOW, GOLD, RED, MAROON, PURPLE]
        mycolors = [WHITE, LIGHT_GREY, DARK_GREY, LIGHT_GREY]
        a = 7.4/1.5
        b = 0.6/1.5
        c = np.sqrt(a**2 + b**2)
        theta = find_angle(a,b)
        sq1 = Square(side_length = a+b, color = DARK_BLUE, fill_opacity = 0.03).rotate(PI/4).move_to(offset)
        sqg = VGroup()
        words= VGroup()
        title = Text("c r i t i c a l   b a n d", color=redcol, font = fth_font, stroke_width = 1, stroke_color = DARK_GREY, stroke_opacity = 1).scale(2.5).move_to(ORIGIN+offset)
        subtitle = Text("v  i  d  e  o     s  e  r  i  e  s", color=redcol, font = fth_font,stroke_width = 1, stroke_color = DARK_GREY, stroke_opacity = 1).move_to(DOWN + offset)
        author = Text("w w w . f e l i p e - t o v a r - h e n a o . c o m", font = fth_font, color=WHITE, stroke_width=0.5, stroke_color=DARK_BLUE).scale(0.5).move_to((DOWN*3.9)+[0,0.1,0])
        words.add(title)
        words.add(subtitle)
        for i in range(60):
            sqg.add(sq1.copy().set_stroke(mycolors[i%len(mycolors)], 0.5))
            sq1.rotate(theta).scale(c/(a+b))  
        self.add_sound(snddir + "snd.wav")
        self.wait(0.2)
        self.play(
            Write(sqg, run_time=7.5, rate_func = lingering, stroke_width=1, lag_ratio = 0.01, stroke_color = DARK_BLUE),
            Write(words, run_time = 6, lag_ratio = 0, stroke_color=BLUE),
            Write(author, run_time = 6, lag_ratio = 0, stroke_color=BLUE, stroke_width=0),
        )
        self.play(
            FadeOut(sqg),
            FadeOut(words),
            FadeOut(author),
            run_time = 1.5
        )

class EpisodeTitle(Scene):
    def construct(self):
        epititle = Text("t i l i n g   c a n o n s", font = fth_font, stroke_width = 0, stroke_color = DARK_GREY, color = redcol).scale(1.5).move_to(ORIGIN + offset)
        episubtitle = Text("p  a  r  t   I", font = fth_font, stroke_width = 0, stroke_color = DARK_GREY, color = redcol).move_to(ORIGIN+DOWN+offset)
        episode = VGroup().add(epititle, episubtitle)
        self.wait(0.3)
        self.play(
            FadeIn(episode, lag_ratio = 0, rate_func = rush_into),
            run_time = 0.5
        )
        self.wait(1.5)
        self.play(
            FadeOut(episode)
        )
        self.wait()

class TextOnly(Scene):
    def construct(self):
        totalHeight = 0
        totalWidth = 0
        textItems = [ # text sequence
            "Possible Vuza Canons:",
            "   • [0,0,0,1]",
            "   • {0,1,2,3,4}"
        ]
        waitTimes = [1,3,3] # timing between text
        lines = VGroup()
        stpt = np.array([-6, 3, 0])
        i = 0
        offset = 0
        spacing = 0.3
        for t in textItems:
            tmp = Text(t, font=fth_font).align_to(stpt, UL).shift([0, -offset, 0])
            lines.add(tmp)
            i += 1
            offset += tmp.get_height() + spacing
        i = 0
        for l in lines:
            self.play(
                Write(l)
            )
            self.wait(waitTimes[i])
            i += 1

class MusicExample(Scene): 
    def construct(self):
        example = VGroup()
        filename = "sampscore3.svg"
        mus = SVGMobject(svgdir + filename, stroke_width = 0.3,color=DARKER_GREY).scale(2.3)
        fw = mus.get_width()
        fh = mus.get_height()
        frame = RoundedRectangle(width=fw, height=fh, corner_radius=0.2, fill_color=WHITE, fill_opacity=1, stroke_width=2, stroke_color=BLUE).move_to(mus.get_center()).scale(1.15)
        subtitle = Text("Ex. 1: Interval cycles from «...de lo voluble...»", t2c = {"«...de lo voluble...»":RED}, font = fth_font, color=BLUE).scale(0.5).move_to(frame.get_bottom() + DOWN*0.5)
        example.add(subtitle,frame, mus)
        self.play( 
            Write(example, lag_ratio=0, stroke_width = 2),
            run_time=2
        )
        self.add_sound(snddir+"playback.mp3")
        self.wait(4)

class Subscribe(Scene):
    def construct(self):
        logos = VGroup()
        text = VGroup()
        logonames = ["patreon", "youtube", "soundcloud"]
        labels = ["/support", "/subscribe", "/follow"]
        xrange = 9
        st = np.array([-xrange/2,1.8,0])
        incr = np.array([xrange/(len(logonames)-1), 0, 0])
        for i in range(len(logonames)):
            logodir = svgdir + "logos/" + logonames[i] + ".svg"
            l = SVGMobject(logodir).scale(0.6).move_to(ORIGIN+st+(incr*i))
            t = Text(labels[i], font = fth_font).move_to(l.get_center() + DOWN*1.3)
            logos.add(l)
            text.add(t)
        logos[0][0].set_stroke(BLACK, width=0)
        logos[1][0].set_fill(RED)
        logos[1][1].set_stroke(BLACK, width=0)
        logos[2].set_fill(ORANGE)
        # self.add_sound("./media/designs/sounds/sound3.aif")
        author = Text("w w w . f e l i p e - t o v a r - h e n a o . c o m", font = fth_font, color=WHITE, stroke_width=0.5, stroke_color=WHITE).scale(0.5).move_to((DOWN*3.8)+[0,0.1,0])
        self.play(
            Write(logos, lag_ratio=0, stroke_color=WHITE),
            Write(text, lag_ratio=0, stroke_color=WHITE),
            Write(author, lag_ratio=0),
            run_time = 3
        )
        self.add_sound(snddir + "wave.aif")
        self.play(
            *[ApplyWave(mob) for mob in logos],
            run_time=1.3
        )
        self.wait(2.25)
        self.play(
            FadeOut(logos),
            FadeOut(text),
            FadeOut(author)
        )
        self.wait(1)







        

    












