import React from "react";
import classes from "./ProfitLoss.module.css";
import { Box, Paper } from "@material-ui/core";
import Grid from "@mui/material/Unstable_Grid2"; // Grid version 2
import { Stack } from "@mui/system";
import CurrencyExchangeOutlinedIcon from "@mui/icons-material/CurrencyExchangeOutlined";

const ProfitLoss = () => {
	return (
		<>
			<Grid container spacing={2} width={"100%"}>
				<Grid xs={12} sm={6} md={3}>
					<Paper className={classes.pnlPaperContainer}>
						<Box className={classes.imgContainer}>
							<CurrencyExchangeOutlinedIcon />
						</Box>
						<Stack marginLeft={"1.5rem"} direction={"column"}>
							<h4 className={classes.valueText}> $1000 </h4>
							<h6 className={classes.subText}>
								Starting Capital
							</h6>
						</Stack>
					</Paper>
				</Grid>
				<Grid xs={12} sm={6} md={3}>
					<Paper className={classes.pnlPaperContainer}>
						<Box className={classes.imgContainer}>
							<CurrencyExchangeOutlinedIcon />
						</Box>
						<Stack>
							{" "}
							<h4 className={classes.valueText}> $1000 </h4>
							<h6 className={classes.subText}>Current Balance</h6>
						</Stack>
					</Paper>
				</Grid>
				<Grid xs={12} sm={6} md={3}>
					<Paper className={classes.pnlPaperContainer}>
						<Box className={classes.imgContainer}>
							<CurrencyExchangeOutlinedIcon />
						</Box>
						<Stack marginLeft={"1.5rem"} direction={"column"}>
							<h4 className={classes.valueText}> $1000 </h4>
							<h6 className={classes.subText}>Profit/Loss</h6>
						</Stack>
					</Paper>
				</Grid>
				<Grid xs={12} sm={6} md={3}>
					<Paper className={classes.pnlPaperContainer}>
						<Box className={classes.imgContainer}>
							<CurrencyExchangeOutlinedIcon />
						</Box>
						<Stack marginLeft={"1.5rem"} direction={"column"}>
							<h4 className={classes.valueText}> $1000 </h4>
							<h6 className={classes.subText}>Timer</h6>
						</Stack>
					</Paper>
				</Grid>
			</Grid>
		</>
	);
};

export default ProfitLoss;
