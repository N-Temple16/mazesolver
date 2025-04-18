from window import Line, Point

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        # Left wall
        left_line = Line(Point(x1, y1), Point(x1, y2))
        if self.has_left_wall:
            self._win.draw_line(left_line)
        else:
            self._win.draw_line(left_line, "white")
            
        # Top wall
        top_line = Line(Point(x1, y1), Point(x2, y1))
        if self.has_top_wall:
            self._win.draw_line(top_line)
        else:
            self._win.draw_line(top_line, "white")
            
        # Right wall
        right_line = Line(Point(x2, y1), Point(x2, y2))
        if self.has_right_wall:
            self._win.draw_line(right_line)
        else:
            self._win.draw_line(right_line, "white")
            
        # Bottom wall
        bottom_line = Line(Point(x1, y2), Point(x2, y2))
        if self.has_bottom_wall:
            self._win.draw_line(bottom_line)
        else:
            self._win.draw_line(bottom_line, "white")
    
    def draw_move(self, to_cell, undo=False):
        x1 = (self._x1 + self._x2) // 2
        y1 = (self._y1 + self._y2) // 2
        x2 = (to_cell._x1 + to_cell._x2) // 2
        y2 = (to_cell._y1 + to_cell._y2) // 2

        if undo:
            color = "gray" 
        else:
            color = "red"

        line = Line(Point(x1, y1), Point(x2, y2))
        self._win.draw_line(line, color)