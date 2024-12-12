from transformers import pipeline

class Generator:
    """
    텍스트 생성을 담당하는 클래스입니다.
    GPT-2 모델을 사용하여 주어진 프롬프트에 이어지는 텍스트를 생성합니다.
    """
    def __init__(self):
        """
        Generator 클래스의 생성자
        transformers 라이브러리의 pipeline을 사용하여 GPT-2 모델을 초기화합니다.
        """
        self.generator = pipeline("text-generation", model="gpt2")

    def generate(self, prompt):
        """
        주어진 프롬프트를 기반으로 텍스트를 생성합니다.

        매개변수:
            prompt (str): 텍스트 생성의 시작점이 되는 입력 문자열

        반환값:
            str: 생성된 텍스트 (입력 프롬프트를 제외한 새로 생성된 부분만 반환)

        설정:
            max_length: 생성될 전체 텍스트의 최대 길이 (기본값: 50)
            num_return_sequences: 생성할 텍스트의 수 (기본값: 1)
        """
        response = self.generator(prompt, max_length=50, num_return_sequences=1)
        return response[0]['generated_text'][len(prompt):]

# # 사용 예시
# generator = Generator()
# print(generator.generate("Have a good"))