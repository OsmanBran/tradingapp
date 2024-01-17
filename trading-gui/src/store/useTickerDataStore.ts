import { create } from "zustand";

export interface TickerData {
    timestamp: Date,
    price: number,
    ewma_s: number,
    ewma_f: number,
    balance: number,
    trade: unknown
}

interface TickerDataState {
  tickerData: TickerData[];
  setTickerData: (newData: TickerData) => void;
  webSocket: WebSocket | null;
  setWebSocket: (ws: WebSocket) => void;
}

export const useTickerDataStore = create<TickerDataState>((set) => ({
  tickerData: [],
  setTickerData: (newTickerData: TickerData) =>
    set((state) => ({ tickerData: [...state.tickerData, newTickerData] })),
  webSocket: null,
  setWebSocket: (ws) => set({ webSocket: ws }),
}));