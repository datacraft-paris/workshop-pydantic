from workshop_pydantic.structured_output.club import Club
import openai
import json
from dotenv import load_dotenv


def main():
    load_dotenv()
    client = openai.OpenAI()
    result = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that generates club information.",
            },
            {
                "role": "user",
                "content": ...,
            },
        ],
        response_format=...,
    )
    result_dict = json.loads(result.choices[0].message.content)
    with open("club.json", "w") as f:
        json.dump(result_dict, f, indent=2)


if __name__ == "__main__":
    main()
