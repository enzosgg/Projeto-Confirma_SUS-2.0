document.querySelectorAll('tbody tr').forEach(row => {
    row.addEventListener('click', () => {

        if (row.classList.contains('nao-clicavel')) {
            return; 
        }

        const consultaId = row.getAttribute('data-consulta-id');

        Swal.fire({
            title: 'Confirmar marcação',
            text: 'Deseja realmente marcar esta consulta?',
            icon: 'question',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Sim, marcar!',
            cancelButtonText: 'Não'
        }).then((result) => {
            if (result.isConfirmed) {window.location.href = `/confirmar_marcacao/${consultaId}/`;}
        });
    });
});