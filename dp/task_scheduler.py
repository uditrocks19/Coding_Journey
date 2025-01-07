import heapq

class TaskManager:
    def __init__(self, tasks: list[list[int]]):
        self.task_map = {}  # Maps taskId to (userId, priority)
        self.priority_queue = []  # Min-heap storing (-priority, -taskId, userId)
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        # Add task to task_map
        self.task_map[taskId] = (userId, priority)
        # Add task to the priority queue with negative priority and taskId
        heapq.heappush(self.priority_queue, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        # Remove the old task and add a new one with updated priority
        userId, _ = self.task_map[taskId]
        self.priority_queue = [item for item in self.priority_queue if item[1] != taskId]
        self.priority_queue = heapq.heapify(self.priority_queue)
        self.task_map[taskId] = (userId, newPriority)
        # Push updated task to priority queue
        heapq.heappush(self.priority_queue, (-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        # Remove task from task_map
        if taskId in self.task_map:
            del self.task_map[taskId]

    def execTop(self) -> int:
        # Process heap until a valid task is found
        while self.priority_queue:
            neg_priority, neg_taskId, userId = heapq.heappop(self.priority_queue)
            taskId = -neg_taskId
            if taskId in self.task_map:
                # Remove the executed task from task_map
                del self.task_map[taskId]
                return userId
        return -1  # No tasks available

# Test Case
taskManager = TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]])
taskManager.add(4, 104, 5)
taskManager.edit(102, 8)
print(taskManager.execTop())  # Output: 3
taskManager.rmv(101)
taskManager.add(5, 105, 15)
print(taskManager.execTop())  # Output: 5
