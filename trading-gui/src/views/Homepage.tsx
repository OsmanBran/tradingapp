import React, { useEffect } from "react";
import TickerChart from "../components/TickerChart";
import ProfitLoss from "../components/ProfitLoss";
import classes from "./Homepage.module.css";
import TradeHistory from "../components/TradeHistory";
import {
	Data,
	MessageType,
	TickerData,
	TradeData,
	useDataStore,
} from "../store/useDataStore";
import { Container } from "@mui/material";
import Grid from "@mui/material/Unstable_Grid2"; // Grid version 2

const Homepage = () => {
	const { setTickerData, setWebSocket, setTradeData } = useDataStore();

	useEffect(() => {
		const ws = new WebSocket("ws://localhost:8765/");

		ws.onopen = () => console.log("WebSocket Connected");

		ws.onmessage = (event) => {
			const data: Data = JSON.parse(event.data);
			// Assuming the data is already in the format of TickerData

			console.log("INCOMING DATA OBJECT", data);
			if (data.message_type === MessageType.Ticker) {
				setTickerData(data as TickerData);
			} else if (data.message_type === MessageType.Trade) {
				setTradeData(data as TradeData);
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
				<Grid xs={12} md={12} lg={12} className={classes.chartContainer}>
					<TickerChart />
				</Grid>
				<Grid xs={12} md={12} lg={12}>
					<TradeHistory />
				</Grid>
			</Grid>
		</Container>
	);
};

export default Homepage;
