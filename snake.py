import turtle


class Snake:
    def __init__(self):
        self.body = []
        self.x = 0
        for _ in range(3):
            self.x += 20
            body_seg = turtle.Turtle("square")
            body_seg.color("white")
            body_seg.penup()
            body_seg.setx(self.x)
            self.body.append(body_seg)
        self.head = self.body[0]

    def move(self):
        self.head.forward(10)
        # make segments follow the previous segment
        prior_position = (self.head.xcor(), self.head.ycor())
        for segment in self.body:
            current_position = (segment.xcor(), segment.ycor())
            segment.goto(prior_position)
            prior_position = current_position

    def go_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def go_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def go_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def go_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def add_new_segment(self):
        new_seg = turtle.Turtle(shape="square")
        new_seg.penup()
        new_seg.setposition(self.body[-1].xcor(), self.body[-1].ycor())
        new_seg.color("white")
        self.body.append(new_seg)

    def position_head(self):
        return self.head.position()

    def get_segments_position(self):
        list_positions = []
        for seg in self.body[4:]:
            list_positions.append(seg.pos())
        return list_positions


