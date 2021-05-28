# Class which contains info about each task
class Task:
    # Constructor of class
    def __init__(self, p, d, w):
        # r - time of accessibility
        # p - time of execution
        # q - time of deliver the task
        self.p = int(p)
        self.d = int(d)
        self.w = int(w)

    # This is a definition used in printing an object
    def __str__(self):
        return "p: %d d: %d w: %d" % (self.p, self.d, self.w)
