function confirmDelete(responsableId) {
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
            const url = eliminarResponsableUrl.replace('id_placeholder', responsableId);
            window.location.href = url;
        }
    });
    return false;
}