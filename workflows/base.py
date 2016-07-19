import abc
import six


from taskflow.types import notifier
from taskflow import task
from taskflow.patterns import linear_flow
from taskflow import engines


ANY = notifier.Notifier.ANY


def task_watch(state, details):
    print('Task details : ', details)
    print('Task %s => %s' % (details.get('task_name'), state))


def flow_watch(state, details):
    print('Flow => %s' % state)


@six.add_metaclass(abc.ABCMeta)
class Taskflow(task.Task):
    """Task Flow base class. Needs execute() method
    defined."""


@six.add_metaclass(abc.ABCMeta)
class Runflow(object):

    def __init__(self):
        self.flow = linear_flow.Flow('TestFlow')

    @abc.abstractmethod
    def run(self):
        """Run runs the task."""

    def process(self, data=None):
        """Process this plugin."""
        if data:
            print("Data is: ", data)


        print("Starting task")
        #f = linear_flow.Flow('TestFlow')
        #f.add(Task1(name='task-1'))

        e = engines.load(self.flow, executor='processes', engine='parallel',
                         max_worker=1)
        e.notifier.register(ANY, flow_watch)
        e.notifier.register(ANY, task_watch)
        e.run()
        return e.statistics
