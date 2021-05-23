# Class which contains info about each task
class Task:
    # Constructor of class
    def __init__(self, r, p, q, C):
        # r - time of accessibility
        # p - time of execution
        # q - time of deliver the task
        self.r = int(r)
        self.p = int(p)
        self.q = int(q)
        self.C = 0


    # This is a definition used in printing an object
    def __str__(self):
        return "r: %d p: %d q: %d C: %d" % (self.r, self.p, self.q, self.C)

# Class for unordered tasks - they are sorted differently than the ordered ones
class NsetTask(Task):
    def __init__(self, r, p, q, C):
        super().__init__(r, p, q, C)

    # Operator Less Than overloaded
    def __lt__(self, other):
        self_r = self.r
        other_r = other.r
        return self_r < other_r

# Class for unordered tasks - they are sorted differently than the ordered ones
class GsetTask(Task):
    def __init__(self, othertask):
        super().__init__(othertask.r, othertask.p, othertask.q, othertask.C)

    # Operator Less Than overloaded
    def __lt__(self, other):
        self_q = self.q
        other_q = other.q
        return self_q < other_q