/**
 * Created by huangxinhua on 2017/11/17.
 */
$(function () {
    $('input[name="b5a11"]').click(function () {
        if(this.value==0){
            $("#kind_b5a11").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
        }else{
            $("#kind_b5a11").css('display','none');
        }
    });

    $('input[name="b5a110"]').click(function () {
        if(this.value==1){
            $("#k_b5a11").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
        }else{
            $("#k_b5a11").css('display','none');
        }
    });

    $('#close_naogenshi').click(function () {
        $("#kind_b5a11").css('display','none');
    });

    $('input[name="b5a21"]').click(function () {
        if(this.value==0){
            $("#kind_b5a21").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
        }else{
            $("#kind_b5a21").css('display','none');
        }
    });

    $('input[name="b5a27"]').click(function () {
        if(this.value==0){
            $("#kind_b5a27").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
        }else{
            $("#kind_b5a27").css('display','none');
        }
    });

    $("#close_xingdong").click(function () {
        $("#kind_b5a21").css('display','none');
    });

    $('input[name="b5a31"]').click(function () {
        if(this.value==0){
            $("#kind_b5a31").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
        }else{
            $("#kind_b5a31").css('display','none');
        }
    });

    $('input[name="b5a34"]').click(function () {
        if(this.value==0){
            $("#kind_b5a34").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
        }else{
            $("#kind_b5a34").css('display','none');
        }
    });

    $("#close_jixian").click(function () {
        $("#kind_b5a31").css('display','none');
    });

    $('input[name="b5a41"]').click(function () {
        if(this.value==0){
            $("#kind_b5a41").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
        }else{
            $("#kind_b5a41").css('display','none');
        }
    });

    $("#close_jizheng").click(function () {
        $("#kind_b5a41").css('display', 'none');
    });

    $('input[name="c1"]').click(function () {
        if(this.value==3){
            $("#kind_c1").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
        }else{
            $("#kind_c1").css('display','none');
        }
    });

    $("#close_hunmi").click(function () {
        $("#kind_c1").css('display', 'none');
    });


    $('input[name="c2"]').click(function () {
        if(this.value==10 && this.checked){
            $("#id_c2a1").css({'display':'inline-block'});
        }else{
            $("#id_c2a1").css({'display':'none'});
        }
    });

    $('input[name="c12a1"]').click(function () {
        if(this.value==0){
            $("#kind_c12a1").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
        }else{
            $("#kind_c12a1").css('display','none');
        }
    });

    $("#close_mrt").click(function () {
        $("#kind_c12a1").css('display', 'none');
    });

    $('input[name="c14a1"]').click(function () {
        if(this.value==0){
            $("#kind_c14a1").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
        }else{
            $("#kind_c14a1").css('display','none');
        }
    });

    $("#close_xindianjianhu").click(function () {
        $("#kind_c14a1").css('display', 'none');
    });

    $('input[name="d1a10"]').click(function () {
        if(this.value==0){
            $("#kind_d1a10").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
        }else{
            $("#kind_d1a10").css('display','none');
        }
    });

    $("#close_kangxuexiaoban").click(function () {
        $("#kind_d1a10").css('display', 'none');
    });

    $('input[name="d1a11"]').click(function () {
        if(this.value==1){
            $("#id_d1a12").attr("disabled",true);
            $("#id_d1a13").attr("disabled",true);
            $("#id_d1a14").attr({"disabled":false, "background":"#999"});
            $("#id_d1a15").attr({"disabled":false, "background":"#999"});
        }else{
            $("#id_d1a12").attr({"disabled":false, "background":"#999"});
            $("#id_d1a13").attr({"disabled":false, "background":"#999"});
            $("#id_d1a14").attr("disabled",true);
            $("#id_d1a15").attr("disabled",true);
        }
    });

    $('input[name="d1a20"]').click(function () {
        if(this.value==0){
            $("#kind_d1a20").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
        }else{
            $("#kind_d1a20").css('display','none');
        }
    });

    $("#close_kangningyaowu").click(function () {
        $("#kind_d1a20").css('display', 'none');
    });

    $('input[name="d1a21"]').click(function () {
        if(this.value==6){
            $("#id_d1a23").attr({"disabled":false, "background":"#999"});
        }else{
            $("#id_d1a23").attr("disabled",true);
        }
    });

    $('input[name="d1a30"]').click(function () {
        if(this.value==0){
            $("#kind_d1a30").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
        }else{
            $("#kind_d1a30").css('display','none');
        }
    });

    $("#close_tiaojiexuezhi").click(function () {
        $("#kind_d1a30").css('display', 'none');
    });

    $('input[name="d1a222"]').attr('disabled',true);
    $('input[name="d1a35"]').attr('disabled',true);
    $('input[name="d1a38"]').attr('disabled',true);
    $('input[name="d1a311"]').attr('disabled',true);
    $('input[name="d1a314"]').attr('disabled',true);

    $('input[name="d1a31"]').click(function () {
        if(this.checked && this.value==0){
            $('input[name="d1a222"]').attr('disabled',false);
            return true;
        }else if(this.checked &&this.value==1){
            $('input[name="d1a35"]').attr('disabled',false);
            return true;
        }else if(this.checked &&this.value==2){
            $('input[name="d1a38"]').attr('disabled',false);
            return true;
        }else if(this.checked &&this.value==3){
            $('input[name="d1a311"]').attr('disabled',false);
            return true;
        }else if(this.checked &&this.value==4){
            $('input[name="d1a314"]').attr('disabled',false);
            return true;
        }else if(this.checked && this.value==5){
            $("#id_d1a317").attr('disabled',false);
            return true;
        }

        if(this.checked == false && this.value==0){
            $('input[name="d1a222"]').attr('disabled',true);
            return true;
        }else if(this.checked == false &&this.value==1){
            $('input[name="d1a35"]').attr('disabled',true);
            return true;
        }else if(this.checked == false &&this.value==2){
            $('input[name="d1a38"]').attr('disabled',true);
            return true;
        }else if(this.checked == false &&this.value==3){
            $('input[name="d1a311"]').attr('disabled',true);
            return true;
        }else if(this.checked == false &&this.value==4){
            $('input[name="d1a314"]').attr('disabled',true);
            return true;
        }else if(this.checked == false && this.value==5){
            $("#id_d1a317").attr('disabled',false);
            return true;
        }
    });

    $('input[name="d1a222"]').click(function () {
        if(this.checked && this.value==7){
            $("#id_d1a33").attr({"disabled":false, "background":"#999"});
        }else{
            $("#id_d1a33").attr("disabled",true);
        }
    });

    $('input[name="d1a35"]').click(function () {
        if(this.value==4 && this.checked){
            $("#id_d1a36").attr({"disabled":false, "background":"#999"});
        }else{
            $("#id_d1a36").attr("disabled",true);
        }
    });

    $('input[name="d1a38"]').click(function () {
        if(this.value==1 && this.checked){
            $("#id_d1a39").attr({"disabled":false, "background":"#999"});
        }else{
            $("#id_d1a39").attr("disabled",true);
        }
    });

    $('input[name="d1a311"]').click(function () {
        if(this.value==4 && this.checked){
            $("#id_d1a312").attr({"disabled":false, "background":"#999"});
        }else{
            $("#id_d1a312").attr("disabled",true);
        }
    });

    $('input[name="d1a314"]').click(function () {
        if(this.value==2 && this.checked){
            $("#id_d1a315").attr({"disabled":false, "background":"#999"});
        }else{
            $("#id_d1a315").attr("disabled",true);
        }
    });

    $('input[name="d1a40"]').click(function () {
        if(this.value==0){
            $("#kind_d1a40").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
        }else{
            $("#kind_d1a40").css('display','none');
        }
    });

    $("#close_kongzhixueya").click(function () {
         $("#kind_d1a40").css('display', 'none');
    });

    $('input[name="d1a401"]').click(function () {
        if(this.value==0){
            $("#kind_d1a401").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
        }else{
            $("#kind_d1a401").css('display','none');
        }
    });

    $("#close_qita").click(function () {
         $("#kind_d1a401").css('display', 'none');
    });

    $('input[name="d1a401_1"]').click(function () {
        if(this.checked && this.value==0){
            $("#kind_d1a401_1").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
            return true;
        }else if(this.checked==false && this.value==0){
            $("#kind_d1a401_1").css('display','none');
            return true;
        }

        if(this.checked && this.value==1){
            $("#kind_d1a401_2").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
            return true;
        }else if(this.checked==false && this.value==1){
            $("#kind_d1a401_2").css('display','none');
            return true;
        }

        if(this.checked && this.value==2){
            $("#kind_d1a401_3").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
            return true;
        }else if(this.checked==false && this.value==2){
            $("#kind_d1a401_3").css('display','none');
            return true;
        }

        if(this.checked && this.value==3){
            $("#kind_d1a401_4").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
            return true;
        }else if(this.checked==false && this.value==3){
            $("#kind_d1a401_4").css('display','none');
            return true;
        }

        if(this.checked && this.value==4){
            $("#kind_d1a401_5").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
            return true;
        }else if(this.checked==false && this.value==4){
            $("#kind_d1a401_5").css('display','none');
            return true;
        }


    });

    $("#close_zhongyao").click(function () {
         $("#kind_d1a401_1").css('display', 'none');
    });

    $("#close_naobaohu").click(function () {
         $("#kind_d1a401_2").css('display', 'none');
    });

    $("#close_tuoshui").click(function () {
         $("#kind_d1a401_3").css('display', 'none');
    });

    $("#close_kuorongyaowu").click(function () {
         $("#kind_d1a401_4").css('display', 'none');
    });

    $("#close_kongzhixuetang").click(function () {
         $("#kind_d1a401_5").css('display', 'none');
    });

    $('input[name="d1a531"]').click(function () {
        if(this.checked && this.value==0){
            $("#kind_d1a401_5_1").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
            return true;
        }else if(this.checked==false && this.value==0){
            $("#kind_d1a401_5_1").css('display','none');
            return true;
        }

        if(this.checked && this.value==1){
            $("#kind_d1a401_5_2").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
            return true;
        }else if(this.checked==false && this.value==1){
            $("#kind_d1a401_5_2").css('display','none');
            return true;
        }

        if(this.checked && this.value==2){
            $("#kind_d1a401_5_3").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
            return true;
        }else if(this.checked==false && this.value==2){
            $("#kind_d1a401_5_3").css('display','none');
            return true;
        }

        if(this.checked && this.value==3){
            $("#kind_d1a401_5_4").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
            return true;
        }else if(this.checked==false && this.value==3){
            $("#kind_d1a401_5_4").css('display','none');
            return true;
        }

        if(this.checked && this.value==4){
            $("#kind_d1a401_5_5").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
            return true;
        }else if(this.checked==false && this.value==4){
            $("#kind_d1a401_5_5").css('display','none');
            return true;
        }

        if(this.checked && this.value==5){
            $("#kind_d1a401_5_6").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
            return true;
        }else if(this.checked==false && this.value==5){
            $("#kind_d1a401_5_6").css('display','none');
            return true;
        }

        if(this.checked && this.value==6){
            $("#kind_d1a401_5_7").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
            return true;
        }else if(this.checked==false && this.value==6){
            $("#kind_d1a401_5_7").css('display','none');
            return true;
        }

        if(this.checked && this.value==7){
            $("#kind_d1a401_5_8").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
            return true;
        }else if(this.checked==false && this.value==7){
            $("#kind_d1a401_5_8").css('display','none');
            return true;
        }
    });

    $("#close_yidaoshu").click(function () {
         $("#kind_d1a401_5_1").css('display', 'none');
    });

    $("#close_shuanghulei").click(function () {
         $("#kind_d1a401_5_2").css('display', 'none');
    });

    $("#close_huangxianniao").click(function () {
         $("#kind_d1a401_5_3").css('display', 'none');
    });

    $("#close_butaotang").click(function () {
         $("#kind_d1a401_5_4").css('display', 'none');
    });

    $("#close_shaichuowan").click(function () {
         $("#kind_d1a401_5_5").css('display', 'none');
    });

    $("#close_gelinai").click(function () {
         $("#kind_d1a401_5_6").css('display', 'none');
    });

    $("#close_yigaotang").click(function () {
         $("#kind_d1a401_5_7").css('display', 'none');
    });

    $("#close_ertaiji").click(function () {
         $("#kind_d1a401_5_8").css('display', 'none');
    });

    $("#close_qita").click(function () {
        $("#kind_d1a401").css('display', 'none');
    });

    $('input[name="d2a10"]').click(function () {
        if(this.checked && this.value==0){
            $("#kind_d2a10").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
            return true;
        }else if(this.checked==false && this.value==0){
            $("#kind_d2a10").css('display','none');
            return true;
        }
    });

    $("#close_tuoshuiyaowu").click(function () {
        $("#kind_d2a10").css('display', 'none');
    });

    $('input[name="d2a21"]').click(function () {
        if(this.checked && this.value==0){
            $("#kind_d2a21").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
            return true;
        }else if(this.checked==false && this.value==0){
            $("#kind_d2a21").css('display','none');
            return true;
        }
    });

    $("#close_kongzhixueya2").click(function () {
        $("#kind_d2a21").css('display', 'none');
    });

    $('input[name="d1a401_2_2"]').click(function () {
        if(this.checked && this.value==0){
            $("#kind_d2a212_2_2").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
            return true;
        }else if(this.checked==false && this.value==0){
            $("#kind_d2a212_2_2").css('display','none');
            return true;
        }

        if(this.checked && this.value==1){
            $("#kind_d2a212_2_3").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
            return true;
        }else if(this.checked==false && this.value==1){
            $("#kind_d2a212_2_3").css('display','none');
            return true;
        }

        if(this.checked && this.value==2){
            $("#id_d2a331").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
            return true;
        }else if(this.checked==false && this.value==2){
            $("#id_d2a331").css('display','none');
            return true;
        }
    });

    $('input[name="d2a212"]').click(function () {
        if (this.checked && this.value == 0) {
            $("#kind_d2a212_2").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
            return true;
        } else if (this.checked == false && this.value == 0) {
            $("#kind_d2a212_2").css('display', 'none');
            return true;
        }
    });

    $("#close_zhongyao2").click(function () {
        $("#kind_d2a212_2_2").css('display', 'none');
    });


    $("#close_naobaohu2").click(function () {
        $("#kind_d2a212_2_3").css('display','none');
    });


    $('input[name="d2a331"]').click(function () {
        if (this.checked && this.value == 0) {
            $("#id_d2a331_1").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
            return true;
        } else if (this.checked == false && this.value == 0) {
            $("#id_d2a331_1").css('display', 'none');
            return true;
        }

        if (this.checked && this.value == 1) {
            $("#id_d2a331_2").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
            return true;
        } else if (this.checked == false && this.value == 1) {
            $("#id_d2a331_2").css('display', 'none');
            return true;
        }

        if (this.checked && this.value == 2) {
            $("#id_d2a331_3").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
            return true;
        } else if (this.checked == false && this.value == 2) {
            $("#id_d2a331_3").css('display', 'none');
            return true;
        }

        if (this.checked && this.value == 3) {
            $("#id_d2a331_4").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
            return true;
        } else if (this.checked == false && this.value == 3) {
            $("#id_d2a331_4").css('display', 'none');
            return true;
        }

        if (this.checked && this.value == 4) {
            $("#id_d2a331_5").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
            return true;
        } else if (this.checked == false && this.value == 4) {
            $("#id_d2a331_5").css('display', 'none');
            return true;
        }

        if (this.checked && this.value == 5) {
            $("#id_d2a331_6").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
            return true;
        } else if (this.checked == false && this.value == 5) {
            $("#id_d2a331_6").css('display', 'none');
            return true;
        }

        if (this.checked && this.value == 6) {
            $("#id_d2a331_7").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
            return true;
        } else if (this.checked == false && this.value == 6) {
            $("#id_d2a331_7").css('display', 'none');
            return true;
        }

        if (this.checked && this.value == 7) {
            $("#id_d2a331_8").css({'display':'block','border':'1px solid rgba(0,0,0,.2)','background':'white','padding':'10px 0px'});
            return true;
        } else if (this.checked == false && this.value == 7) {
            $("#id_d2a331_8").css('display', 'none');
            return true;
        }
    });


    $("#close_yidaoshu2").click(function () {
        $("#id_d2a331_1").css('display', 'none');
    });


    $("#close_shuanhulei2").click(function () {
        $("#id_d2a331_2").css('display', 'none');
    });

    $("#close_huangxiniao2").click(function () {
        $("#id_d2a331_3").css('display', 'none');
    });

    $("#close_putaotang2").click(function () {
        $("#id_d2a331_4").css('display', 'none');
    });

    $("#close_shaichuowan2").click(function () {
        $("#id_d2a331_5").css('display', 'none');
    });

    $("#close_gelienai2").click(function () {
        $("#id_d2a331_6").css('display', 'none');
    });

    $("#close_yigaotang2").click(function () {
        $("#id_d2a331_7").css('display', 'none');
    });

    $("#close_ertaiji2").click(function () {
        $("#id_d2a331_8").css('display', 'none');
    });
    
    $("#close_kongzhixuetang2").click(function () {
        $("#id_d2a331").css('display', 'none');
    });;

     $("#close_qita2").click(function () {
        $("#kind_d2a212_2").css('display', 'none');
    });

    $('input[name="d2a331_1_1"]').click(function () {
        if (this.checked && this.value == 0) {
            $("#id_d2a331_8_1").css({
                'display': 'block',
                'border': '1px solid rgba(0,0,0,.2)',
                'background': 'white',
                'padding': '10px 0px'
            });
            return true;
        } else if (this.checked == false && this.value == 0) {
            $("#id_d2a331_8_1").css('display', 'none');
            return true;
        }
    });

    $("#close_weixiayingshu").click(function () {
        $("#id_d2a331_8_1").css('display', 'none');
    });
});