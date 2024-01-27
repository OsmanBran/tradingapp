import {
	Box,
	Card,
	CardHeader,
	Paper,
	Table,
	TableCell,
	TableHead,
	TableRow,
} from "@mui/material";
import React from "react";
import { useDataStore } from "../store/useDataStore";
import TableBody from "@mui/material/TableBody";
import TableContainer from "@mui/material/TableContainer";

const TradeHistory = () => {
	const { tradeData } = useDataStore();

	return (
		<Card sx={{mb: 2}}>
			<CardHeader title={"Trade History"} sx={{ mb: 0, pb: 0 }} />
			<Box sx={{ p: 3, pb: 1 }}>
				<TableContainer component={Paper} sx={{ maxHeight: '500px'}}>
					<Table sx={{ minWidth: 650 }} aria-label="simple table" stickyHeader>
						<TableHead>
							<TableRow>
								<TableCell>Type</TableCell>
								<TableCell>Status</TableCell>
								<TableCell>Side</TableCell>
								<TableCell>Price</TableCell>
								<TableCell>Amount</TableCell>
								<TableCell>Fiat Qty</TableCell>
								<TableCell>Notional Change</TableCell>
								<TableCell>Total Notional</TableCell>
							</TableRow>
						</TableHead>
						<TableBody sx={{overflow: 'auto'}}>
							{tradeData.map((trade, index) => (
								<TableRow key={index}>
									<TableCell>{trade.type}</TableCell>
									<TableCell>{trade.status}</TableCell>
									<TableCell>{trade.side}</TableCell>
									<TableCell>{trade.price}</TableCell>
									<TableCell>{trade.amount}</TableCell>
									<TableCell>{trade.fiat_qty}</TableCell>
									<TableCell>
										{trade.notional_change}
									</TableCell>
									<TableCell>
										{trade.total_notional}
									</TableCell>
								</TableRow>
							))}
						</TableBody>
					</Table>
				</TableContainer>
			</Box>
		</Card>
	);
};

export default TradeHistory;
