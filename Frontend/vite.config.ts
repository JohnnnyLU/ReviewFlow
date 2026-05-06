import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";
import { fileURLToPath, URL } from "node:url";
import { devtools } from "@tanstack/devtools-vite";

export default defineConfig(({ command }) => {
  const isDev = command === "serve";

  return {
    plugins: [react(), tailwindcss(), isDev && devtools()].filter(Boolean),

    resolve: {
      alias: {
        "@": fileURLToPath(new URL("./src", import.meta.url)),
      },
    },
  };
});
