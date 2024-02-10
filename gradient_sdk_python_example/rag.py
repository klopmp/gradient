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
    question = "How manu invoices are there total? Only return the number and nothing else."

    print(f"• Question: {question}\n")
    #print("Answering question...")
    result = gradient.answer(
        question=question,
        source={
            "type": "rag",
            "collectionId": "632675d7-5e7e-4cb1-a80f-131218cfbfd9_rag_config"
        },
    )
    print(f"• Answer: {result['answer']}")
    

    question = "Output Invoice ID, Company Name and Amounts as columns in a table. Report any parsing error."

    print("\n")
    print("==== Q & A ====")

    print(f"• Question: {question}\n")
    result = gradient.answer(
        question=question,
        source={
            "type": "rag",
            "collectionId": "95fb08f3-d668-43f3-a316-78c2021f2a63_rag_config"
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
