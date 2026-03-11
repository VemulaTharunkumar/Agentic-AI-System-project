from tools.java_runner import run_java

class JavaExecutorAgent:
    def execute(self, file):
        return run_java(file)
