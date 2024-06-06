
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig
import torch
torch.manual_seed(1234)

from multiprocessing import Pool
import os, json
from tqdm import tqdm

tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-Audio-Chat", trust_remote_code=True)

model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-Audio-Chat", device_map="cuda", trust_remote_code=True, fp16=True).eval()

f = open('../mloops/val_metadata.json')
data = json.load(f)

cats = []

for d in tqdm(data):
    # print(d)
    cat = d['info']['Category']
    query = tokenizer.from_list_format([
        {'audio': '../mloops/' + d['files'][0]['path']}, # Either a local path or an url
        {'text': 'What instruments are in this piece?'},
    ])
    response, history = model.chat(tokenizer, query=query, history=None)
    # print(cat, response)
    cats.append((cat, response))

with open('./cats.json', 'w', encoding='utf-8') as f:
    json.dump(cats, f, ensure_ascii=False, indent=4)


