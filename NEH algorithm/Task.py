# Class which contains info about each task
class Task:
    # Constructor of class
    def __init__(self, TimesOfExecution, Index):
        # TimesOfExecution - list of times of execution on each machine
        # SumOfTimes - sum of times of execution on each machine
        self.Index = Index
        self.TimesOfExecution = MapStringToInt(TimesOfExecution)
        self.SumOfTimes = SumOfTimes(self)


def SumOfTimes(Task):
    sum = 0
    for Time in Task.TimesOfExecution:
        sum += Time
    return sum


def MapStringToInt(ListOfStrings):
    integer_map = map(int, ListOfStrings)
    ListOfIntegers = list(integer_map)
    return ListOfIntegers
