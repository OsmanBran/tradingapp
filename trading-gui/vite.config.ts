import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";

// https://vitejs.dev/config/
export default defineConfig({
	plugins: [react()],
	optimizeDeps: {
		include: ["@mui/material/Unstable_Grid2"],
	},
	server: {
		watch: {
			usePolling: true,
		},
	},
});
