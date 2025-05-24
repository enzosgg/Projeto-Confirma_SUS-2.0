document.querySelectorAll('tbody tr').forEach(row => {
    row.addEventListener('click', () => {

        if (row.classList.contains('nao-clicavel')) {
            return;
        }

        const consultaId = row.getAttribute('data-consulta-id');
        const consultaAtualId = document.getElementById('consulta-atual-id').value;

        Swal.fire({
            title: 'Confirmar reagendamento',
            text: 'Deseja realmente reagendar esta consulta?',
            icon: 'question',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Sim, reagendar!',
            cancelButtonText: 'Não'
        }).then((result) => {
            if (result.isConfirmed) {
                window.location.href = `/confirmar-reagendamento/${consultaAtualId}/${consultaId}/`;
            }
        });
    });
});