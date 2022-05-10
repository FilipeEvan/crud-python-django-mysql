/* Máscara */
var SPMaskBehavior = function (val) {
    return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
},
spOptions = {
    onKeyPress: function(val, e, field, options) {
        field.mask(SPMaskBehavior.apply({}, arguments), options);
    }
};

$(function(){
    $('.mask-cep').mask('00000-000');
    $('.mask-telefone').mask(SPMaskBehavior, spOptions);
});


$(document).ready(function() {
    var btnDeletar =  $('.btn-deletar');
    var btnBuscar = $('#btn-buscar');
    var formBuscar = $('#form-buscar');

    /* Mensagem de exclusão */
    $(btnDeletar).on('click', function(e) {

        e.preventDefault();

        var delLink = $(this).attr('href');
        var resultado = confirm('Quer deletar este item?');

        if (resultado) {
            window.location.href = delLink;
        }

    });

    /* Consulta */
    $(btnBuscar).on('click', function() {
        formBuscar.submit();
        
    });
});
