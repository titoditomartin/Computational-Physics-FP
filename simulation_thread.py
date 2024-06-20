import threading
import time
import queue

class SimulationThread(threading.Thread):
    def __init__(self, simulation_queue, model):
        super().__init__()
        self.simulation_queue = simulation_queue
        self.model = model
        self.running = True

    def run(self):
        while self.running:
            # Run the simulation step
            self.model.step()

            # Put the result into the queue to communicate with the GUI
            result = {
                'position': self.model.cart_position,
                'velocity': self.model.cart_velocity
            }
            self.simulation_queue.put(result)

            # Sleep to limit the simulation update rate (e.g., 60 updates per second)
            time.sleep(1/60)

    def stop(self):
        self.running = False
