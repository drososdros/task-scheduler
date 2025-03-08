"""
tasks:
X time
1 reapeted every X mins

2 reapeted in X time

3 reapeted in specific X repeatedly like every once month

4 reapeted once a month and for some days till matched finished

    if task pass and didnt run run it now
    if this happen maybe the computer will be shut off
"""

from datetime import datetime, timedelta


class Task:

    def __init__(self) -> None:
        """
        start_of_task is when the task run for the first time
        message is the message to print for start
        reapeted is how ofter the task is reapeded
        need validated is if the task need validation else it will run everyday
        validated mean that the task is validated
            and we wont need to run silmutaniously

        next_run the time till the next run
        """

        """Latter i provide support to run other exec files with the scheduler
        python files or other executables"""

        self.task_name = None
        self.start_of_task: datetime = None
        self.message: str = ""
        self.repeted: timedelta | bool = False
        self.need_validation: bool = False
        self.validated: bool = False
        self.next_run: int = 0
        self.succeeded: bool = False

    def __gt__(self, other):
        if isinstance(other, Task):
            return self.start_of_task > other.start_of_task
        return False

    def __str__(self) -> str:
        return str(self.start_of_task.strftime("%d/%m/%Y %H:%M:%S"))

    def set_task(self,
                 name: str,
                 start_of_task: datetime,
                 message: str,
                 repeated: timedelta | bool = False,
                 need_validation: bool = False,
                 validated: bool = False
                 ):

        self.task_name = name
        self.start_of_task = start_of_task
        self.message = message
        self.repeted = repeated
        self.need_validation = need_validation
        self.validated = validated

        self.next_run = int((datetime.now()-start_of_task).total_seconds())

    def task_create(self):
        task_name = input("Enter Task Name")
        start_of_task = input("Enter Start of Task in dd/mm/yy hh:mm:ss")
        message = input("enter message")
        start_time = datetime.strptime(start_of_task, "%d/%m/%Y %H:%M:%S")
        self.set_task(task_name, start_time, message)
