from dotenv import load_dotenv
import os

from langchain.chains.conversation.base import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage,

)


def main():
    load_dotenv()
    # print(os.getenv("GOOGLE_API_KEY"))

    chat = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

    messages = [
        SystemMessage(content="You are  a helpful assistant"),
    ]
    print("Hello, I am Your personal Assistant!")
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
    conversation = ConversationChain(
        llm=llm,
        memory=ConversationBufferMemory(),
        verbose=True
    )
    while True:
        user_input = input("> ")

        # messages.append(HumanMessage(content=user_input))
        # ai_response = chat.invoke(messages)
        # print("\nAssistant:\n", ai_response)
        #
        # messages.append(AIMessage(content=ai_response.content))
        ai_response = conversation.predict(input=user_input)
        messages.append(AIMessage(content=ai_reponse))
        print(f'\nAssistant: \n{ai_response}')


if __name__ == "__main__":
    main()