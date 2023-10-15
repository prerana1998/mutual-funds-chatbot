# mutual-funds-chatbot
This is a chatbot answering queries about mutual funds
The code has two parts
  1. Uploading custom documents and creating embeddings using Pinecone. For more information on Pinecone visit https://www.pinecone.io/
  2. Using openAI's gpt-3.5 turbo to generate answers for the queries
Please look at the data section to get the documents that are used in generating the response,
[app.py](https://github.com/prerana1998/mutual-funds-chatbot/blob/main/app.py) contains the inference part of generating response to the user queries
[upload_docs.py](https://github.com/prerana1998/mutual-funds-chatbot/blob/main/upload_docs.py) contains code for generating embeddings and storing in the vectordatabase
![Architecture](https://github.com/prerana1998/mutual-funds-chatbot/blob/main/Architecture.png)
Sample images of the chatbot
![Chatbot](https://github.com/prerana1998/mutual-funds-chatbot/blob/main/chatbot.JPG)
