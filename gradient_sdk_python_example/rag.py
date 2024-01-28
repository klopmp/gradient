from typing import List, Mapping

from dotenv import load_dotenv

load_dotenv()
from gradientai import (
    AnalyzeSentimentParamsExample,
    ExtractParamsSchemaValue,
    ExtractParamsSchemaValueType,
    Gradient,
    Sentiment,
    SummarizeParamsExample,
    SummarizeParamsLength,
)


def run_answer_example(*, gradient: Gradient) -> None:
    print("==== Q & A ====")
    #print(f"Document: {document}\n")
    question = "How manu invoices are there? Only return the number and nothing else."

    print(f"• Question: {question}\n")
    #print("Answering question...")
    result = gradient.answer(
        question=question,
        source={
            "type": "rag",
            "collectionId": ""
        },
    )
    print(f"• Answer: {result['answer']}")
    print("\n")
    print("================\n")
    print("\n")

    question = "Output Invoice ID and Amounts as columns in a table. Exclude invoice without an Invoice ID."

    print(f"• Question: {question}\n")
    result = gradient.answer(
        question=question,
        source={
            "type": "rag",
            "collectionId": "76f2bc82-5e96-4661-879b-338e29f1b6ee_rag_config"
        },
    )
    print(f"• Answer: {result['answer']}")

    print("================\n")

def main() -> None:
    gradient = Gradient()

    run_answer_example(gradient=gradient)
    gradient.close()


if __name__ == "__main__":
    main()
