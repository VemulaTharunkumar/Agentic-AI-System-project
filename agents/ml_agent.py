from tools.ml_trainer import train_model

class MLAgent:
    def run(self, dataset):
        acc = train_model(dataset)
        return f"ML Accuracy: {acc * 100:.2f}%"
