from typing import List

from dotenv import load_dotenv

load_dotenv()
from gradientai import Gradient, Sample


def main() -> None:
    gradient = Gradient()

    base_model = gradient.get_base_model(base_model_slug="llama2-7b-chat")

    new_model_adapter = base_model.create_model_adapter(
        name="my test model adapter",
    )
    print(f"Created model adapter with id {new_model_adapter.id}")

    test_samples: List[Sample] = [
        
        {
            "inputs": "### Instruction: What are ZenBiz specialities? \n\n### Response: ZenBiz specializes in account payables, account receivables, and international taxation."
        },
    ]
    new_model_adapter.fine_tune(samples=test_samples)

    sample_query = (
        "### Instruction: What does ZenBiz do?\n\n##Response:"
    )
    print(f"Asking: {sample_query}")

    complete_response = new_model_adapter.complete(
        query=sample_query,
        max_generated_token_count=100,
    )
    print(f"Generated: {complete_response.generated_output}")

    new_model_adapter.delete()
    gradient.close()


if __name__ == "__main__":
    main()
