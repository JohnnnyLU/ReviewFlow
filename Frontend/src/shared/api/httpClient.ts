import { env } from "@/shared/config";

type HttpMethod = "GET" | "POST" | "PUT" | "PATCH" | "DELETE";

type HttpClientOptions = {
  method?: HttpMethod;
  body?: unknown;
  headers?: HeadersInit;
};

export async function httpClient<T>(endpoint: string, options: HttpClientOptions = {}): Promise<T> {
  const { method = "GET", body, headers } = options;

  const response = await fetch(`${env.apiUrl}${endpoint}`, {
    method,
    headers: {
      "Content-Type": "application/json",
      ...headers,
    },
    credentials: "include",
    body: body ? JSON.stringify(body) : undefined,
  });

  if (!response.ok) {
    throw new Error(`Request failed with status ${response.status}`);
  }

  return response.json() as Promise<T>;
}
