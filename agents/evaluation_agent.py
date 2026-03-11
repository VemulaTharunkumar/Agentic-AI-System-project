class EvaluationAgent:
    def judge(self, accuracy):
        if accuracy > 0.90:
            return "Excellent model performance"
        elif accuracy > 0.80:
            return "Good performance — can optimize"
        else:
            return "Low accuracy — retraining needed"
