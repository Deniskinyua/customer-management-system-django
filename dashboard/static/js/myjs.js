$(document).ready(function(){
    // alert("We are all set")
    $('#div_id_se, #div_id_se_quantity, #div_id_se_unit_price, #div_id_se_totals, #div_id_te, #div_id_te_quantity, #div_id_te_unit_price, #div_id_te_totals, #div_id_fte, #div_id_fte_quantity, #div_id_fte_unit_price, #div_id_fte_totals, #div_id_ffe, #div_id_ffe_quantity, #div_id_ffe_unit_price, #div_id_ffe_totals').hide()
        $('#more-lines').click(function(){
            $('#div_id_se, #div_id_se_quantity, #div_id_se_unit_price, #div_id_se_totals').slideToggle(200)
            $('#div_id_te, #div_id_te_quantity, #div_id_te_unit_price, #div_id_te_totals').slideToggle(200)
            $('#div_id_fte, #div_id_fte_quantity, #div_id_fte_unit_price, #div_id_fte_totals').slideToggle(200)
            $('#div_id_ffe, #div_id_ffe_quantity, #div_id_ffe_unit_price, #div_id_ffe_totals').slideToggle(200)
        });

        $('#id_fe_quantity, #id_fe_unit_price, #id_se_quantity, #id_se_unit_price, #id_te_quantity, #id_te_unit_price,#id_fte_quantity, #id_fte_unit_price, #id_ffe_quantity, #id_ffe_unit_price').keyup(function(){
            var fe_quantity_txt = $('#id_fe_quantity').val();
            var fe_unit_price_txt = $('#id_fe_unit_price').val();
            var fe_totals = fe_quantity_txt * fe_unit_price_txt

            var se_quantity_txt = $('#id_se_quantity').val();
            var se_unit_price_txt = $('#id_se_unit_price').val();
            var se_totals = se_quantity_txt * se_unit_price_txt

            var te_quantity_txt = $('#id_te_quantity').val();
            var te_unit_price_txt = $('#id_te_unit_price').val();
            var te_totals = te_quantity_txt * te_unit_price_txt

            var fte_quantity_txt = $('#id_fte_quantity').val();
            var fte_unit_price_txt = $('#id_fte_unit_price').val();
            var fte_totals = fte_quantity_txt * fte_unit_price_txt

            var ffe_quantity_txt = $('#id_ffe_quantity').val();
            var ffe_unit_price_txt = $('#id_ffe_unit_price').val();
            var ffe_totals = ffe_quantity_txt * ffe_unit_price_txt

            var total = fe_totals + se_totals + te_totals + fte_totals + ffe_totals
            $('#id_fe_totals').val(fe_totals);
            $('#id_se_totals').val(se_totals);
            $('#id_te_totals').val(te_totals);
            $('#id_fte_totals').val(fte_totals);
            $('#id_ffe_totals').val(ffe_totals);
            $('#id_total').val(total)
        });
});
