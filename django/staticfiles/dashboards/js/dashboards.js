// data
var data0 = JSON.parse(document.getElementById('data0').textContent);
var data1 = JSON.parse(document.getElementById('data1').textContent);
var index = JSON.parse(document.getElementById('index').textContent);

var ctx = document.getElementById("main-js-chart").getContext("2d");
var data = {
labels: index,
datasets: [{
    label: document.currentScript.getAttribute('label1'),
    borderColor: '#000000',
    fill: false,
    pointStyle: 'dot',
    borderWidth: 2,
    pointRadius: (ctx) => {
        const pointsLenght = ctx.chart.data.labels.length -1;
        const pointsArray = [];
        for (let i=0; i<=pointsLenght; i++) {
        if (i == pointsLenght | i == 0) {
            pointsArray.push(3.5);
        }
        else {
            pointsArray.push(0);
        }
        }
        return pointsArray;
    },
    data: data0
    },
    {
    label: document.currentScript.getAttribute('label2'),
    borderColor: '#4ab78f',
    pointStyle: 'dot',
    fill: false,
    borderWidth: 2,
    pointRadius: (ctx) => {
        const pointsLenght = ctx.chart.data.labels.length -1;
        const pointsArray = [];
        for (let i=0; i<=pointsLenght; i++) {
        if (i == pointsLenght | i == 0) {
            pointsArray.push(3.5);
        }
        else {
            pointsArray.push(0);
        }
        }
        return pointsArray;
    },
    data: data1
    }
]
};


var options = {
responsive: true,
maintainAspectRatio: false,
legend: {
    labels : {
        usePointStyle: true
    }
},
hover: {
    intersect: false
},
tooltips: {
    mode: 'nearest',
    custom: function(tooltip) {
    if (!tooltip) return;
        tooltip.displayColors = false;
    }
},
scales: {
    xAxes: [{
        gridLines: {
            display:false
        }
    }]
    }
}

var chart = new Chart(ctx, {
    type: "line",
    data: data,
    options: options,
});

function UpdatesSlider(range) {
    var il = document.getElementById('input-left').value;
    var ir = document.getElementById('input-right').value;
    var abs_il = Math.ceil(data0.length * il / 100);
    var abs_ir = Math.ceil(data0.length * ir / 100);
    chart.data.labels = index.slice(abs_il, abs_ir);
    chart.data.datasets[0].data = data0.slice(abs_il, abs_ir);
    chart.data.datasets[1].data = data1.slice(abs_il, abs_ir);
    chart.update();
    console.log(abs_il, abs_ir);
};
