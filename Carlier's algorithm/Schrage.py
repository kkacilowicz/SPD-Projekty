import heapq
import Task

def Schrage(NSet):
    # Tasks are sorted in ascending order (With ascending value of NsetTask obj.r)
    NSet.sort()

    # Variables initialized (t - actual moment in time, Cmax - Max time of delivery,
    t = 0
    Cmax = 0

    # It's a list of tasks ready to be executed
    # It stores GsetTask objects which are sorted in descending order (With descending value of obj.q)
    GSet = []

    # It's a list of tasks which represents the order of execution
    Harmonogram = []

    # While lists are not empty


    while len(NSet) != 0 or len(GSet) != 0:
        # While smallest time of accessibility is smaller than actual moment in time (and Nset is not empty)
        while len(NSet) != 0 and min(NSet).r <= t:
            # Task with smallest r is removed from NSet and added to variable e
            # heapq library makes a list behave like a heap, where Nset is a min-heap, Gset is a max-heap
            e = heapq.heappop(NSet)
            # e is appended to list, from now on NsetTask became GsetTask
            GSet.append(Task.GsetTask(e))
            # Apparently you always have to heapify (make heap out of list) when you have populated list
            # Otherwise algorithm doesn't work
            heapq._heapify_max(GSet)

        # In a situation where Gset is empty, t = smallest r in Nset
        if len(GSet) == 0:
            t = min(NSet).r
        else:
            # e = GsetTask with highest q
            e = heapq._heappop_max(GSet)
            # Saving order of execution
            Harmonogram.append(e)
            # Actual moment in time = Previous moment in time + time of execution of this task
            t = t + e.p
            # Max time of delivery = Hiqhest of old Cmax vs actual time + time of delivery
            e.C = t
            Cmax = max(Cmax, t + e.q)
            #print(Harmonogram.index(e))
    return Harmonogram, Cmax




