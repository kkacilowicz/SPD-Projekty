import Task
import heapq



def SchrageWithDistributuion(NSet):
    # Tasks are sorted in ascending order (With ascending value of NsetTask obj.r)
    NSet.sort()

    # Variables initialized (t - actual moment in time, Cmax - Max time of delivery,
    t = 0
    Cmax = 0

    # It's a list of tasks ready to be executed
    # It stores GsetTask objects which are sorted in descending order (With descending value of obj.q)
    GSet = []

    # l is an actual processed task (q is very big so as not to mess with first execution of a loop)
    l = Task.Task(0, 0, 10000000000, 0)
    k = 0
    # While lists are not empty
    while len(NSet) != 0 or len(GSet) != 0:
        # While smallest time of accessibility is smaller than actual moment in time (and Nset is not empty)
        while len(NSet) != 0 and min(NSet).r <= t:
            # Task with smallest r is removed from NSet and added to variable e
            # heapq library makes a list behave like a heap, where Nset is a min-heap, Gset is a max-heap
            e = heapq.heappop(NSet)
            # e is appended to list, from now on NsetTask became GsetTask
            GSet.append(Task.GsetTask(e))

            # If time of delivery of considered task is higher than the one of actual task
            if e.q > l.q:
                # Stop executing l task
                l.p = t - e.r
                t = e.r
                if l.p > 0:
                    # Add task with time left to be executed
                    GSet.append(Task.GsetTask(l))
            # Apparently you always have to heapify (make heap out of list) when you have populated list
            # Otherwise algorithm doesn't work
            heapq._heapify_max(GSet)

        # In a situation where Gset is empty, t = smallest r in Nset
        if len(GSet) == 0:
            t = min(NSet).r
        else:
            # e = GsetTask with highest q
            e = heapq._heappop_max(GSet)
            # Actual task is now e
            l = e
            # Actual moment in time = Previous moment in time + time of execution of this task
            t = t + e.p
            e.C = t
            # Max time of delivery = Hiqhest of old Cmax vs actual time + time of delivery
            Cmax = max(Cmax, t + e.q)
    return Cmax


