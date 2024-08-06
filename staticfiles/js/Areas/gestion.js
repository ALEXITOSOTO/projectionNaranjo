// Inicializa la validación del formulario con jQuery Validate
$("#frm_nuevo_area").validate({
    rules: {
        codigo: {
            required: true
        },
        nombre: {
            required: true
        },
        descripcion: {
            required: true
        }
    },
    messages: {
        codigo: {
            required: "Ingrese código para identificar el área",
        },
        nombre: {
            required: "Ingrese nombre del área"
        },
        descripcion: {
            required: "Ingrese descripción"
        }
    },
    submitHandler: function(formulario) {
        const formData = new FormData(formulario);
        
        $.ajax({
            url: "{% url 'guardarArea' %}", // Cambia esto al nombre de la vista en Django que maneja la solicitud POST
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
                    cargarareas();
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
                    text: "Hubo un error al guardar el área",
                    icon: 'error'
                });
            }
        });
    }
});

function cargarareas() {
    $("#contenedor-areas").load('{% url "listadoAreas" %}', function(response, status, xhr) {
        if (status === "error") {
            console.error("Error al cargar áreas: " + xhr.status + " " + xhr.statusText);
        } else {
            console.log("Áreas cargadas correctamente.");
        }
    });
}

$(document).ready(function() {
    cargarareas();
});