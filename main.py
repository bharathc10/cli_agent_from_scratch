import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function
from config import MAX_ITERS

def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError("api_key is not defined")

    client = genai.Client(api_key=api_key)

    for _ in range(MAX_ITERS):
        response = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=system_prompt)
        )

        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)

        if response.usage_metadata is None:
            raise RuntimeError("usage_metadata is None")

        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
            
        if not response.function_calls:
            # no tools, just text
            print("Response:")
            print(response.text)
            return

        # otherwise: handle function calls
        function_responses = []
        for function_call in response.function_calls:
            result = call_function(function_call, args.verbose)

            if (
                not result.parts
                or not result.parts[0].function_response
                or not result.parts[0].function_response.response
            ):
                raise RuntimeError(f"Empty function response for {function_call.name}")

            if args.verbose:
                print(f"-> {result.parts[0].function_response.response}")

            function_responses.append(result.parts[0])

        messages.append(types.Content(role="user", parts=function_responses))
    
    print("Agent stopped after 20 iterations without a final response.")

if __name__ == "__main__":
    main()
