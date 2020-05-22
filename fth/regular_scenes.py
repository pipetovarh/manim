from manimlib.imports import *
from fth.imports import *

class OpeningTitle(Scene): 
    CONFIG  = {
        "camera_config":{"background_color": FTH_BG},
        "mycolors": [WHITE, LIGHT_GREY, DARK_GREY, LIGHT_GREY],
        "a" : 4.6,
        "b": 0.4,
        "c": 0,
        "titletext": "a hidden noise",
        "subtitle_text": "essays on music",
        "website_text": "w w w . f e l i p e - t o v a r - h e n a o . c o m"
    } 

    def construct(self):
        self.c = np.sqrt(self.a**2 + self.b**2)
        theta = find_angle(self.a,self.b)
        sq1 = Square(side_length = self.a+self.b, color = DARK_BLUE, fill_opacity = 0.03).rotate(PI/4).scale(0.95)
        sqg = VGroup()
        words = VGroup()
        title = Text(self.titletext, color=RED_C, font = fth_font, stroke_width = 1, stroke_color = DARK_GREY, stroke_opacity = 1).scale(2.5)
        subtitle = Text(self.subtitle_text, color=WHITE, font = fth_font,stroke_width = 1, stroke_color = DARK_GREY, stroke_opacity = 1).move_to(DOWN)
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
        self.wait(0.3)

class EpisodeTitle(Scene):
    CONFIG = {
        "camera_config":{"background_color": FTH_BG},
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

class Subscribe(Scene):
    CONFIG = {
        "camera_config":{"background_color": FTH_BG},
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
                l.scale(1.25)
                l[0].set_fill("#f96854")
                l[2].set_fill("#052d49")
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

class TestFormat(Scene):
    CONFIG  = {
        "camera_config":{"background_color": FTH_BG}
    } 
    def construct(self):
        hdr = make_header("This is a header")
        line1 = make_text("This is a line without bullet point", bullet = False)
        line2 = make_text("This is an indented line with bullet point", line_index = 1, indent=1)
        line3 = make_text("This is an indented line without bullet point", line_index = 2, indent=2, bullet = False)
        line4 = make_text("This is another line", line_index = 3, bullet = False)
        fn = make_footnote("[1] This is a video foot note.\nIt can be quite long... very, very, very looooong\nor have many, many\nmany,\nmany lines too.")
        cmt = make_comment("This is a video comment\nwhich can occupy\nmany, many lines...\nmany, even if the text is too long... seriously... too... long!")
        mus = make_score(svg_dir + "tiling canons/ex_1_1.svg", caption = "This is a score caption", scl = 0.5, pos = DOWN)
        items = [hdr, line1, line2, line3, line4, mus]
        circ = MCircle(10).add_set([0,3,5]).move_to(RIGHT*2.8 + DOWN*0.5)
        csets = SetsFromCircle(circ)
        for mo in items:
            self.play(
                Write(mo)
            )
        print(circ.mod)
        self.play(
            FadeInFrom(fn, LEFT)
        )
        self.play(
            FadeInFrom(cmt, RIGHT)
        )
        self.play(
            FadeOut(mus), #ReplacementTransform(mus, circ),
            Write(circ),
            csets.show, circ,
        )
        self.wait()
        self.play(
            circ.add_set, [0,3,4,8,12], BLUE,
            circ.transpose, 3,
            csets.show, circ,
        )
        self.wait()
        self.play(
            circ.inversion,
            csets.show, circ,
        )
        self.wait()
        circ.set_mod(20)
        self.play(
            circ.reset, False,
            csets.show, circ,
        )
        self.wait()
        self.play(
            circ.add_set, [3,14,20], ORANGE,
            csets.show, circ,
        )
        self.play(
            circ.add_set, [5,10,21], GREEN,
            csets.show, circ,
        )
        circ.set_mod(24)
        self.play(
            circ.reset, True
        )
        self.wait()

class TestCircle(Scene):
    CONFIG  = {
        "camera_config":{"background_color": FTH_BG}
    } 
    def construct(self):
        setA = [0,4,7]
        setB = [0,5,10]
        c = MCircle().add_set(setA).transpose(T = 0)
        sets = SetsFromCircle(c)
        self.play(
            Write(c),
            Write(sets)
        )
        self.play(
            ApplyMethod(c.move_to, RIGHT),
            ApplyMethod(sets.show, c),
            ApplyMethod(sets.shift, RIGHT),
            run_time = 1
        )
        self.play(
            ApplyMethod(c.inversion, 3),
            ApplyMethod(c.move_to, RIGHT),
            ApplyMethod(sets.show, c),
            run_time = 1
        )
        c.move_to(RIGHT)
        self.play(
            ApplyMethod(c.add_set, [2,5,6], BLUE),
            ApplyMethod(sets.show, c),
        )
        self.play(
            ApplyMethod(c.reset, 8),
            ApplyMethod(sets.show, c),   
        )
        self.play(
            ApplyMethod(sets.show, c),   
        )
        self.wait(3)




