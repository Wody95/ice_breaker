import os
from dotenv import load_dotenv


if __name__ == "__main__":

    # 환경변수 로드
    load_dotenv()
    print("Hello, World!")
    # print(os.environ.get("OPENAI_API_KEY"))
    print(os.getenv("OPENAI_API_KEY"))
