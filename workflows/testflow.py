import base
import json
import sys

from taskflow import task
from taskflow.patterns import linear_flow
from taskflow import engines
from taskflow.types import notifier



class Task1(base.Taskflow):

    def execute(self):
        print("Executing task 1")
        print("Task 1 is going to return 1")
        return 1


class RunTestFlow(base.Runflow):

    def run(self, data):
        self.flow.add(Task1())
        self.process(data)


if __name__ == '__main__':
    data = sys.argv[1]
    tf = RunTestFlow()
    output = tf.run(json.loads(data))
    print("If i get None below .. its B A D")
    print output
