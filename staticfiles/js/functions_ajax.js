function utilizouHoraExtra(id) {
    console.log(id)
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: '/horas-extras/used-time-bank/' + id,
        data: {
            csrfmiddlewaretoken: token,
        },
        success: function(result) {
            var button = $("#btn_horas")
            
            if (button.hasClass('btn-info')) {
                button.removeClass('btn-info').addClass('btn-danger');
                button.text('Marcar como não utilizada');
            } else {
                button.removeClass('btn-danger').addClass('btn-info');
                button.text('Marcar como utilizada');
            }

            $("#horas_atualizadas").text('Total de horas extras: ' + result.horas)
        }
    });
};