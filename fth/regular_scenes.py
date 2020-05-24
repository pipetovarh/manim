from manimlib.imports import *
from fth.imports import *
import random
from collections import deque

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
        circ = MCircle(12).move_to(RIGHT*3)
        csets = SetsFromCircle(circ)
        # for mo in items:
        #     self.play(
        #         Write(mo)
        #     )
        # print(circ.mod)
        # self.play(
        #     FadeInFrom(fn, LEFT)
        # )
        # self.play(
        #     FadeInFrom(cmt, RIGHT)
        # )
        self.play(
           # FadeOut(mus), 
            Write(circ),
        )
        self.play(
            circ.add_set, [0,3,5],
        )
        csets.show(circ)
        self.play(
            Write(csets)
        )
        self.wait()
        self.play(
            circ.add_set, [0,3,4,8,12], BLUE,
            circ.add_set, [4,8,11], PURPLE,
            csets.show, circ,
        )
        self.wait()
        self.play(
            circ.inversion, 1,
            csets.show, circ,
        )
        for _ in range(3):
            self.play(
                circ.transpose, 0,
                csets.show, circ,
            )
        self.play(
            circ.add_set, [0,4,8], PINK,
            circ.transpose, 2, {"set_index": 1},
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
        circ.transpose(3,0)
        self.play(
            circ.transpose, 3, {"set_index": 0},
            circ.transpose, 3, {"set_index": 1},
        ) 
        self.play(
            circ.inversion, 3, 0,
            circ.inversion, 3, 1,
        )
        self.wait()

class NewIntro(Scene):
    def construct(self):
        # colorList = [RED_E, MAROON_E, PURPLE_E, BLUE_E, TEAL_E, GREEN_E, YELLOW_E, GOLD_E]
        colorList = [DARKER_GREY, BLACK, DARKER_GREY, DARK_GREY, LIGHT_GREY, WHITE, LIGHT_GREY, DARK_GREY]
        A = 5.5
        B = A * 0.083
        AB = A + B
        C = AB*0.5*np.sqrt(3)
        x = B * np.sin(PI/3)
        y = A - (B * np.cos(PI/3))
        theta = np.arctan(x/y)
        Z = x/np.sin(theta)
        c = AB*0.5*np.tan(PI/6)
        scl = Z/AB
        vertices = [
            (0,0,0),
            (AB, 0, 0),
            (AB/2, C, 0)
        ]
 
        def make_tri(num):
            new_vertices = []
            numv = len(vertices)
            for i in range(numv):
                new_vertices.append(vertices[(i+num)%numv])
            col = colorList[num%len(colorList)]
            sub_tri = Polygon(*new_vertices, stroke_width = 0.5, fill_color = col, fill_opacity = 1, stroke_color = BLACK).move_to(ORIGIN).shift((0,C*0.5-c,0))
            shape = VGroup(Square(side_length = AB, stroke_opacity = 0, stroke_width = 0.5), sub_tri).move_to(ORIGIN).rotate(PI)
            return shape
        logo = VGroup() 
        rotate = 0
        for i in range(16):
            triangle = make_tri(rotate)
            tri = triangle.copy()
            tri.rotate(-theta*i, about_point = tri[0].get_center()).scale(scl**i)
            logo.add(tri[1])
            last_scl = scl**i
            last_theta = -theta*i
            rotate += 1

        old_tri = tri.copy()
        for i in range(1, 16):
                triangle = make_tri(rotate)
                triangle.rotate(last_theta, about_point = old_tri[0].get_center()).scale(last_scl)
                tri = triangle.copy()
                tri.rotate(-theta*i, about_point = tri[0].get_center()).scale(scl**i)
                logo.add(tri[1])
                new_tri = tri.copy()
                new_scl = scl**i
                rotate += 1

        self.play(
            Write(logo.move_to(ORIGIN), lag_ratio = 0.02, rate_func = lingering, stroke_color = DARK_GREY, stroke_width = 1.5), 
            # logo.rotate, TAU,
            run_time = 5
        )
        self.wait(3)

class NewCircle(Scene):
    def construct(self):
        c = ModCircle(12).move_to(RIGHT)
        s = ModSet(c, [0,4,8])
        t = ModText(s).move_to(BL)
        def update_set(obj):
            obj.move_to(c)
        s.add_updater(update_set)
        self.play(
            Write(s), 
            Write(c),
            Write(t)
        )
        for i in range(2):
            c.resize(0.9)
            s.set_circle(c)
            self.play(
                c.draw,
                s.draw,
                t.draw, s
            )
            self.play(
                s.transposition, 1,
                t.draw, s
            )
            self.play(
                s.inversion,
                t.draw, s
            )
            self.play(
                c.shift, LEFT*0.5
            )
        self.play(
            c.move_to, ORIGIN
        )
        for i in range(10, 20):
            c.set_mod(i)
            s.set_circle(c)
            self.play(
                c.draw,
                s.draw,
                t.draw, s,
            )
        for i in range(5):
            self.play(
                s.transposition, -1,
                t.draw, s,
            )
            self.play(
                s.inversion, 
                t.draw, s,
            )
        self.wait()








