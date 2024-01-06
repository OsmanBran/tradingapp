import React, { useEffect } from "react";
import Chart from "../components/Chart";
import ProfitLoss from "../components/ProfitLoss";
import classes from "./Homepage.module.css";
import TradeHistory from "../components/TradeHistory";
import { useTickerDataStore } from "../store/useTickerDataStore";

const Homepage = () => {
	const { tickerData, setTickerData, setWebSocket } = useTickerDataStore();

	useEffect(() => {
		const ws = new WebSocket("ws://192.168.1.121:8765");

		ws.onopen = () => console.log("WebSocket Connected");

		ws.onmessage = (event) => {
			const data = JSON.parse(event.data);
			// Assuming the data is already in the format of TickerData
			if (data.type === "ticker") {
				setTickerData(data);
			}
		};

		ws.onerror = (error) => console.error("WebSocket Error: ", error);

		ws.onclose = () => console.log("WebSocket Disconnected");

		setWebSocket(ws);

		return () => ws.close();
	}, [setTickerData, setWebSocket]);

	return (
		<>
			<div className={classes.graphPnLContainer}>
				<Chart />
				<ProfitLoss />
			</div>
			{/* Render your ticker data here */}
			{tickerData.map((data: unknown, index: React.Key | null | undefined) => (
				<p key={index}>Ticker Data: {JSON.stringify(data)}</p>
			))}
			<TradeHistory />
		</>
	);
};

export default Homepage;
