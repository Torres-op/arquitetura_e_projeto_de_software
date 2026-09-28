from abc import ABC, abstractmethod

class Renderer(ABC):
    @abstractmethod
    def render_shape(self, shape_name: str):
        pass

class VectorRenderer(Renderer):
    def render_shape(self, shape_name: str):
        print(f"Desenhando {shape_name} com linhas.")

class PixelRenderer(Renderer):
    def render_shape(self, shape_name: str):
        print(f"Desenhando {shape_name} com pixels.")

class Shape(ABC):
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        self.renderer.render_shape("Círculo")

class Square(Shape):
    def draw(self):
        self.renderer.render_shape("Quadrado")

if __name__ == "__main__":
    vector = VectorRenderer()
    raster = PixelRenderer()

    circle_vector = Circle(vector)
    circle_raster = Circle(raster)
    
    square_vector = Square(vector)
    square_raster = Square(raster)

    circle_vector.draw()
    circle_raster.draw()
    square_vector.draw()
    square_raster.draw()