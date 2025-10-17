from core.application.services.todo_service import TodoService


def get_todo_service():
    return TodoService(text="get_todo_service_dependency")
