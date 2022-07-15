from typing import List, Optional


def find_next_best_task(tasks: List[str], prev_prev_task: str, prev_task:str, current_task: str, current_index: int, completed_tasks: set) -> Optional[int]:
    print(f" Trying to find better search from array: {tasks}")
    for task_index, task in enumerate(tasks):
        if task != current_task and (task_index + current_index) not in completed_tasks and task != prev_task and task != prev_prev_task:
            print(f" Found better task: {task}, task index: {task_index + current_index}")
            return task_index + current_index
    print(" No better task found")
    return None

def least_interval(tasks: List[str], n: int) -> int:
    # completed_tasks = set()
    completed_tasks = []

    task_index = 0
    n_tasks = len(tasks)
    prev_prev_task = None
    prev_task = None
    time_required = 0
    remaining_idle_time = 0
    checked_tasks = set()

    while task_index < n_tasks:
        print(f"\n--- Task index: {task_index} ---")
        if task_index not in completed_tasks:
            task = tasks[task_index]
            if task in (prev_task, prev_prev_task) or remaining_idle_time > 0:
                if task_index not in checked_tasks:
                    checked_tasks.add(task_index)
                    cooldown_time = n - (1 if task == prev_prev_task else 0)

                    # time_required += cooldown_time  # add the cool down time if doing same task again
                    remaining_idle_time = cooldown_time
                    print(f"Remaining idle time: {remaining_idle_time}")

                print(f"task: {task}({task_index}) in {(prev_prev_task, prev_task)}")
                better_task_index = find_next_best_task(tasks[task_index+1:], prev_prev_task, prev_task, task, task_index+1, completed_tasks)
                if better_task_index and better_task_index not in completed_tasks:
                    completed_tasks.append(better_task_index)
                    print(f"Task {tasks[better_task_index]} is completed. Prev task was {prev_task} (by better search)")
                    prev_prev_task = prev_task
                    prev_task = tasks[better_task_index]
                    if n == 0:
                        time_required += 1
                    else:
                        remaining_idle_time -= 1
                        time_required += 1
                        print(f"Remaining idle time: {remaining_idle_time}")
                    print([tasks[x] for x in completed_tasks])

                    continue
                # if remaining_idle_time > 0:
                #     remaining_idle_time -= 1
                # print("------ idle -------")

            completed_tasks.append(task_index)
            print(f"Task {task} is completed. Prev task was {prev_task}")
            prev_prev_task = prev_task
            prev_task = task
            # print(task, end=" -> ")
            print(f"Remaining idle time: {remaining_idle_time}")
            time_required += 1 + remaining_idle_time  # add the time required to do the current task
            task_index += 1  # increment the task index
            remaining_idle_time = 0
        else:
            print(f"Skipped {task_index=} ({tasks[task_index]}) as already completed")
            task_index += 1  # skip if task already completed
            remaining_idle_time = 0

        print([tasks[x] for x in completed_tasks])

    return time_required

if __name__ == '__main__':
    _tasks = ["A","A","A","B","B","B"]
    # _tasks = ["A", "B", "A"]
    # _tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
    _time_requred = least_interval(_tasks, 2)
    print()
    print("Tot. Time required:", _time_requred)
