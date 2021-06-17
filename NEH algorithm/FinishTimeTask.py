# Class which contains info about each task
class FinishTimeTask:
    # Constructor of class
    def __init__(self, TimesOfFinish):
        # TimesOfExecution - list of times of execution on each machine
        # SumOfTimes - sum of times of execution on each machine
        self.TimesOfFinish = MapStringToInt(TimesOfFinish)
        self.SumOfTimes = SumOfTimes(self)


def SumOfTimes(Task):
    sum = 0
    for Time in Task.TimesOfFinish:
        sum += Time
    return sum


def MapStringToInt(ListOfStrings):
    integer_map = map(int, ListOfStrings)
    ListOfIntegers = list(integer_map)
    return ListOfIntegers
