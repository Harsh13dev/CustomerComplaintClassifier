from langchain.chat_models.base import init_chat_model   
# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableBranch, RunnableLambda, RunnableSequence, RunnablePassthrough
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
import streamlit as st

load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")


st.set_page_config("Customer Email Analyser")
st.title("Customer Email Analyser and Response Generator")

# llm1 = HuggingFaceEndpoint(
#     repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
#     # task="text-generation"
# )

# model = ChatHuggingFace(llm=llm1)
model = init_chat_model("groq:llama-3.1-8b-instant")


parser = StrOutputParser()

class classify_email(BaseModel):
    email_type: Literal['complaint','refund','feedback'] = Field(description="Give the type of the email it belongs to")

parser2 = PydanticOutputParser(pydantic_object=classify_email)


prompt1 = PromptTemplate(
    template="Classify the type of the following emali from customer into complaint, refund or feedback \n {email} \n {format_instruction}",
    input_variables=['email'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2


def refund(email):
    return "Your refund request has been initiated, It will take 2-3 working days to process and refund"

prompt2 = PromptTemplate(
    template='Write an short and appropriate response from company to this customer email for complaint \n {email}',
    input_variables=['email']
)

prompt3 = PromptTemplate(
    template='Write an short and appropriate response from company to this customer email feedback \n {email}',
    input_variables=['email']
)


branch_chain = RunnableBranch(
    (lambda x: x.email_type == 'complaint', RunnableSequence(prompt2, model, parser)),
    (lambda x: x.email_type == 'refund', RunnableLambda(refund)),
    (lambda x: x.email_type == 'feedback', RunnableSequence(prompt3, model, parser)),
    RunnablePassthrough()
)

chain = classifier_chain | branch_chain

# response = chain.invoke({'email':'Thank you for the product its good product'})
# response = chain.invoke({'email':'This is the terriable smartphone'})
# response = chain.invoke({'email':'Whats the status of my refund'})


with st.form('my_form'):
  email = st.text_area('Enter email:')
  submitted = st.form_submit_button('Submit')
  if submitted:
    result = chain.invoke({
        'email':email
    })

    st.header("Response for email:")
    st.write(result)