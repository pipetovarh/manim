from manimlib.imports import *
from fth.imports import *

class OpeningTitle(Scene): 
    CONFIG  = {
        "camera_config":{"background_color": BLACK},
        "mycolors": [WHITE, LIGHT_GREY, DARK_GREY, LIGHT_GREY],
        "a" : 4.6,
        "b": 0.4,
        "c": 0,
        # "titletext" = "c r i t i c a l   b a n d",
        "titletext": "the beauty of noise",
        "subtitle_text": "v  i  d  e  o     s  e  r  i  e  s",
        "website_text": "w w w . f e l i p e - t o v a r - h e n a o . c o m"
    } 

    def construct(self):
        self.c = np.sqrt(self.a**2 + self.b**2)
        theta = find_angle(self.a,self.b)
        sq1 = Square(side_length = self.a+self.b, color = DARK_BLUE, fill_opacity = 0.03).rotate(PI/4).scale(0.95)
        sqg = VGroup()
        words = VGroup()
        title = Text(self.titletext, color=RED_C, font = fth_font, stroke_width = 1, stroke_color = DARK_GREY, stroke_opacity = 1).scale(2.5)
        subtitle = Text(self.subtitle_text, color=RED_C, font = fth_font,stroke_width = 1, stroke_color = DARK_GREY, stroke_opacity = 1).move_to(DOWN)
        website = Text(self.website_text, font = fth_font, color=WHITE, stroke_width=0.5, stroke_color=DARK_BLUE).scale(0.5).move_to(DOWN*3.6)
        words.add(title, subtitle).move_to(ORIGIN)
        words.add(title, subtitle)
        for i in range(67):
            color_index = i % len(self.mycolors)
            sqg.add(sq1.copy().set_stroke(self.mycolors[color_index], 0.5))
            sq1.rotate(theta).scale(self.c/(self.a+self.b))  
        self.add_sound(audio_dir + "snd.wav")
        self.wait(0.2)
        self.play(
            Write(sqg, run_time=7.5, rate_func = lingering, stroke_width=1, lag_ratio = 0.01, stroke_color = DARK_BLUE),
            Write(words, run_time = 6, lag_ratio = 0, stroke_color=BLUE),
            Write(website, run_time = 6, lag_ratio = 0, stroke_color=BLUE, stroke_width=0),
        )
        self.play(
            FadeOut(sqg),
            FadeOut(words),
            FadeOut(website),
            run_time = 1.5
        )

class EpisodeTitle(Scene):
    CONFIG = {
        "title": "t i l i n g  c a n o n s",
        "part": "part 1:",
        "subtitle": "basic properties",
    }
    def construct(self):
        epititle = Text(self.title, font = fth_font, stroke_width = 0, color = WHITE).scale(1.5).move_to(ORIGIN)
        epipart = Text(self.part, font = fth_font, stroke_width = 0, color = WHITE).move_to(epititle).shift(DOWN*1.5)
        episubtitle = Text(self.subtitle, font = fth_font, stroke_width = 0, color = RED_C).move_to(epipart).shift(DOWN*0.5)
        episode = VGroup().add(epititle, epipart, episubtitle).move_to(ORIGIN)
        self.wait(0.3)
        self.play(
            Write(episode, lag_ratio = 0),
            run_time = 2
        )
        self.wait(1)
        self.play(
            FadeOut(episode)
        )
        self.wait(1)

class TextOnly(Scene):
    CONFIG = {
        "spacing": 0.8
    }
    def construct(self):
        totalHeight = 0
        totalWidth = 0
        textItems = [ # text sequence
            "Possible Vuza Canons:",
            "   • [0,0,0,1]",
            "   • {0,1,2,3,4}"
        ]
        waitTimes = [1,3,3] # timing between text
        for i in range(len(textItems)):
            line = Text(textItems[i], font=fth_font).align_to(TL, UL).shift(DOWN*i*self.spacing)
            self.play(
                Write(line)
            )
            self.wait(waitTimes[i])
            
class MusicExample(Scene): 
    def construct(self):
        example = VGroup()
        mus = SVGMobject(svg_dir + "sampscore3.svg", stroke_width = 0.3,color=DARKER_GREY).scale(2.3)
        fw = mus.get_width()
        fh = mus.get_height()
        frame = RoundedRectangle(width=fw, height=fh, corner_radius=0.2, fill_color=WHITE, fill_opacity=1, stroke_width=2, stroke_color=BLUE).move_to(mus.get_center()).scale(1.15)
        subtitle = Text("Ex. 1: Interval cycles from «...de lo voluble...»", t2c = {"«...de lo voluble...»":RED}, font = fth_font, color=BLUE).scale(0.5).move_to(frame.get_bottom() + DOWN*0.5)
        example.add(subtitle,frame, mus)
        self.play( 
            Write(example, lag_ratio=0, stroke_width = 2),
            run_time=2
        )
        self.add_sound(audio_dir+"playback.mp3")
        self.wait(4)
        self.play(
            FadeOut(example)
        )
        self.wait()

class Subscribe(Scene):
    CONFIG = {
        "h_spacing": 0.8
    }
    def construct(self):
        logos = VGroup()
        text = VGroup()
        logonames = ["patreon", "youtube", "soundcloud"]
        labels = ["/support", "/subscribe", "/follow"]
        xrange = 3*len(logonames)
        st = np.array([-xrange/2,1.8,0])
        incr = np.array([xrange/(len(logonames)-1), 0, 0])
        for i in range(len(logonames)):
            logodir = svg_dir + "logos/" + logonames[i] + ".svg"
            l = SVGMobject(logodir).scale(0.6).move_to(st+(incr*i))
            t = Text(labels[i], font = fth_font).move_to(l.get_center() + DOWN*1.3)

            if (logonames[i] == "youtube"):
                l[0].set_fill("#ff0000")
                l[1].set_stroke(BLACK, width=0)
            if (logonames[i] == "patreon"):
                l.set_stroke(BLACK, width=0)
            if (logonames[i] == "soundcloud"):
                l.set_color_by_gradient("#ff8800", "#ff3300").set_stroke(WHITE)
            logos.add(l)
            text.add(t)
        author = Text("w w w . f e l i p e - t o v a r - h e n a o . c o m", font = fth_font, color=WHITE, stroke_width=0.5, stroke_color=WHITE).scale(0.5).move_to(DOWN*3.6)
        self.play(
            Write(logos, lag_ratio=0, stroke_color=WHITE),
            Write(text, lag_ratio=0, stroke_color=WHITE),
            Write(author, lag_ratio=0),
            run_time = 3
        )
        # self.add_sound(audio_dir + "wave.aif")
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




        

    












