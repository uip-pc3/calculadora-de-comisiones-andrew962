# calculadora-comisiones-base
Este repositorio contiene información sobre la asignación de la calculadora de
comisiones.

## Descripción del Problema
La empresa ABC está interesada en una calculadora de comisiones.
La calculadora de comisiones es una plataforma web que calcula cuánto dinero
le corresponde a un vendedor dada las ventas mensuales.

ABC ha definido algunas reglas que indican cómo se distribuye la comisión:
* Para ventas que superan los $100,000, el vendedor recibe una comisión del 15%
de su total de ventas mensual

* Para ventas que superan los $75,000, el vendedor recibe una comisión del
10% de su total de ventas mensual.
* Para ventas que superan los $50,000, el vendedor recibe una comisión del
7% de su total de ventas mensual.
* Para ventas que superan los $25,000, el vendedor recibe una comisión del
5% de su total de ventas mensual.
* Para el resto de ventas, el vendedor recibe una comisión del 3% de su total
de ventas mensual.
* En caso tal no se haya dado ventas en el mes, entonces el vendedor recibe
un llamado de atención.

La plataforma web debe validar las entradas antes de procesar la solicitud,
debe mostrar la salida a través de una nueva página y guardar este resultado en un fichero CSV dentro del servidor que siga el patrón "apellido,nombre,ventas,comision" (ejemplo: Martinez,Carlos,200000,30000).

No es necesario realizar pruebas unitarias, ni documentar. Igualmente,
si lo hace, tendrá puntos adicionales.

## Licencia
El código de este repositorio está bajo la licencia MIT (ver archivo LICENSE) y
la documentación, bajo la licencia Creative Commons (CC-BY-SA-3.0).
