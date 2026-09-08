from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="sample.csv")

data = loadeer.load()

print(data[0])