window.addEventListener('load', async (event) => {

    // line chart

    let logCount = await fetchChartData("/logs/chart/log-count");
    logCount = await logCount.log_count || null;

    const headings = logCount.map(function (l) { return l.name });

    drawLineChart(
        'line-chart',
        data = logCount,
        title = 'Log count',
        subtitle = null,
        xAxisTitle = 'Timestamp',
        yAxisTitle = 'Log Count',
        xLabels = headings,
    );

    // end: line chart


    // *********************


    // category pie chart
    let categories = await fetchChartData("/logs/chart/category");
    categories = categories.categories || null;


    drawPieChart(
        'pie-chart',
        data = categories,
        title = "Category wise log count",
        dataLabelsEnabled = false,
    );

});
// end: window.addEventListener



async function fetchChartData(url) {
    try {
        const resp = await fetch(url);
        const respJSON = await resp.json();
        return respJSON;
    } catch (err) {
        console.log("Error while fetching data: ", err);
        return null;
    }
}



function drawLineChart(id, data, title = null, subtitle = null,
    xAxisTitle = null, yAxisTitle = null, xLabels = null) {
    Highcharts.chart(id, {
        chart: {
            type: 'line',
            zoomType: 'x',
        },

        credits: {
            enabled: false,
        },

        title: {
            text: title
        },

        subtitle: {
            text: subtitle
        },

        xAxis: {
            categories: xLabels,
        },

        yAxis: {
            title: {
                text: yAxisTitle
            }
        },

        series: [{
            name: xAxisTitle,
            // chart data
            data
        },
        ],
    });
}
// end: drawLineChart






function drawPieChart(
    elementId,
    data,
    title = null,
    dataLabelsEnabled = true,
) {
    Highcharts.chart(elementId, {
        chart: {
            type: 'pie',
            backgroundColor: '#f1f7ff',
        },

        credits: {
            enabled: false,
        },

        title: {
            text: title,
        },

        tooltip: {
            pointFormat: '{series.name}: <b>{point.y}</b>'
        },

        plotOptions: {
            pie: {
                allowPointSelect: false,
                cursor: 'pointer',
                dataLabels: {
                    enabled: dataLabelsEnabled,
                    format: '<b>{point.name}</b><br>[{point.y}]'
                }
            }
        },

        series: [{
            name: 'Number of Logs',
            colorByPoint: true,

            // chart data
            data,
        }]
    });
}
    // end: drawPieChart

