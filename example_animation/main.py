from manim import *

class SimpleAnimation(Scene):
    def construct(self):
        square = Square(color=BLUE, fill_opacity=0.5)
        
        self.play(Create(square))
        self.wait(1)
        
        self.play(Rotate(square, angle=PI / 4))  # Rotate by 45 degrees
        self.wait(1)
        
        self.play(square.animate.set_fill(GREEN))
        self.wait(1)
        
        self.play(FadeOut(square))

