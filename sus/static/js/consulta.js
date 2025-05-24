document.addEventListener('DOMContentLoaded', function () {
    const btncancelar = document.getElementById('btncancelar');
    const btnconfirmar = document.getElementById('btnconfirmar');

    if (btncancelar) {
        btncancelar.addEventListener('click', function () {
            Swal.fire({
                title: 'Confirmar cancelamento',
                text: 'Deseja realmente cancelar esta consulta?',
                icon: 'question',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Sim, cancelar!',
                cancelButtonText: 'Não'
            }).then((result) => {
                if (result.isConfirmed) {
                    const consultaId = this.getAttribute('data-id');
                    window.location.href = `/cancelar_consulta/${consultaId}/`;
                }
            });
        });
    }

    if (btnconfirmar) {
        btnconfirmar.addEventListener('click', function () {
            Swal.fire({
                title: 'Confirmar presença na unidade',
                text: 'Deseja realmente confirmar presença no hospital?',
                icon: 'question',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Sim, estou aqui!',
                cancelButtonText: 'Não'
            }).then((result) => {
                if (result.isConfirmed) {
                    const consultaId = this.getAttribute('data-id');
                    window.location.href = `/confirmar_consulta/${consultaId}/`;
                }
            });
        });
    }
});