class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        self.engine = engine # Composition: Car HAS-A Engine

    def start_engine(self):
        self.engine.start() # Access Engine's method via Car

engine = Engine()
car = Car(engine)
car.start_engine()

