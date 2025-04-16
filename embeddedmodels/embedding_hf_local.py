from langchain_huggingface import HuggingFaceEmbeddings

embedding  = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

text = "bengaluru weather is so good"

vector = embedding.embed_query(text)

print(str(vector))

