import React from "react";
import classes from "./TickerChart.module.css";
import { TickerData, useDataStore } from "../store/useDataStore";
import {
	Chart as ChartJS,
	CategoryScale,
	LinearScale,
	PointElement,
	LineElement,
	Title,
	Tooltip,
	Legend,
} from "chart.js";
import { Line } from "react-chartjs-2";

ChartJS.register(
	CategoryScale,
	LinearScale,
	PointElement,
	LineElement,
	Title,
	Tooltip,
	Legend
);

interface DataPoint {
	index: number;
	BitcoinPrice: number;
	FMA?: number; // Fast Moving Average (optional)
	SMA?: number; // Slow Moving Average (optional)
}

const TickerChart = () => {
	// const data: DataPoint[] = []

	const { tickerData } = useDataStore();
	console.log("TICKER DATA!!", tickerData);
	const data: DataPoint[] = tickerData.map(
		(ticker: TickerData, index: number) => ({
			index: index, // Or any other logic to generate index
			BitcoinPrice: ticker.price,
			// Assuming FMA and SMA are derived from ewma_s and ewma_f:
			FMA: ticker?.ewma_f, // Map according to your logic
			SMA: ticker?.ewma_s, // Map according to your logic
			// If FMA and SMA are not directly from ewma_s and ewma_f, you will need additional logic to calculate them
		})
	);

	// const fmaPeriod = 5; // Fast moving average period
	// const smaPeriod = 20; // Slow moving average period

	// let bitcoinPrice = 1000;
	// for (let i = 1000, index = 1; i <= 10000; i += 50, index++) {
	// 	// Add Bitcoin price
	// 	const fluctuation = Math.random() > 0.5 ? 1 : -1; // Random upward or downward fluctuation
	// 	bitcoinPrice += fluctuation * Math.floor(Math.random() * 100); // Adjust the fluctuation range as needed

	// 	const newDataPoint: DataPoint = { index, BitcoinPrice: bitcoinPrice };

	// 	// Calculate Fast Moving Average
	// 	if (index >= fmaPeriod) {
	// 		const fmaStartIndex = index - fmaPeriod;
	// 		const fmaPrices = data
	// 			.slice(fmaStartIndex, index)
	// 			.map((p) => p.BitcoinPrice);
	// 		const fma = fmaPrices.reduce((a, b) => a + b, 0) / fmaPrices.length;
	// 		newDataPoint.FMA = fma;
	// 	}

	// 	// Calculate Slow Moving Average
	// 	if (index >= smaPeriod) {
	// 		const smaStartIndex = index - smaPeriod;
	// 		const smaPrices = data
	// 			.slice(smaStartIndex, index)
	// 			.map((p) => p.BitcoinPrice);
	// 		const sma = smaPrices.reduce((a, b) => a + b, 0) / smaPrices.length;
	// 		newDataPoint.SMA = sma;
	// 	}

	// 	data.push(newDataPoint);
	// }

	let lastFMA = data[0]?.FMA || 0;
	let lastSMA = data[0]?.SMA || 0;
	const intersections: number[] = [];

	data.forEach((point, index) => {
		if (point?.FMA && point?.SMA) {
			if (
				(lastFMA <= lastSMA && point.FMA > point.SMA) ||
				(lastFMA >= lastSMA && point.FMA < point.SMA)
			) {
				intersections.push(index);
			}
			lastFMA = point.FMA;
			lastSMA = point.SMA;
		}
	});

	console.log("CHART DATA!!", data);

	const chartData = {
		labels: data.map((_, i) => i), // Assuming 'index' is just the index of the data array
		datasets: [
			{
				label: "BitcoinPrice",
				data: data.map((item) => item.BitcoinPrice),
				borderColor: "#8884d8",
				fill: true,
			},
			{
				label: "FMA",
				data: data.map((item) => item.FMA),
				borderColor: "#82ca9d",
				fill: false,
			},
			{
				label: "SMA",
				data: data.map((item) => item.SMA),
				borderColor: "#ff7300",
				fill: false,
			},
		],
	};

	const chartOptions = {
		responsive: true,
		scales: {
			y: {
				min: 62500,
				max: 63500,
			},
		},
		interaction: {
			intersect: false,
			mode: "index" as const,
		},
		plugins: {
			tooltip: {
				enabled: true,
			},
		},
	};

	return (
		<div className={classes.chartContainer}>
			<div>Bitcoin Price Chart</div>
			<Line data={chartData} options={chartOptions} />;
		</div>
	);
};

export default TickerChart;
