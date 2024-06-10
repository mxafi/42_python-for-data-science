from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

# Expected output:
# $> python tester.py
# 100%|[==================================>]| 333/333
# 100%|                                     | 333/333 [00:01<00:00, 191.61it/s]

for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()
for elem in tqdm(range(333)):
    sleep(0.005)
print()
