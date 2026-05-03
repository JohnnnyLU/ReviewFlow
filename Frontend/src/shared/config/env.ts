const apiUrl = import.meta.env.VITE_API_URL;

if (!apiUrl && import.meta.env.PROD) {
  throw new Error("VITE_API_URL is required in production");
}

export const env = {
  apiUrl: apiUrl ?? "http://localhost:8000",
};
