function confirmDelete(areaId) {
    Swal.fire({
        title: "¿Seguro de eliminar?",
        text: "¡No se podrá revertir la acción!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Confirmar",
        cancelButtonText: "Cancelar"
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = "{% url 'eliminarArea' 'id_placeholder' %}".replace('id_placeholder', areaId);
        }
    });
    return false;
}