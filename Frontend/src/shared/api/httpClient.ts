import { env } from "@/shared/config";

type HttpMethod = "GET" | "POST" | "PUT" | "PATCH" | "DELETE";

type HttpClientOptions = {
  method?: HttpMethod;
  body?: unknown;
  headers?: HeadersInit;
};

export class HttpError extends Error {
  constructor(
    message: string,
    public readonly status: number,
    public readonly payload: unknown,
  ) {
    super(message);
    this.name = "HttpError";
  }
}

export async function httpClient<T>(
  endpoint: string,
  options: HttpClientOptions = {},
): Promise<T> {
  const { method = "GET", body, headers } = options;

  const isFormData = body instanceof FormData;
  const hasBody = body !== undefined;

  const requestHeaders = new Headers(headers);

  if (hasBody && !isFormData && !requestHeaders.has("Content-Type")) {
    requestHeaders.set("Content-Type", "application/json");
  }

  const response = await fetch(`${env.apiUrl}${endpoint}`, {
    method,
    headers: requestHeaders,
    credentials: "include",
    body: hasBody ? (isFormData ? body : JSON.stringify(body)) : undefined,
  });

  const contentType = response.headers.get("Content-Type");
  const isJson = contentType?.includes("application/json");

  const payload =
    response.status === 204
      ? undefined
      : isJson
        ? await response.json()
        : await response.text();

  if (!response.ok) {
    throw new HttpError(
      `Request failed with status ${response.status}`,
      response.status,
      payload,
    );
  }

  return payload as T;
}
