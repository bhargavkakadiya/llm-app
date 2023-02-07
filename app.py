from langchain.llms import OpenAI

from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)

llm = OpenAI(temperature=0.9)

print(llm(prompt.format(product="colorful socks")))
