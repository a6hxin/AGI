from agents.planner import plan_task
from agents.executor import execute_step
from agents.critic import critique
from memory.vector_store import store_memory, retrieve_memory

def run_agent(task):

    print("TASK:", task)

    memory = retrieve_memory(task)

    if memory:
        print("Relevant memory:", memory)

    plan = plan_task(task)

    print("PLAN:", plan)

    result = execute_step(plan)

    print("EXECUTION:", result)

    improved = critique(str(result))

    store_memory(improved)

    return improved


if __name__ == "__main__":

    task = input("Enter task: ")

    output = run_agent(task)

    print("\nFINAL OUTPUT:")
    print(output)
    store_memory("Paris is the capital of France")
store_memory("Mumbai is in India")

result = retrieve_memory("What is the capital of France?")
print(result)