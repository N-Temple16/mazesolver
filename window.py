from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.__root = Tk()
        self.__root.title("Maze Solver")

        self.canvas = Canvas(self.__root, width=self.width, height=self.height)
        self.canvas.pack()

        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)
    
    def wait_for_close(self):
        self.running = True

        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2
        )


def main():
    win = Window(800, 600)

    win.draw_line(Line(Point(100, 100), Point(200, 200)), "red")
    win.draw_line(Line(Point(200, 200), Point(300, 300)), "black")
    win.draw_line(Line(Point(300, 300), Point(400, 400)), "blue")

    win.wait_for_close()

if __name__ == "__main__":
    main()