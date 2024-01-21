import { create } from "zustand";

export enum MessageType {
	Ticker = "TICKER",
	Trade = "TRADE",
}

export interface Data {
	status: string;
	message_type: MessageType;
	market_id: string;
	type: string;
}

export interface TickerData extends Data {
	timestamp: Date;
	price: number;
	ewma_s: number;
	ewma_f: number;
	balance: number;
}

export interface TradeData extends Data {
	price: number;
	amount: number;
	open_amount: number;
	side: "Bid" | "Ask";
	fiat_balance: number;
	order_id: string;
}

interface DataState {
	tickerData: TickerData[];
	tradeData: TradeData[];
	setTickerData: (newTickerData: TickerData) => void;
	webSocket: WebSocket | null;
	setWebSocket: (ws: WebSocket) => void;
}

export const useDataStore = create<DataState>((set) => ({
	tickerData: [],
	setTickerData: (newTickerData: TickerData) =>
		set((state) => ({ tickerData: [...state.tickerData, newTickerData] })),
	tradeData: [],
	setTradeData: (newTradeData: TradeData) =>
		set((state) => ({ tradeData: [...state.tradeData, newTradeData] })),
	webSocket: null,
	setWebSocket: (ws) => set({ webSocket: ws }),
}));
