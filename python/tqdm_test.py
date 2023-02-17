#Progress bar
from tqdm import tqdm
from time import sleep
for i in tqdm(range(100)):
    sleep(1)

#En pandas hay mejores alternativas que los pickles, estan los parquet(mas liviano y lento) y los feather(mas pesado y rapido)
#Los dos parecen ser mejores que pickle