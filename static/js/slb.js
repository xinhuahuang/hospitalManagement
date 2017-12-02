$(document).ready(function () {
    $(document).ready(function(){
        var canvas = document.getElementById('canvas');
        var stage = new JTopo.Stage(canvas);
        var scene = new JTopo.Scene(stage);
        // scene.backgroundColor = '0,0,0';
        scene.alpha = 0;

        function node(x, y, name,img,postion){
            var node = new JTopo.Node(name);
            node.fillColor = '128, 128, 128'; //节点背景色 只支持rgb格式
            node.zIndex = 12;
            node.font = '12px';
            node.fontColor = '0,0,0';
            node.textPosition = postion;
            node.setImage(img);
            node.setLocation(x, y);
            scene.add(node);
            return node;
        }

        function linkNode(nodeA, nodeZ){
            var link = new JTopo.Link(nodeA, nodeZ);
            link.lineWidth = 1; //线宽
            link.bundleOffset = 60; //折线拐角的长度
            link.bundleGap = 5; //线条之间的间隔
            link.zIndex=11;
            link.strokeColor = JTopo.util.randomColor(); //设置线条颜色 随机色
            scene.add(link);
            return link;
        }

        function textNode(text,x,y){
                var textNode = new JTopo.TextNode(text);
                textNode.font = 'bold 12px 微软雅黑';
                textNode.fontColor = '0,0,0';
                textNode.setLocation(x, y);
                scene.add(textNode);
            }


        var slb = node(100, 200, 'SLB','/static/slb.png','Top_Center');
        var app = node(300, 160, 'APP','/static/app.png','Top_Center');
        var callapp = node(300, 260, '调用APP','/static/app.png','Bottom_Center');
        var ecs = node(500,200,'ECS','/static/ecs.png','Top_Center');


        linkNode(slb,app);
        linkNode(app,ecs);
        linkNode(app,callapp);

        textNode('负载均衡层',100,100);
        textNode('APP',300,100);
        textNode('ECS',500,100);
        textNode(2,112,235); // slb数量
        textNode(1,331,155); //app数量
        textNode(4,336,268); //调用app数量
        textNode(5,513,232); //ecs数量
    });
});