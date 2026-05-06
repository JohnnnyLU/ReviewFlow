import { isRouteErrorResponse, useRouteError } from "react-router";

export function RouteErrorPage() {
  const error = useRouteError();

  if (isRouteErrorResponse(error)) {
    return (
      <main>
        <h1>
          {error.status} {error.statusText}
        </h1>

        {error.data && <p>{String(error.data)}</p>}
      </main>
    );
  }

  if (error instanceof Error) {
    return (
      <main>
        <h1>Something went wrong</h1>
        <p>{error.message}</p>
      </main>
    );
  }

  return (
    <main>
      <h1>Something went wrong</h1>
      <p>Unknown route error</p>
    </main>
  );
}
