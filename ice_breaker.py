import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

if __name__ == "__main__":

    # 환경변수 로드
    load_dotenv()
    print("Hello, World!")
    # print(os.environ.get("OPENAI_API_KEY"))
    print(os.getenv("OPENAI_API_KEY"))
