class Trainer:
    trainer_id = 0

    def __init__(self, name):
        Trainer.trainer_id += 1
        self.name = name
        self.id = Trainer.trainer_id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Trainer.trainer_id + 1
