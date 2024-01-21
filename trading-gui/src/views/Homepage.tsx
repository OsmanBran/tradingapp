import React, { useEffect } from "react";
import TickerChart from "../components/TickerChart";
import ProfitLoss from "../components/ProfitLoss";
import classes from "./Homepage.module.css";
import TradeHistory from "../components/TradeHistory";
import { Data, MessageType, useDataStore } from "../store/useDataStore";
import { Container } from "@mui/material";
import Grid from "@mui/material/Unstable_Grid2"; // Grid version 2

const Homepage = () => {
	const { tickerData, setTickerData, setWebSocket, setTradeData } = useDataStore();

 
	useEffect(() => {
		const ws = new WebSocket("ws://localhost:8765/");

		ws.onopen = () => console.log("WebSocket Connected");

		ws.onmessage = (event) => {
			const data: Data = JSON.parse(event.data);
			// Assuming the data is already in the format of TickerData
			console.log("WEB SOCKET DATA!!", data);

			if (data.message_type === MessageType.Ticker) {
				setTickerData(data);
			} else if (data.message_type === MessageType.Trade) {
				setTradeData(data);
			}
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
				<TickerChart />
				Render your ticker data here
				{tickerData.map(
					(data: unknown, index: React.Key | null | undefined) => (
						<p key={index}>Ticker Data: {JSON.stringify(data)}</p>
					)
				)}
				<TradeHistory />
			</Grid>
		</Container>
	);
};

export default Homepage;
