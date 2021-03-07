class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name):
        try:
            is_in = [t for t in self.tasks if t.name == task_name][0]
            is_in.completed = True
            return f"Completed task {task_name}"
        except IndexError:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        clean_task_list = [t for t in self.tasks if t.completed != True]
        num_removed = len(self.tasks) - len(clean_task_list)
        self.tasks = clean_task_list
        return f"Cleared {num_removed} tasks."

    def view_section(self):
        res = f"Section {self.name}:\n"
        for each in self.tasks:
            res += f"{each.details()}\n"
        return res
