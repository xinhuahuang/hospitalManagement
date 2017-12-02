$(document).ready(function () {
    $('#level > .ct').hide(); //所有后端配置信息默认隐藏
    $('.but').click(function(){
        $(this).parent().parent().next('.ct').slideToggle().siblings('.ct').slideUp();
    })
});