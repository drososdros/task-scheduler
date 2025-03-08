from datetime import datetime
from typing import Generator
from task import Task


class TaskNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next: TaskNode | None = None
        self.prev: TaskNode | None = None

    def __gt__(self, other):
        return self.data > other.data

    def __str__(self) -> str:
        return str(self.data)


class TaskQueue:
    def __init__(self) -> None:
        self.head: TaskNode | None = None
        self.tail: TaskNode | None = None
        self.length = 0

    def __len__(self) -> int:
        return self.length

    def __iter__(self) -> Generator[TaskNode]:
        node = self.head

        while node is not None:
            yield node
            node = node.next
            if node == self.head:
                break

    def __str__(self):
        node_list = []
        for i in self:
            node_list.append(str(i))
        return " -> ".join(node_list)

    def append_first(self, val) -> None:
        if len(self) == 0:
            self.append
        else:
            new_node = TaskNode(val)
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node
            self.length += 1

    def append(self, val):
        new_node = TaskNode(val)
        if len(self) == 0:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
            self.head.prev = self.tail
        self.length += 1

    def insert(self, val) -> None:
        new_node = TaskNode(val)
        if len(self) == 0:
            self.append(val)
        elif new_node > self.tail:
            self.append(val)
        elif new_node < self.head:
            self.append_first(val)
        else:
            node = self.head
            while node < new_node and node.next > node:
                node = node.next
            node = node.prev
            new_node.next = node.next
            new_node.prev = node
            node.next.prev = new_node
            node.next = new_node
            self.length += 1

    def pop_first(self):
        pass

    def pop_last(self):
        pass

    def pop_finished(self):
        pass


q = TaskQueue()

tas = Task()
tas.set_task("task 1", datetime(2025, 2, 1), "someMessage")
tas1 = Task()
tas1.set_task("task 2", datetime(2025, 2, 2), "someMessage2")

tas2 = Task()
tas2.set_task("task 3", datetime(2025, 2, 3), "someMessage3")

tas3 = Task()
tas3.set_task("task 3", datetime(2025, 2, 2, 11), "someMessage3")

tas4 = Task()
tas4.set_task("task 3", datetime(2025, 2, 1, 11), "someMessage3")

q.insert(tas1)
print(len(q))
q.insert(tas2)
print(len(q))
q.insert(tas)
print(len(q))
q.insert(tas3)
print(len(q))
q.insert(tas4)
print(len(q))
print(q)
for i in q:
    print(i.prev, "<-", i, "->", i.next)
