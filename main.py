from orchestrator.orchestrator_controller import Orchestrator

def start():
    print("\n🚀 Agentic AI System Started")

    system = Orchestrator()

    while True:
        goal = input("\nEnter your task (or type 'exit'): ")
        if goal.lower() == "exit":
            break

        system.run(goal)

if __name__ == "__main__":
    start()
