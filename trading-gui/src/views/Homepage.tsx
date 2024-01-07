import React, { useEffect } from "react";
import Chart from "../components/Chart";
import ProfitLoss from "../components/ProfitLoss";
import classes from "./Homepage.module.css";
import TradeHistory from "../components/TradeHistory";
import { useTickerDataStore } from "../store/useTickerDataStore";
import { Container } from "@material-ui/core";
import Grid from "@mui/material/Unstable_Grid2"; // Grid version 2

const Homepage = () => {
	const { tickerData, setTickerData, setWebSocket } = useTickerDataStore();

	useEffect(() => {
		const ws = new WebSocket("ws://192.168.1.121:8765");

		ws.onopen = () => console.log("WebSocket Connected");

		ws.onmessage = (event) => {
			const data = JSON.parse(event.data);
			// Assuming the data is already in the format of TickerData
			console.log("WEB SOCKET DATA!!", data);

			setTickerData(data);
		};

		ws.onerror = (error) => console.error("WebSocket Error: ", error);

		ws.onclose = () => console.log("WebSocket Disconnected");

		setWebSocket(ws);

		return () => ws.close();
	}, []);

	return (
		<Container>
			<Grid container spacing={2} direction={"row"}>
				<ProfitLoss />
				<Chart />
				{/* Render your ticker data here
				{tickerData.map(
					(data: unknown, index: React.Key | null | undefined) => (
						<p key={index}>Ticker Data: {JSON.stringify(data)}</p>
					)
				)} */}
				<TradeHistory />
			</Grid>
		</Container>
	);
};

export default Homepage;
