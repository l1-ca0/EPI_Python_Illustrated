import collections

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))

def optimum_task_assignment(task_durations):
    """
    Finds an optimum assignment of tasks to workers to minimize the maximum time
    any worker spends on their assigned tasks

    The greedy strategy is to pair the task with the longest duration with the
    task with the shortest duration, the second-longest with the second-shortest,
    and so on

    Args:
        task_durations: A list of integers representing the duration of each task

    Returns:
        A list of PairedTasks tuples, where each tuple represents the two tasks
        assigned to a single worker
    """
    # Sort the tasks by duration in non-decreasing (ascending) order
    # The overall time complexity is dominated by this O(n log n) sort operation
    task_durations.sort()

    # Create pairs by matching the shortest tasks with the longest tasks
    # We iterate through the first half of the sorted list
    # For each index `i` from the beginning, we pair it with index `~i` from the end
    # `~i` is the bitwise NOT operator, which is equivalent to `-i - 1`
    # This effectively pairs task_durations[0] with task_durations[-1],
    # task_durations[1] with task_durations[-2], and so on
    return [
        PairedTasks(task_durations[i], task_durations[~i])
        for i in range(len(task_durations) // 2)
    ]


