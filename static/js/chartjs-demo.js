$(function () {

    var lineData = {
        labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [

            {
                label: "Data 1",
                backgroundColor: 'rgba(26,179,148,0.5)',
                borderColor: "rgba(26,179,148,0.7)",
                pointBackgroundColor: "rgba(26,179,148,1)",
                pointBorderColor: "#fff",
                data: [28, 48, 40, 19, 86, 27, 90]
            },{
                label: "Data 2",
                backgroundColor: 'rgba(220, 220, 220, 0.5)',
                pointBorderColor: "#fff",
                data: [65, 59, 80, 81, 56, 55, 40]
            }
        ]
    };

    var lineOptions = {
        responsive: true
    };


    // var ctx = document.getElementById("lineChart").getContext("2d");
    // new Chart(ctx, {type: 'line', data: lineData, options:lineOptions});

    var barData = {
        labels: ["1.1.1.1", "1.1.1.2", "1.1.1.3", "1.1.1.4", "1.1.1.5", "1.1.1.6", "1.1.1.7"],
        datasets: [
            {
                label: "APP数量",
                backgroundColor: 'rgba(26,179,148,0.5)',
                pointBorderColor: "#fff",
                data: [10, 9, 8, 7, 6, 5, 4, 3]
            },
            // {
            //     label: "Data 2",
            //     backgroundColor: 'rgba(220, 220, 220, 0.5)',
            //     borderColor: "rgba(26,179,148,0.7)",
            //     pointBackgroundColor: "rgba(26,179,148,1)",
            //     pointBorderColor: "#fff",
            //     data: [28, 48, 40, 19, 86, 27, 90]
            // }
        ]
    };

    var barOptions = {
        responsive: true
    };


    var ctx2 = document.getElementById("barChart").getContext("2d");
    new Chart(ctx2, {type: 'bar', data: barData, options:barOptions});

    var polarData = {
        datasets: [{
            data: [
                300,140,200
            ],
            backgroundColor: [
                "#a3e1d4", "#dedede", "#b5b8cf"
            ],
            label: [
                "My Radar chart"
            ]
        }],
        labels: [
            "App","Software","Laptop"
        ]
    };

    var polarOptions = {
        segmentStrokeWidth: 2,
        responsive: true

    };

    // var ctx3 = document.getElementById("polarChart").getContext("2d");
    // new Chart(ctx3, {type: 'polarArea', data: polarData, options:polarOptions});

    var doughnutData = {
        labels: ["ECS","SLB","Redis","OSS"],
        datasets: [{
            data: [240,50,30,10],
            backgroundColor: ["#a3e1d4","#dedede","#b5b8cf","#0080FF"]
        }]
    } ;


    var doughnutOptions = {
        responsive: true
    };


    var ctx4 = document.getElementById("doughnutChart").getContext("2d");
    new Chart(ctx4, {type: 'doughnut', data: doughnutData, options:doughnutOptions});


    var radarData = {
        labels: ["Eating", "Drinking", "Sleeping", "Designing", "Coding", "Cycling", "Running"],
        datasets: [
            {
                label: "My First dataset",
                backgroundColor: "rgba(220,220,220,0.2)",
                borderColor: "rgba(220,220,220,1)",
                data: [65, 59, 90, 81, 56, 55, 40]
            },
            {
                label: "My Second dataset",
                backgroundColor: "rgba(26,179,148,0.2)",
                borderColor: "rgba(26,179,148,1)",
                data: [28, 48, 40, 19, 96, 27, 100]
            }
        ]
    };

    var radarOptions = {
        responsive: true
    };

    // var ctx5 = document.getElementById("radarChart").getContext("2d");
    // new Chart(ctx5, {type: 'radar', data: radarData, options:radarOptions});

});