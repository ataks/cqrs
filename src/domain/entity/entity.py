from enum import Enum


class Task:

    # コンストラクタとメソッドでドメインの制約（仕様）を表現
    # ポイント：
    # ①entityが保持する値をuserにすることで型安全にする
    # ②必ず”未完了”の状態でインスタンス生成、という制約をコンストラクタで表現
    # ③nameは更新しないことにより「名前を変更できない」という制約を表現

    def __init__(self, create_user, own_user, name):
        self.create_user = create_user
        self.own_user = own_user
        self.name = name
        self.task_status = self.Task_Status.UNDONE

    def undone(self):
        self.task_status = self.Task_Status.UNDONE

    def done(self):
        self.task_status = self.Task_Status.DONE


    # @classmethod
    # def create_task(cls):
    #     return Task()

    class Task_Status(Enum):
        UNDONE = 1
        DONE = 2



