from kivy.uix.widget import Widget
from kivy.app import App
from kivy.vector import Vector
from kivy.properties import NumericProperty,ReferenceListProperty,ObjectProperty
from kivy.clock import Clock
from random import randint

class PongPaddle(Widget):
     score=NumericProperty(0)
     def bounce_ball(self,ball):
      if self.collide_widget(ball):
          ball.v_x *=-1


class PongBall(Widget):
    v_x=NumericProperty(0)
    v_y=NumericProperty(0)
    vnet=ReferenceListProperty(v_x,v_y)
    def move(self):
        self.pos=Vector(*self.vnet)+self.pos
class PongGame(Widget):
   # PongPaddle=ObjectProperty(None)
    ball=ObjectProperty(None)
    p1=ObjectProperty(None)
    p2 = ObjectProperty(None)
    def serve(self):
        self.ball.vnet=Vector(5,0).rotate(randint(0,360))
    def update(self,dt):
        self.ball.move()
        if (self.ball.y<0 )or (self.ball.y>self.height-50):
            self.ball.v_y*=-1
        if (self.ball.x<0 ):
            self.ball.v_x *= -1
            self.p2.score+=1
        if  (self.ball.x>self.width-50):
            self.ball.v_x*=-1
            self.p1.score += 1
        self.p1.bounce_ball(self.ball)
        self.p2.bounce_ball(self.ball)

    def on_touch_move(self,touch):
        if touch.x<self.width/1/4:
            self.p1.center_y=touch.y
        if touch.x>self.width*3/4:
            self.p2.center_y=touch.y
class PongApp(App):

    def build(self):
        game = PongGame()
        game.serve()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

PongApp().run()