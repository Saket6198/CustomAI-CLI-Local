from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    print(os.getenv("API_KEY"))

if __name__ == "__main__":
    main()