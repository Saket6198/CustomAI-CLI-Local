from dotenv import load_dotenv
import os
from langchain_core.runnables.history import RunnableWithMessageHistory
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
    memory = ConversationBufferMemory()
    def get_message():
        return memory.chat_memory
    print("Hello, I am Your personal Assistant!")
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
    conversation = RunnableWithMessageHistory(
        get_session_history=get_message,
        runnable=llm
    )
    while True:
        user_input = input("> ")

        # messages.append(HumanMessage(content=user_input))
        # ai_response = chat.invoke(messages)
        # print("\nAssistant:\n", ai_response)
        #
        # messages.append(AIMessage(content=ai_response.content))
        ai_response =   conversation.invoke(input=user_input)
        messages.append(AIMessage(content=ai_response.content))
        print(f'\nAssistant: \n{ai_response}')


if __name__ == "__main__":
    main()