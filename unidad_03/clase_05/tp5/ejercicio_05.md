 Dado el siguiente Arbol:
         40
       /    \
     28      70
    /  \    /  \
   9   32  52  10

## Indique el resultado del recorrido post-orden 
9 32 28 52 10 70 40

## Indique el resultado del recorrido pre-orden
40 28 9 32 70 52 10

## Elabore un algoritmo para el recorrido in-orden que permita imprimir los números pares

```python
def in_order_pares(nodo):
    if nodo is not None:
        in_order_pares(nodo.izq)
        if nodo.valor % 2 == 0:
            print(nodo.valor)
        in_order_pares(nodo.der)
```