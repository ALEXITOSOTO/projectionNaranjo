// Inicializa la validación del formulario con jQuery Validate
$("#frm_nueva_variedad").validate({
    rules: {
        nombre: {
            required: true
        },
        caracteristicas: {
            required: true
        }
    },
    messages: {
        nombre: {
            required: "Ingrese el nombre de la variedad",
        },
        caracteristicas: {
            required: "Ingrese las características de la variedad"
        }
    },
    submitHandler: function(formulario) {
        const formData = new FormData(formulario);
        
        $.ajax({
            url: "{% url 'guardarVariedad' %}", // Cambia esto al nombre de la vista en Django que maneja la solicitud POST
            type: "POST",
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response.estado) {
                    Swal.fire({
                        title: "Confirmación",
                        text: response.mensaje,
                        icon: 'success'
                    }).then(() => {
                        location.reload();
                    });
                    
                    $('#exampleModal').modal('hide');
                    formulario.reset();
                    cargarVariedades();
                } else {
                    Swal.fire({
                        title: "Error",
                        text: response.mensaje,
                        icon: 'error'
                    });
                }
            },
            error: function(xhr, status, error) {
                Swal.fire({
                    title: "Error",
                    text: "Hubo un error al guardar la variedad",
                    icon: 'error'
                });
            }
        });
    }
});

function cargarVariedades() {
    $("#contenedor-variedades").load('{% url "listadoVariedades" %}', function(response, status, xhr) {
        if (status === "error") {
            console.error("Error al cargar variedades: " + xhr.status + " " + xhr.statusText);
        } else {
            console.log("Variedades cargadas correctamente.");
        }
    });
}

$(document).ready(function() {
    cargarVariedades();
});
