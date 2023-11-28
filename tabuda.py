from msilib.schema import tables
import tabnanny
from turtle import TNavigator
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap

tab= int(input("informe um numero"))
indice = 1
while indice <11:
    Resultado = tab * indice
    print(tab, "x", indice, "=", Resultado)
    indice= indice + 1