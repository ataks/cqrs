import pytest
from src.domain.entity.entity import Task
from src.domain.entity.user import User


@pytest.fixture
def valid_create_user_dict():
    create_user = dict([('id', '1'),
                        ('name', 'Taro')])
    return create_user


@pytest.fixture
def valid_own_user_dict():
    own_user_dict = dict([('id', '2'),
                     ('name', 'Jiro')])
    return own_user_dict


def test_user_entity_object():

    create_user = User(1, "Taro")
    own_user = User(2, "Jiro")

    assert create_user.id == 1
    assert create_user.name == "Taro"
    assert own_user.id == 2
    assert own_user.name == "Jiro"


def test_own_user_valid_dict(valid_own_user_dict):

    own_user = User.from_dict(valid_own_user_dict)

    assert own_user.id == "2"
    assert own_user.name == "Jiro"


def test_create_task():

    create_user = User(1, "Taro")
    own_user = User(2, "Jiro")
    task = Task(create_user, own_user, "cqrs_learning")

    assert isinstance(task, Task)
    assert task.name == "cqrs_learning"


def test_task_status():
    pass
#    assert task.task_status = DONE

# def test_task_done():
#
#     task = Task.create_task()

