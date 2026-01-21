import adk
import adk.evaluation
import os
import asyncio # Often needed for ADK evaluation, especially if tools are async

# --- IMPORT YOUR ROOT AGENT ---
# Assuming 'my_agent_definition.py' is in the same 'ecommerce_app' directory
# as this 'evalagent.py' file.
from ecommerce_app.agent import root_agent
# ------------------------------

# Define evaluation questions and expected answers
# Replace with your actual evaluation data

# Load test cases from a JSONL file
with open("evaluate_dataset.json", "r") as f:
    test_cases_data = [json.loads(line) for line in f]

EVAL_QUESTIONS = [adk.evaluation.TestCase(**data) for data in test_cases_data]




def run_eval():
    print("Starting agent evaluation...")

    # Initialize the Evaluator
    evaluator = adk.evaluation.Evaluator(
        agent=root_agent,  # The agent to evaluate
        test_cases=EVAL_QUESTIONS,
        # Use the same model as your agent for evaluation if you want consistent responses,
        # or a different one for comparison/refinement.
        model=root_agent.model,
        # Other optional parameters:
        project_id=os.environ.get("GOOGLE_CLOUD_PROJECT"), # Replace with your project ID if not in env
        # trace_path="path/to/evaluation_traces", # Optional: directory to save evaluation traces
        # evaluation_name="ecommerce-agent-q1-eval" # Optional: name for this evaluation run
    )

    # Run the evaluation asynchronously
    # Use asyncio.run() to execute the async method
    evaluation_results = asyncio.run(evaluator.run())

    # Print a summary of the evaluation results
    print("\n--- Evaluation Summary ---")
    evaluation_results.print_summary()

    # You can also access detailed results:
    # for result in evaluation_results.test_case_results:
    #     print(f"Question: {result.test_case.question}")
    #     print(f"Agent Answer: {result.agent_response.answer}")
    #     print(f"Evaluation Score: {result.score}")
    #     print(f"Evaluation Reason: {result.reasoning}")
    #     print("-" * 30)

    print("Evaluation finished.")


if __name__ == '__main__':
    # Ensure your Google Cloud authentication is set up (e.g., via `gcloud auth application-default login`)
    # and any necessary environment variables are configured.
    run_eval()
