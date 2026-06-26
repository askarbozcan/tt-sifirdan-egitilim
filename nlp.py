from transformers import AutoTokenizer, AutoModel
from pprint import pprint

tokenizer = AutoTokenizer.from_pretrained("dbmdz/bert-base-turkish-cased")
model = AutoModel.from_pretrained("dbmdz/bert-base-turkish-cased")
model.eval()
