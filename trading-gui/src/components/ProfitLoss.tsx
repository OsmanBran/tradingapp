import React, { useEffect, useState } from "react";
import Grid from "@mui/material/Unstable_Grid2"; // Grid version 2
import CurrencyExchangeOutlinedIcon from "@mui/icons-material/CurrencyExchangeOutlined";
import AppWidgetSummary from "./elements/AppWidgetSummary";
import { useDataStore } from "../store/useDataStore";
import dayjs from "dayjs";
import duration from "dayjs/plugin/duration";
dayjs.extend(duration);

const ProfitLoss = () => {
	const { tradeData } = useDataStore();

	const [currentBalance, setCurrentBalance] = useState(0);
	const [profitLoss, setProfitLoss] = useState(0);
	const [runningTime, setRunningTime] = useState(0);

	const getStartingCapital = tradeData[0]?.fiat_qty;
	const startingCapital: number = getStartingCapital ? getStartingCapital : 5000;

	useEffect(() => {
		const intervalId = setInterval(() => {
			setRunningTime((runningTime) => runningTime + 1);
		}, 1000); // Update every second

		const getCurrentBalance =
			tradeData[tradeData.length - 1]?.total_notional;

		setCurrentBalance(
			getCurrentBalance ? getCurrentBalance : startingCapital
		);

		console.log("CURRENT BVALANCE VS STARTING CAP", currentBalance, startingCapital);
		setProfitLoss(currentBalance - startingCapital);

		return () => {
			clearInterval(intervalId);
		};
	}, [tradeData, currentBalance]);

	return (
		<>
			<Grid xs={12} sm={6} md={3}>
				<AppWidgetSummary
					title="Starting Capital"
					// total={'$' + startingCapital.toFixed(2)}
					total={"$" + startingCapital?.toFixed(2)}
				/>
			</Grid>
			<Grid xs={12} sm={6} md={3}>
				<AppWidgetSummary
					title="Current Balance"
					total={"$" + currentBalance?.toFixed(2)}
				/>
			</Grid>
			<Grid xs={12} sm={6} md={3}>
				<AppWidgetSummary
					title="Profit/Loss"
					total={"$" + profitLoss.toFixed(3)}
				/>
			</Grid>
			<Grid xs={12} sm={6} md={3}>
				<AppWidgetSummary
					title="Time Running"
					total={dayjs
						.duration(runningTime, "seconds")
						.format("H[h] m[m] s[s]")}
				/>
			</Grid>
		</>
	);
};

export default ProfitLoss;
