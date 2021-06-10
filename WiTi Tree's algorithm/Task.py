# Class which contains info about each task
class Task:
    # Constructor of class
    def __init__(self, p, w, d):
        # p - time of execution
        # w - punishment rate
        # d - requested time of execution end
        self.p = int(p)
        self.w = int(w)
        self.d = int(d)

    # This is a definition used in printing an object
    def __str__(self):
        return "p: %d w: %d d: %d" % (self.p, self.w, self.d)


# Compute punishment
# If task wasn't late punishment is 0
# If task is late then it is (C - d) * w
def punishment(task, EndOfExecution):
    return max((EndOfExecution - task.d) * task.w, 0)
