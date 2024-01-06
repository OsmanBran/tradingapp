import React from 'react'
import classes from './ProfitLoss.module.css'
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@material-ui/core';

const ProfitLoss = () => {
  return (
    <div className={classes.profitLossContainer}>
        <div>P&L Sheet</div>
        <TableContainer component={Paper}>
            <Table aria-label="simple table">
                <TableHead>
                    <TableRow>
                        <TableCell align="left">Description</TableCell>
                        <TableCell align="right">Value</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    <TableRow>
                        <TableCell component="th" scope="row">Starting Capital</TableCell>
                        <TableCell align="right">{/* Value Here */}</TableCell>
                    </TableRow>
                    <TableRow>
                        <TableCell component="th" scope="row">Current Balance</TableCell>
                        <TableCell align="right">{/* Value Here */}</TableCell>
                    </TableRow>
                    <TableRow>
                        <TableCell component="th" scope="row">Profit/Loss</TableCell>
                        <TableCell align="right">{/* Value Here */}</TableCell>
                    </TableRow>
                    <TableRow>
                        <TableCell component="th" scope="row">Timer</TableCell>
                        <TableCell align="right">{/* Value Here */}</TableCell>
                    </TableRow>
                </TableBody>
            </Table>
        </TableContainer>
    </div>
  )
}

export default ProfitLoss