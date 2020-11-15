
import itertools
import random

class Persons:

    id_iter = itertools.count()

    def __init__(self):
        self.id = next(self.id_iter)
        self.workload = self.workload

    def assign_workload(self):
        self.workload = random.randint(1, 20)
