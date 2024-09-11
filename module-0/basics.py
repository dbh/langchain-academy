
import os, getpass

from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .envxw


# [Here](https://python.langchain.com/v0.2/docs/how_to/#chat-models) is a useful how-do for all the things that you can do with chat models, but we'll show a few highlights below. If you've run `pip install -r requirements.txt` as noted in the README, then you've installed the `langchain-openai` package. With this, we can instantiate our `ChatOpenAI` model object. If you are signing up for the API for the first time, you should receive [free credits](https://community.openai.com/t/understanding-api-limits-and-free-tier/498517) that can be applied to any of the models. You can see pricing for various models [here](https://openai.com/api/pricing/). The notebooks will default to `gpt-4o` because it's a good balance of quality, price, and speed [see more here](https://help.openai.com/en/articles/7102672-how-can-i-access-gpt-4-gpt-4-turbo-gpt-4o-and-gpt-4o-mini), but you can also opt for the lower priced `gpt-3.5` series models. 
# 
# There are [a few standard parameters](https://python.langchain.com/v0.2/docs/concepts/#chat-models) that we can set with chat models. Two of the most common are:
# 
# * `model`: the name of the model
# * `temperature`: the sampling temperature
# 
# `Temperature` controls the randomness or creativity of the model's output where low temperature (close to 0) is more deterministic and focused outputs. This is good for tasks requiring accuracy or factual responses. High temperature (close to 1) is good for creative tasks or generating varied responses. 


# gpt4o_chat = ChatOpenAI(model="gpt-4o", temperature=0)
gpt35_chat = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)


# Chat models in LangChain have a number of [default methods](https://python.langchain.com/v0.2/docs/concepts/#runnable-interface). For the most part, we'll be using:
# 
# * `stream`: stream back chunks of the response
# * `invoke`: call the chain on an input
# 
# And, as mentioned, chat models take [messages](https://python.langchain.com/v0.2/docs/concepts/#messages) as input. Messages have a role (that describes who is saying the message) and a content property. We'll be talking a lot more about this later, but here let's just show the basics.

openAiKey = os.getenv("OPENAI_API_KEY")

from langchain_core.messages import HumanMessage

# Create a message
msg = HumanMessage(content="Hello world", name="Lance")

# Message list
messages = [msg]
print(messages)
# gpt4o_chat.invoke(messages)
# gpt4o_chat.invoke("hello world")


gpt35_chat.invoke(messages)
hello_world = gpt35_chat.invoke("hello world")
print(hello_world)

# ## Search Tools
# 
# You'll also see [Tavily](https://tavily.com/) in the README, which is a search engine optimized for LLMs and RAG, aimed at efficient, quick, and persistent search results. As mentioned, it's easy to sign up and offers a generous free tier. Some lessons (in Module 4) will use Tavily by default but, of course, other search tools can be used if you want to modify the code for yourself.
from langchain_community.tools.tavily_search import TavilySearchResults
tavily_search = TavilySearchResults(max_results=3)
search_docs = tavily_search.invoke("What is LangGraph?")

search_docs


