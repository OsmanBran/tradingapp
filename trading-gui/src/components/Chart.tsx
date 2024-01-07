import React from "react";
import classes from "./Chart.module.css";
import {
	LineChart,
	Line,
	CartesianGrid,
	XAxis,
	YAxis,
	Tooltip,
	ResponsiveContainer,
	Brush,
} from "recharts";
import CustomDot from "./elements/CustomDot";
import { TickerData, useTickerDataStore } from "../store/useTickerDataStore";

interface DataPoint {
	index: number;
	BitcoinPrice: number;
	FMA?: number; // Fast Moving Average (optional)
	SMA?: number; // Slow Moving Average (optional)
}

const Chart = () => {
	const data: DataPoint[] = []
	// const {tickerData} = useTickerDataStore();
	// const data: DataPoint[] = tickerData.map((ticker: TickerData, index: number) => ({
	// 	index: ticker.timestamp,  // Or any other logic to generate index
	// 	BitcoinPrice: ticker.price,
	// 	// Assuming FMA and SMA are derived from ewma_s and ewma_f:
	// 	FMA: ticker?.ewma_f, // Map according to your logic
	// 	SMA: ticker?.ewma_s, // Map according to your logic
	// 	// If FMA and SMA are not directly from ewma_s and ewma_f, you will need additional logic to calculate them
	// }));


	const fmaPeriod = 5; // Fast moving average period
	const smaPeriod = 20; // Slow moving average period

	let bitcoinPrice = 1000;
	for (let i = 1000, index = 1; i <= 10000; i += 50, index++) {
		// Add Bitcoin price
		const fluctuation = Math.random() > 0.5 ? 1 : -1; // Random upward or downward fluctuation
		bitcoinPrice += fluctuation * Math.floor(Math.random() * 100); // Adjust the fluctuation range as needed

		const newDataPoint: DataPoint = { index, BitcoinPrice: bitcoinPrice };

		// Calculate Fast Moving Average
		if (index >= fmaPeriod) {
			const fmaStartIndex = index - fmaPeriod;
			const fmaPrices = data
				.slice(fmaStartIndex, index)
				.map((p) => p.BitcoinPrice);
			const fma = fmaPrices.reduce((a, b) => a + b, 0) / fmaPrices.length;
			newDataPoint.FMA = fma;
		}

		// Calculate Slow Moving Average
		if (index >= smaPeriod) {
			const smaStartIndex = index - smaPeriod;
			const smaPrices = data
				.slice(smaStartIndex, index)
				.map((p) => p.BitcoinPrice);
			const sma = smaPrices.reduce((a, b) => a + b, 0) / smaPrices.length;
			newDataPoint.SMA = sma;
		}

		data.push(newDataPoint);
	}

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

	return (
		<div className={classes.chartContainer}>
			<div>Bitcoin Price Chart</div>
			<ResponsiveContainer width='100%' height={500}>
				<LineChart
					data={data}
					margin={{ top: 5, right: 0, bottom: 5, left: 0 }}>
					<Line
						type="monotone"
						dataKey="BitcoinPrice"
						stroke="#8884d8"
						dot={false}
						activeDot={{ r: 8 }}
					/>
					<Line
						type="monotone"
						dataKey="FMA"
						stroke="#82ca9d"
						dot={(props) => (
							<CustomDot
								{...props}
								index={props.index}
								intersections={intersections}
							/>
						)}
					/>
					<Line
						type="monotone"
						dataKey="SMA"
						stroke="#ff7300"
						dot={(props) => (
							<CustomDot
								{...props}
								index={props.index}
								intersections={intersections}
							/>
						)}
					/>
					{/* <CartesianGrid stroke="#ccc" /> */}
					<XAxis dataKey="index" />
					{/* <YAxis domain={[63000, 68000]} /> */}
					<Tooltip />
					<Brush dataKey="name" height={30} stroke="#8884d8" />
				</LineChart>
			</ResponsiveContainer>
		</div>
	);
};

export default Chart;
