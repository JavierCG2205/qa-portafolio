# Día 16: Checklists

_Semana 3 · Sábado 7 de noviembre · QA Engineer_

## Tema del día

Un **checklist** es una lista corta de cosas por revisar, sin pasos detallados.

-   **Caso de prueba** = receta de cocina: paso a paso, con cantidades.
-   **Checklist** = lista de compras: te dice **qué** revisar, no **cómo**.

Sirve para revisar rápido y no olvidar nada.

## Cómo escribir un buen punto

-   Una frase corta, escrita como algo que **debe ser cierto**.
-   Una sola cosa por punto.
-   Que se pueda responder con ✔ (pasó) o ✘ (falló).

**Ejemplos buenos:**

-   Cada producto muestra su propia imagen.
-   El campo Apellido se puede llenar en el checkout.
-   Un usuario bloqueado ve un mensaje claro al intentar entrar.

**Ejemplo malo:** "Probar el login" (no dice qué revisar, no se puede marcar ✔ o ✘).

## Práctica (30 min)

Arma tu checklist de **15 a 20 puntos** de saucedemo.com. Usa tus notas del Día 15 y agrupa por zona. Anota también el usuario con el que probaste.

## Mi checklist v1

#

Zona

Punto a revisar

Usuario

¿Pasó? (✔/✘)

Notas

1

Login

Se puede ingresar con los usuarios que te brinda la página

Todos

Paso

Excepto locked\_out\_user por que aparece el mensaje "Epic sadface: Sorry, this user has been locked out."

2

Login

La contraseña secret\_sauce funciona con todos los usuarios de la lista

Todos

Paso

3

Login

Un usuario que no existe no puede entrar y ve un mensaje de error.

No aplica

Paso

4

Carrito

Todos los productos se pueden agregar al carrito

error\_user

No paso

Ingresando con el usuario "error\_user" las prendas Bolt T-Shirt, Fleece Jacket y Test.allTheThings no se agregan

5

Carrito

El carrito muestra el número de productos

Todos

Paso

6

Carrito

Los productos se pueden remover dándole clic al botón de "Remove" de cada producto

error\_user

No paso

El botón Remove falla en las prendas "Sauce Labs Backpack, Sauce Labs Bike Light y Sauce Labs Onesie"

7

Carrito

No se puede finalizar la compra sin agregar un producto

standard\_user, performance\_glitch\_user y visual\_user

No paso

Se puede finalizar el checkout con el carrito vacío en los usuarios "standard\_user", "performance\_glitch\_user" y "visual\_user"

8

Checkout (formularios)

El campo Nombre se puede llenar

Todos

Paso

9

Checkout (formularios)

El campo Apellido se puede llenar

problem\_user, error\_user

No Paso

El campo Apellido no deja escribir con los usuarios error\_user y problem\_user

10

Checkout (formularios)

El campo Zip code se puede llenar

Todos

Paso

11

Checkout (formularios)

El Overview muestra la información del producto

Todos

Paso

12

Imágenes

Cada producto cuenta con su propia imagen

problem\_user y visual\_user

No Paso

Con el usuario "problem\_user" los productos tienen la imagen de un perro y con el usuario "visual\_user" la prenda Sauce Labs Backpack es la única sin imagen propia.

13

Carrito

El precio de los productos sigue siendo mismo cuando se agregan al carrito

visual\_user

No paso

Con el usuario "visual\_user" es el único cuyos precios cambian al momento de agregarlos al carrito

14

Mensajes de error y textos

locked\_out\_user no puede entrar y ve un mensaje claro

locked\_out\_user

Paso

15

Mensajes de error y textos

El botón "logout" te regresa a iniciar sesión

Todos

Paso

16

Otra zona

Se puede ordenar los productos por nombre

Todos

Paso

17

Otra zona

Se pueden ordenar los productos por precio

Todos

Paso

18

Otra zona

Reset App State deja el carrito en 0

Todos

Paso

19

Otra zona

"Dynamic Catalog" cuenta con 3 formas de ver el catálogo

Todos

Paso

20

Otra zona

Ingresando con el usuario "performance\_glitch\_user" entra en menos de 2 segundos

performance\_glitch\_user

No Paso

Tardó unos 4 segundos en entrar a la página.