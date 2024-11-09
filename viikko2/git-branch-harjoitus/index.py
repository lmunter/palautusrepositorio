from logger import logger
from summa import summa
from erotus import erotus
from tulo import tulo

logger("aloitetaan ohjelma")

x = int(input("Luku 1: "))
y = int(input("Luku 2: "))
print(f"{x} + {y} = {summa(x, y)}")
print(f"{x} - {y} = {erotus(x, y)}")
print(f"{x} * {y} = {tulo(x, y)}")

logger("lopetetaan")
print("goodbye!")
