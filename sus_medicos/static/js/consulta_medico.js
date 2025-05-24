document.addEventListener('DOMContentLoaded', function () {
    const btncompareceu = document.getElementById('btncompareceu');
    const btnnaocompareceu = document.getElementById('btnnaocompareceu');

    if (btncompareceu) {
        btncompareceu.addEventListener('click', function () {
            Swal.fire({
                title: 'Confirmar comparecimento',
                text: 'Deseja realmente confirmar que o paciente compareceu?',
                icon: 'question',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Sim, o paciente compareceu!',
                cancelButtonText: 'Não'
            }).then((result) => {
                if (result.isConfirmed) {
                    const consultaId = this.getAttribute('data-id');
                    window.location.href = `/paciente_compareceu/${consultaId}/`;
                }
            });
        });
    }

    if (btnnaocompareceu) {
        btnnaocompareceu.addEventListener('click', function () {
            Swal.fire({
                title: 'Paciente não compareceu',
                text: 'Deseja realmente confirmar que o paciente não compareceu?',
                icon: 'question',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Sim, o paciente não compareceu!',
                cancelButtonText: 'Não'
            }).then((result) => {
                if (result.isConfirmed) {
                    const consultaId = this.getAttribute('data-id');
                    window.location.href = `/paciente_nao_compareceu/${consultaId}/`;
                }
            });
        });
    }


});