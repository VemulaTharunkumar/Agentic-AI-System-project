from tools.python_runner import run_python

class PythonExecutorAgent:
    def execute(self, file):
        return run_python(file)
