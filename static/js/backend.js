$(function () {

    //初始化Button的点击事件
    var oButtonInit = new ButtonInit();
    oButtonInit.Init();

    //初始化Table
    var arr = [];
    $.ajax({
        type: "GET",
        url: '/show_ssd',
        data:{},
        datatype:'json',
        success: function(data){
            datas = JSON.parse(data["res"]);
            for(var i=0;i<datas.length;i++){
                var info = {};
                info['id'] = datas[i]["id"];
                info['name'] = datas[i]["name"];
                info['idnumble'] = datas[i]["idnumble"];
                info['numble'] = datas[i]['numble'];

                // book外建信息
                var book = JSON.parse(datas[i]['book']);
                info['book_conname'] = book["conname"];
                //其余字段自己补充

                // bookcure外建信息
                var bookcure = JSON.parse(datas[i]['bookcure']);
                info['bookcure_b1'] = bookcure['b1'];
                //其余字段自己补充

                //
                var bookcheck = JSON.parse(datas[i]['bcheck']);
                info['bookcheck_c1'] = bookcheck['c1'];
                //其余字段自己补充

                //
                var bookhealth = JSON.parse(datas[i]['bhealth']);
                info['bookhealth_d1a10'] = bookhealth['d1a10'];
                //其余字段自己补充

                //
                var bookdange = JSON.parse(datas[i]['bdange']);
                info['bookdange_e1'] = bookdange['e1'];
                //其余字段自己补充

                //
                var bookchange = JSON.parse(datas[i]['bchange']);
                info['bookchange_f1'] = bookchange['f1'];
                //其余字段自己补充

                //
                var booksituation = JSON.parse(datas[i]['bsituation']);
                info['booksituation_g1'] = booksituation['g1'];
                //其余字段自己补充

                //
                var bookdiagnose = JSON.parse(datas[i]['bdiagnose']);
                info['bookdiagnose_h1'] = bookdiagnose['h1'];
                //其余字段自己补充

                var booktime = JSON.parse(datas[i]['btime']);
                info['booktime_i1'] = booktime['i1'];
                //其余字段自己补充

                arr.push(info)
            }
            var oTable = new TableInit(arr);
            oTable.Init();
        }
    });
    toggleModifyDisable();

    $('#btn_delete').click(function() {
        var ids = get_ids();
        var data = {};
        data['id'] = JSON.stringify(ids);
        confirm_alert('确认框','是否确认删除?',function(){
            $.ajax({
                type: "POST",
                url: '/delete_ssd/',
                data: data,
                datatype: "json",
                success: function(data){
                    msg = data['msg'];
                    (msg ='ok')?info = '删除成功!':info = '删除失败';
                    show_confirm_alert("结果",info,function () {
                        window.location.href = '/backend/';
                    });
                    toggleModifyDisable()
                }
            })
        })
    });

    $('#btn_edit').click(function(){
        var id = get_ids();
        var data = {};
        data['id'] = JSON.stringify(id);
        console.log('id:',id);
        edit_modal(function () {
            $.ajax({
                type: "GET",
                url: '/edit_ssd',
                data: data,
                datatype: "json",
                success: function(data){
                    name = data['name'];
                    idnumble = data['idnumble'];
                    $('.ename').val(name);
                    $('.eidnumble').val(idnumble);
                    // 其余字段自己补充
                }
            })
        })

    });
});


var TableInit = function (data) {
    var oTableInit = {};
    //初始化Table
    oTableInit.Init = function () {
        $('#table_info').bootstrapTable({
            toolbar: '#toolbar',                //工具按钮用哪个容器
            striped: true,                      //是否显示行间隔色
            cache: false,                       //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
            pagination: true,                   //是否显示分页（*）
            sortable: false,                     //是否启用排序
            sortOrder: "asc",                   //排序方式
            queryParams: oTableInit.queryParams,//传递参数（*）
            sidePagination: "client",           //分页方式：client客户端分页，server服务端分页（*）
            pageNumber: 1,                       //初始化加载第一页，默认第一页
            pageSize: 15,                       //每页的记录行数（*）
            pageList: [15, 25, 30],        //可供选择的每页的行数（*）
            search: true,                       //是否显示表格搜索，此搜索是客户端搜索，不会进服务端，所以，个人感觉意义不大
            strictSearch: true,
            showColumns: true,                  //是否显示所有的列
            showRefresh: true,                  //是否显示刷新按钮
            minimumCountColumns: 2,             //最少允许的列数
            clickToSelect: true,                //是否启用点击选中行
            height: 650,                        //行高，如果没有设置height属性，表格自动根据记录条数觉得表格高度
            uniqueId: "id",                     //每一行的唯一标识，一般为主键列
            showToggle: true,                    //是否显示详细视图和列表视图的切换按钮
            cardView: false,                    //是否显示详细视图
            detailView: false,                   //是否显示父子表
            columns: [{
                checkbox: true
            }, {
                field: 'id',
                title: '编号',
                sortable: true
            }, {
                field: 'name',
                title: '姓名',
                sortable: true
            },{
                field: 'idnumble',
                title: '身份证'
            },{
                field: 'numble',
                title: '住院号'
            },{
                field: 'book_conname',
                title: '联系人姓名'
            }],
            //剩余字段自己补充
            data:data,
            onCheck: toggleModifyDisable,
            onUncheck: toggleModifyDisable,
            onCheckAll: toggleModifyDisable,
            onUncheckAll: toggleModifyDisable,
            onDblClickRow: function (item,e) {
                $('#view').modal();
                console.log('item:',item);
                var name = item.name;
                var idnumble = item.idnumble;
                var numble = item.numble;
                $('#name').html(name);
                $('#idnumble').html(idnumble);
                $('#numble').html(numble);
                $

            }
        });
    };

    //得到查询的参数
    oTableInit.queryParams = function (params) {
        var temp = {   //这里的键的名字和控制器的变量名必须一直，这边改动，控制器也需要改成一样的
            limit: params.limit,   //页面大小
            offset: params.offset,  //页码
        };
        return temp;
    };
    return oTableInit;
};


var ButtonInit = function () {
    var oInit = {};
    oInit.Init = function () {
        //初始化页面上面的按钮事件
    };

    return oInit;
};

<!-- 修改按钮是否点击 -->
function toggleModifyDisable() {
    $('#btn_edit').prop('disabled',$('#table_info').bootstrapTable('getAllSelections').length != 1);
    $('#btn_delete').prop('disabled',$('#table_info').bootstrapTable('getAllSelections').length != 1);
}

<!-- 获取选择项 -->
function get_ids() {
    return $.map($('#table_info').bootstrapTable('getSelections'),function(row){
        return row.id
    });
}

<!-- 删除确认框 -->
function confirm_alert(title,content,callback){
    alert = $('<div class="modal fade" data-backdrop="static" id="confirm_alert_modal" tabindex="-1" style="top:30%">' +
                '<div class="modal-dialog" style="width:300px">' +
                    '<div class="modal-content">' +
                        '<div class="modal-header">' +
                            '<button type="button" class="close" data-dismiss="modal">' +
                                '&times;' +
    '                       </button>' +
                            '<h4 class="modal-title">' +
                                title +
                            '</h4>' +
                        '</div>' +
                        '<div class="modal-body">' +
                            content+
                        '</div>' +
                        '<div class="modal-footer">' +
                            '<button type="button" class="btn btn-success" data-dismiss="modal" id="sure_confirm_alert">' +
                                '确定' +
                            '</button>' +
                        '</div>' +
                     '</div>' +
                 '</div>' +
              '</div>');

    $('body').append(alert);
    alert.modal("show");
    $('#sure_confirm_alert').click(function () {
        callback();
        alert.modal("hide");
    })
}

function edit_modal(callback){
    alert = $('<div class="modal fade" id="edit" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabel">\n' +
        '    <div class="modal-dialog modal-lg" role="document">\n' +
        '        <div class="modal-content">\n' +
        '            <div class="modal-header">\n' +
        '                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n' +
        '                <h4 class="modal-title">修改</h4>\n' +
        '            </div>\n' +
        '            <div class="wrapper wrapper-content animated fadeInRight">\n' +
        '                <ul id="myTab" class="nav nav-tabs">\n' +
        '                    <li class="active"><a href="#EA" data-toggle="tab">1.基本信息</a></li>\n' +
        '                    <li><a href="#EB" data-toggle="tab">2.血管再开通治疗</a></li>\n' +
        '                    <li><a href="#EC" data-toggle="tab">3.首次评估及化验检查</a></li>\n' +
        '                    <li><a href="#ED" data-toggle="tab">4.入院后治疗</a></li>\n' +
        '                    <li><a href="#EE" data-toggle="tab">5.危险因素</a></li>\n' +
        '                    <li><a href="#EF" data-toggle="tab">6.住院1周内病情变化</a></li>\n' +
        '                    <li><a href="#EG" data-toggle="tab">7.出院情况</a></li>\n' +
        '                    <li><a href="#EH" data-toggle="tab">8.出院诊断</a></li>\n' +
        '                    <li><a href="#EI" data-toggle="tab">9.住院时间</a></li>\n' +
        '                </ul>\n' +
        '                <div id="myTabContent" class="tab-content">\n' +
        '                    <div class="tab-pane fade in active" id="EA">\n' +
        '                        <div class="panel panel-default" style="margin-top: 10px">\n' +
        '                            <div class="panel-heading">\n' +
        '                                <h3 class="panel-title">\n' +
        '                                    基本信息\n' +
        '                                </h3>\n' +
        '                            </div>\n' +
        '                            <div class="panel-body">\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-4">姓名: <input type="text" class="ename"></div>\n' +
        '                                    <div class="col-md-4">性别: <input type="text" class="egender"></div>\n' +
        '                                    <div class="col-md-4">年龄: <input type="text" class="eage"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-4">住院号: <input type="text" class="enumble"></div>\n' +
        '                                    <div class="col-md-4">身份证号: <input type="text" class="eidnumble"></div>\n' +
        '                                    <div class="col-md-4">患者电话: <input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-4">联系人姓名: <input type="text"></div>\n' +
        '                                    <div class="col-md-4">联系人姓名: <input type="text"></div>\n' +
        '                                    <div class="col-md-4">联系人电话: <input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-6">现地址: <input type="text"></div>\n' +
        '                                    <div class="col-md-6">现住址乡/镇/街道: <input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-6">出生地地址: <input type="text"></div>\n' +
        '                                    <div class="col-md-6">出生地乡/镇/街道: <input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-12">医保类型: <input type="text"></div>\n' +
        '                                </div>\n' +
        '                            </div>\n' +
        '                        </div>\n' +
        '                    </div>\n' +
        '                    <div class="tab-pane fade" id="EB">\n' +
        '                        <div class="panel panel-default" style="margin-top: 10px;overflow: scroll">\n' +
        '                            <div class="panel-heading">\n' +
        '                                <h3 class="panel-title">血管再开通治疗</h3>\n' +
        '                            </div>\n' +
        '                            <div class="panel-body">\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-4">是否为醒后卒中: <input type="text"></div>\n' +
        '                                    <div class="col-md-4">发病时间: <input type="text"></div>\n' +
        '                                    <div class="col-md-4">由何种途径转运至医院: <input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-4">到院时间: <input type="text"></div>\n' +
        '                                    <div class="col-md-4">入院诊断: <input type="text"></div>\n' +
        '                                    <div class="col-md-4">确诊依据: <input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-12">如果是脑梗死，是否行静脉溶栓治疗:</div>\n' +
        '                                </div>\n' +
        '                                <br>\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-4">溶栓开始时间: <input type="text"></div>\n' +
        '                                    <div class="col-md-4">溶栓地点: <input type="text"></div>\n' +
        '                                    <div class="col-md-4">所用药物为: 尿激酶用量(mg) <input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <br>\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-3">溶栓前NHISS评分: <input type="text"></div>\n' +
        '                                    <div class="col-md-3">溶栓后NHISS评分: <input type="text"></div>\n' +
        '                                    <div class="col-md-3">是否有并发症: <input type="text"></div>\n' +
        '                                    <div class="col-md-3">原因: <input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-12">患者是否行动脉溶栓治疗: <input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <br>\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-6">如果“是”，则溶栓开始时间为: <input type="text"></div>\n' +
        '                                    <div class="col-md-6">所用药物为:尿激酶用量(mg) <input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <br>\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-12">溶栓后NHISS评分: <input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <br>\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-6">如果“是”，则动脉是否再通: <input type="text"></div>\n' +
        '                                    <div class="col-md-6">若选择“是”，则动脉再通时间为: <input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-12">患者是否行机械取栓治疗: <input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <br>\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-6">如果“是”，则机械取栓开始时间为: <input type="text"></div>\n' +
        '                                    <div class="col-md-6">取栓后NHISS评分 <input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <br>\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-6">如果“是”，则动脉是否再通？ <input type="text"></div>\n' +
        '                                    <div class="col-md-6">若选择“是”，则动脉再通时间为 <input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-12">患者是否行急诊支架治疗？ <input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <br>\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-6">如果“是”，则支架开始时间为 <input type="text"></div>\n' +
        '                                    <div class="col-md-6">急诊支架后NHISS评分 <input type="text"></div>\n' +
        '                                </div>\n' +
        '\n' +
        '                            </div>\n' +
        '                        </div>\n' +
        '                    </div>\n' +
        '                    <div class="tab-pane fade" id="EC">\n' +
        '                        <div class="panel panel-default" style="margin-top: 10px">\n' +
        '                            <div class="panel-heading">\n' +
        '                                <h3 class="panel-title">首次评估及化验检查</h3>\n' +
        '                            </div>\n' +
        '                            <div class="panel-body">\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-6">意识 <input type="text"></div>\n' +
        '                                    <div class="col-md-6">(若评为昏迷进行评分)Glasgow评分 <input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-6">体征 <input type="text"></div>\n' +
        '                                    <div class="col-md-6">NIHSS评分：<input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-4">血糖(mmol/L)：<input type="text"></div>\n' +
        '                                    <div class="col-md-4">入院后首次血压(mmHg)：<input type="text"></div>\n' +
        '                                    <div class="col-md-4">血小板(10^9/L)：<input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-4">白细胞(10^9/L)：<input type="text"></div>\n' +
        '                                    <div class="col-md-4">红细胞(10^12/L)：<input type="text"></div>\n' +
        '                                    <div class="col-md-4">血红蛋白(g/L)：<input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-4">血脂： TG(mmol/L)：<input type="text"></div>\n' +
        '                                    <div class="col-md-4">谷丙转氨酶(U/L)：<input type="text"></div>\n' +
        '                                    <div class="col-md-4">谷草转氨酶(U/L)：<input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-4">尿素氮(mmol/L)：<input type="text"></div>\n' +
        '                                    <div class="col-md-4">血肌酐(umol/L)：<input type="text"></div>\n' +
        '                                    <div class="col-md-4">同型半胱氨酸HCY(μmol/L)：<input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-4">尿素氮(mmol/L)：<input type="text"></div>\n' +
        '                                    <div class="col-md-4">血肌酐(umol/L)：<input type="text"></div>\n' +
        '                                    <div class="col-md-4">同型半胱氨酸HCY(μmol/L)：<input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-4">超敏-C反应蛋白CRP(mg/L)：<input type="text"></div>\n' +
        '                                    <div class="col-md-4">CK(U/L)：<input type="text"></div>\n' +
        '                                    <div class="col-md-4">Lp-PLA₂(ng/ml)：<input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-3">CT： <input type="text"></div>\n' +
        '                                    <div class="col-md-3">MRI急性期改变：<input type="text"></div>\n' +
        '                                    <div class="col-md-3">心电监护：有无心房纤颤： <input type="text"></div>\n' +
        '                                    <div class="col-md-3">如果“有”，则为：<input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '                            </div>\n' +
        '                        </div>\n' +
        '                    </div>\n' +
        '                    <div class="tab-pane fade" id="ED">\n' +
        '                        <div class="panel panel-default" style="margin-top: 10px">\n' +
        '                            <div class="panel-heading">\n' +
        '                                <h3 class="panel-title">\n' +
        '                                    入院后治疗\n' +
        '                                </h3>\n' +
        '                            </div>\n' +
        '                            <div class="panel-body">\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-12"><strong>1.缺血性脑卒中</strong></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-12">1.1抗血小板聚集药物：<input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <br>\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-12">单抗 <br>\n' +
        '                                        <span>阿司匹林剂量(mg/天):</span><input type="text"><br>\n' +
        '                                        <span>氯吡格雷剂量(mg/天):</span><input type="text">\n' +
        '                                    </div>\n' +
        '                                </div>\n' +
        '                                <br>\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-12">双抗 <br>\n' +
        '                                        <span>阿司匹林剂量(mg/天):</span><input type="text"><br>\n' +
        '                                        <span>氯吡格雷剂量(mg/天):</span><input type="text">\n' +
        '                                    </div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-12">1.2.抗凝药物：<input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <br>\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-6">如果“是”，则为：药物<input type="text"></div>\n' +
        '                                    <div class="col-md-6">剂量(mg/天或iu)：<input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-12">1.3.调节血脂药物：<input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <br>\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-12">如果“是”，则为：药物<input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-12">1.4.控制血压药物：<input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <br>\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-12">如果“是”，则为：药物<input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-12">1.5.其他<input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <br>\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-6">中药：药物<input type="text"></div>\n' +
        '                                    <div class="col-md-6">脑保护：药物<input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <br>\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-6">脱水：药物<input type="text"></div>\n' +
        '                                    <div class="col-md-6">扩容：药物<input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <br>\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-12">控制血糖：药物<input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-12">1.6外科治疗：<input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-12">1.7介入治疗：<input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-12"><strong>2.出血性脑卒中</strong><input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-12">2.1脱水药物：<input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-12">2.2控制血压药物：<input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-12">2.3其他 <input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-12">2.4外科治疗：<input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-12">2.5介入治疗：<input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '\n' +
        '                            </div>\n' +
        '                        </div>\n' +
        '                    </div>\n' +
        '                    <div class="tab-pane fade" id="EE">\n' +
        '                        <div class="panel panel-default" style="margin-top: 10px">\n' +
        '                            <div class="panel-heading">\n' +
        '                                <h3 class="panel-title">\n' +
        '                                    危险因素\n' +
        '                                </h3>\n' +
        '                            </div>\n' +
        '                            <div class="panel-body">\n' +
        '                                <textarea rows="10" cols="118"></textarea>\n' +
        '                            </div>\n' +
        '                        </div>\n' +
        '                    </div>\n' +
        '                    <div class="tab-pane fade" id="EF">\n' +
        '                        <div class="panel panel-default" style="margin-top: 10px">\n' +
        '                            <div class="panel-heading">\n' +
        '                                <h3 class="panel-title">\n' +
        '                                    住院1周内病情变化\n' +
        '                                </h3>\n' +
        '                            </div>\n' +
        '                            <div class="panel-body">\n' +
        '                                <textarea rows="10" cols="118"></textarea>\n' +
        '                            </div>\n' +
        '                        </div>\n' +
        '                    </div>\n' +
        '                    <div class="tab-pane fade" id="EG">\n' +
        '                        <div class="panel panel-default" style="margin-top: 10px">\n' +
        '                            <div class="panel-heading">\n' +
        '                                <h3 class="panel-title">\n' +
        '                                    出院情况\n' +
        '                                </h3>\n' +
        '                            </div>\n' +
        '                            <div class="panel-body">\n' +
        '                                <textarea rows="10" cols="118"></textarea>\n' +
        '                            </div>\n' +
        '                        </div>\n' +
        '                    </div>\n' +
        '                    <div class="tab-pane fade" id="EH">\n' +
        '                        <div class="panel panel-default" style="margin-top: 10px">\n' +
        '                            <div class="panel-heading">\n' +
        '                                <h3 class="panel-title">\n' +
        '                                    出院诊断\n' +
        '                                </h3>\n' +
        '                            </div>\n' +
        '                            <div class="panel-body">\n' +
        '                                <textarea rows="10" cols="118"></textarea>\n' +
        '                            </div>\n' +
        '                        </div>\n' +
        '                    </div>\n' +
        '                    <div class="tab-pane fade" id="EI">\n' +
        '                        <div class="panel panel-default" style="margin-top: 10px">\n' +
        '                            <div class="panel-heading">\n' +
        '                                <h3 class="panel-title">\n' +
        '                                    住院时间\n' +
        '                                </h3>\n' +
        '                            </div>\n' +
        '                            <div class="panel-body">\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-6">住院时间（天）：<input type="text"></div>\n' +
        '                                    <div class="col-md-6">住院期间总花费（元）：<input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '                                <div class="row">\n' +
        '                                    <div class="col-md-6">其中药品花费（元）：<input type="text"></div>\n' +
        '                                    <div class="col-md-6">辅助检查花费（元）：<input type="text"></div>\n' +
        '                                </div>\n' +
        '                                <div class="hr-line-dashed"></div>\n' +
        '                            </div>\n' +
        '                        </div>\n' +
        '                    </div>\n' +
        '                </div>\n' +
        '            </div>\n' +
        '            <div class="modal-footer">\n' +
        '                <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>\n' +
        '                <button type="button" class="btn btn-primary" id="save">保存</button>\n' +
        '            </div>\n' +
        '        </div>\n' +
        '    </div>\n' +
        '</div>')

        $('body').append(alert);
        callback();
        alert.modal("show");
        // $('#save').click(function () {
        //     alert.modal("hide");
        // })
        $('#save').click(function(){
        var id = get_ids();
        var data = {};
        data['id'] = JSON.stringify(id);
        data['name'] = $('.ename').val();
        data['idnumble'] = $('.eidnumble').val();
        console.log(data);
        $.ajax({
            type: "POST",
            url: '/save_ssd/',
            data: data,
            datatype: "json",
            success: function(data){
                if(data == 'ok'){
                    alert.modal('hide');
                    window.location.href = '/backend/'
                }
            }
        })
    });
}


<!-- 展示确认框 -->
function show_confirm_alert(title,content,callback){
    alert = $('<div class="modal fade" data-backdrop="static" id="custom_alert" tabindex="-1" style="top:30%">' +
                '<div class="modal-dialog" style="width:300px">' +
                    '<div class="modal-content">' +
                        '<div class="modal-header">' +
                            '<button type="button" class="close" data-dismiss="modal">' +
                                '&times;' +
    '                       </button>' +
                            '<h4 class="modal-title">' +
                                title +
                            '</h4>' +
                        '</div>' +
                        '<div class="modal-body">' +
                            content+
                        '</div>' +
                        '<div class="modal-footer">' +
                            '<button type="button" class="btn btn-success" data-dismiss="modal" id="custom_alert_ok">' +
                                '确定' +
                            '</button>' +
                        '</div>' +
                     '</div>' +
                 '</div>' +
              '</div>');

    $('body').append(alert);
    alert.modal("show");
    $('#custom_alert_ok').click(function () {
        callback()
        alert.modal("hide");
    })
}