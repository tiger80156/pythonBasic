import collections 
import random
Student = collections.namedtuple('Student',('Grade','Score'))

class Students():
    def __init__(self, *args, **kwargs):
        self._student = []
        for i in range(50):
            self._student.append(Student(random.randint(1,12),random.randint(1,100)))

    def __len__:
        return len(self._student)
    
    def __getitem__(self,position):
        return self._student[position]
    
    def __setitem__(self, position,new):
        self._student[position] = new
        print(self._student[position])
    
    def __delitem__(self,position):
        self._student.pop[position]
        
    
        