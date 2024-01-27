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
import { Box, Card, CardHeader, Grid, Paper } from "@mui/material";

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

	const chartData = {
		labels: data.map((_, i) => i), // Assuming 'index' is just the index of the data array
		datasets: [
			{
				label: "BitcoinPrice",
				data: data.map((item) => item.BitcoinPrice),
				borderColor: "#8884d8",
				fill: true,
				pointRadius: 0,
				tension: 0.4,
			},
			{
				label: "FMA",
				data: data.map((item) => item.FMA),
				borderColor: "#82ca9d",
				fill: false,
				pointRadius: 0,
				tension: 0.4,
			},
			{
				label: "SMA",
				data: data.map((item) => item.SMA),
				borderColor: "#ff7300",
				fill: false,
				pointRadius: 0,
				tension: 0.4,
			},
		],
	};

	const chartOptions = {
		responsive: true,
		scales: {
			y: {
				min: tickerData[0]?.price - 500,
				max: tickerData[0]?.price + 500,
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
		<Card elevation={0}>
			<CardHeader title="Bitcoin Price" style={{ paddingBottom: 0 }} />
			<Box sx={{ p: 3, pb: 1 }}>
				<Line data={chartData} options={chartOptions} />;
			</Box>
		</Card>
	);
};

export default TickerChart;
