tasks = [
    {
        {"id": 1},
        {"name", "to do homework"},
        {"dependency": 1},
        {"deadline": "16.11.2024"}
    },
    {
        {"id": 2},
        {"name", "to do algebra homework"},
        {"dependency": 1},
        {"deadline": "15.11.2024"}
    },
    {
        {"id": 3},
        {"name", "to do python homework"},
        {"dependency": 1},
        {"deadline": "14.11.2024"}
    }
]


def get_tasks_by_id(_id):
    for task in tasks:
        if task["id"] == _id:
            return task

def get_all_tasks():
    return tasks
