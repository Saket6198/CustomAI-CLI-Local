from dotenv import load_dotenv
import os

from langchain.chains.conversation.base import ConversationChain
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.memory import ConversationEntityMemory
from langchain.memory.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
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
    memory = ConversationEntityMemory(llm=llm)
    conversation = RunnableWithMessageHistory(
        get_session_history=lambda: memory.chat_memory,
        runnable=llm,
        verbose=True
    )
    while True:
        user_input = input("> ")

        # messages.append(HumanMessage(content=user_input))
        # ai_response = chat.invoke(messages)
        # print("\nAssistant:\n", ai_response)
        #
        # messages.append(AIMessage(content=ai_response.content))

        # Verbose output: Show the user's input
        print(f"\n[User Input]: {user_input}")

        # Verbose output: Show the current memory state before processing
        print(f"\n[Memory Before]: {memory.chat_memory.messages}")

        ai_response =   conversation.invoke(input=user_input)
        messages.append(AIMessage(content=ai_response.content))
        print(f'\nAssistant: \n{ai_response}')


if __name__ == "__main__":
    main()