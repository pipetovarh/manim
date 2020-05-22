from manimlib.imports import *
from fth.imports import *

class ExampleA(Scene): 
    def construct(self):
        example = VGroup()
        mus = SVGMobject(svg_dir + "/tiling canons/ex_1_1.svg", stroke_width = 1,color=DARKER_GREY).scale(0.8)
        fw = mus.get_width()
        fh = mus.get_height()
        frame = RoundedRectangle(width=fw + 0.5, height=fh + 0.5, corner_radius=0.2, fill_color = PAPER, fill_opacity=1, stroke_width=3, stroke_color=BLUE).move_to(mus.get_center())
        subtitle = Text("Ex. 1: tiling canon", font = fth_font, color=BLUE).scale(0.65).move_to(frame.get_bottom() + DOWN*0.5)
        example.add(subtitle,frame)
        self.play( 
            Write(example, lag_ratio=0, stroke_width = 2),
            Write(mus, lag_ratio=0, stroke_width = 2),
            run_time=2
        )
        sf1 = audio_dir + "tiling canons/ex_1_1.mp3"
        self.add_sound(sf1)
        self.wait(6.5)
        v1 = [25, 26, 28, 31]
        v2 = [29, 30, 32, 35]
        v3 = [33, 34, 36, 27]
        allv = [v1, v2, v3]
        self.add_sound(audio_dir + "tiling canons/ex_1_2.mp3")
        for i, v in enumerate(allv):
            t = Text("voice " + str(i+1), font=fth_font, color = RED).align_to(frame, UL).shift(UP*0.5).scale(0.65)
            self.play(
                *[ApplyMethod(mus[x].set_fill, RED) for x in v],
                CircleIndicate(mus[v[0]], color=DARK_BLUE, run_time = 1.6),
                FadeInFrom(t, LEFT)
            )
            self.play(
                ApplyMethod(mus.set_fill, BLACK),
                FadeOut(t)
            )
        self.wait()
        example.add(mus)
        self.play(
            ApplyMethod(example.move_to, DOWN*2),
        )
        self.wait()

        # self.wait(4)
        # self.play(
        #     FadeOut(example)
        # )
        # self.wait()



        
        

    












