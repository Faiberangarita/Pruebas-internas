/*---------------------------INDEX-----------------------------*/
/*---------------------------INDEX-----------------------------*/
/*---------------------------INDEX-----------------------------*/

const panels = document.querySelectorAll('.panel')

panels.forEach(panel => {
    panel.addEventListener('click', () => {
        removeActiveClasses()
        panel.classList.add('active')
    })
})

function removeActiveClasses() {
    panels.forEach(panel => {
        panel.classList.remove('active')
    })
}




/*---------------------------TIENDA-----------------------------*/ 
/*---------------------------TIENDA-----------------------------*/
/*---------------------------TIENDA-----------------------------*/

// Obtener todos los elementos product-card
const productCards = document.querySelectorAll('.product-card');

// Agregar evento de clic a los botones de despliegue
productCards.forEach(productCard => {
  const toggleButton = productCard.querySelector('.toggle-btn');
  const description = productCard.querySelector('.description');

  toggleButton.addEventListener('click', () => {
    productCard.classList.toggle('expanded');

    if (productCard.classList.contains('expanded')) {
      toggleButton.textContent = 'Mostrar menos...';
    } else {
      toggleButton.textContent = 'Mostrar más...';
    }
  });
});




// ----------------------------

    // Obtener todos los botones "Agregar al carrito"
    var botonesAgregar = document.querySelectorAll(".buttonProduct");

    // Iterar sobre los botones y agregar el evento de escucha de clic
    botonesAgregar.forEach(function(boton) {
        boton.addEventListener("click", agregarAlCarrito);
    });

    // Función para agregar un producto al carrito
    function agregarAlCarrito(event) {
        // Obtener los detalles del producto a partir de los atributos de datos
        var nombre = event.target.getAttribute("data-nombre");
        var precio = parseFloat(event.target.getAttribute("data-precio"));

        // Crear un objeto o estructura de datos para almacenar los detalles del producto
        var producto = {
            nombre: nombre,
            precio: precio
        };

        // Aquí puedes implementar la lógica para agregar el producto al carrito
        // Puedes utilizar localStorage, una matriz en memoria, una solicitud al servidor, etc.

        // Ejemplo de almacenamiento en localStorage
        var carrito = JSON.parse(localStorage.getItem("carrito")) || []; // Obtener el carrito existente o crear uno nuevo si no existe
        carrito.push(producto); // Agregar el producto al carrito
        localStorage.setItem("carrito", JSON.stringify(carrito)); // Guardar el carrito actualizado en localStorage

        // Mostrar un mensaje de confirmación o redireccionar a la página del carrito
        console.log("El producto se agregó al carrito de compras");
        console.log(nombre, precio);
    }



/*---------------------------LOGIN-----------------------------*/
/*---------------------------LOGIN-----------------------------*/
/*---------------------------LOGIN-----------------------------*/

    function submitForm() {
        // Obtener los valores del correo electrónico y la contraseña
        var email = document.getElementById("email").value;
        var password = document.getElementById("password").value;

        // Realizar acciones con los datos ingresados, como enviar una solicitud al servidor
        console.log("Correo electrónico:", email);
        console.log("Contraseña:", password);
    }
/*---------------------------LOGIN-----------------------------*/
/*---------------------------LOGIN-----------------------------*/
/*---------------------------LOGIN-----------------------------*/