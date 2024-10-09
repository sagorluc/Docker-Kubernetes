import { useState } from "react";
import ReactApexChart from "react-apexcharts";

const DashboardLanding = () => {
    const [state, setState] = useState({
        series: [
            {
                name: "series1",
                data: [31, 40, 28, 51, 42, 109, 100],
            },
            {
                name: "series2",
                data: [11, 32, 45, 32, 34, 52, 41],
            },
        ],
        options: {
            chart: {
                type: "area",
                height: '80%', 
                width: '80%',  
                responsive: [
                    {
                        breakpoint: 1000, 
                        options: {
                            chart: {
                                width: '80%',
                                height: '400px',
                            }
                        }
                    }
                ]
            },
            dataLabels: {
                enabled: false,
            },
            stroke: {
                curve: "smooth",
            },
            xaxis: {
                type: "datetime",
                categories: [
                    "2018-09-19T00:00:00.000Z",
                    "2018-09-19T01:30:00.000Z",
                    "2018-09-19T02:30:00.000Z",
                    "2018-09-19T03:30:00.000Z",
                    "2018-09-19T04:30:00.000Z",
                    "2018-09-19T05:30:00.000Z",
                    "2018-09-19T06:30:00.000Z",
                ],
            },
            tooltip: {
                x: {
                    format: "dd/MM/yy HH:mm",
                },
            },
        },
    });


    return (
        <div className="w-full h-full">
            <div id="chart" className="w-[700px] mx-auto">
                <ReactApexChart
                    options={state.options}
                    series={state.series}
                    type="area"
                    // height="80%"
                    width="100%"
                    margin='auto'
                    
                />
            </div>
        </div>
    );
};

export default DashboardLanding;
