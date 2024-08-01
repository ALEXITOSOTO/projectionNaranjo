$('#login-form').validate({
    rules: {
        user: {
            required: true
        },
        pass: {
            required: true
        }
    },
    messages: {
        user: {
            required: "El usuario es necesario"
        },
        pass: {
            required: "La contraseña es necesaria"
        }
    },
    submitHandler: function (formulario) {
        $.ajax({
            type: 'POST',
            url: '{% url "gestionAreas" %}',
            data: $(formulario).serialize(),
            success: function (data) {
                if (data.estado) {
                    window.location.href = data.redirect_url;
                } else {
                    $('#login-form').validate().showErrors({
                        user: data.mensajeUsu || 'Usuario incorrecto',
                        pass: data.mensaje || 'Contraseña incorrecta'
                    });
                }
            },
            error: function () {
                alert('Error en el inicio de sesión. Por favor, intente nuevamente.');
            }
        });
    }
});