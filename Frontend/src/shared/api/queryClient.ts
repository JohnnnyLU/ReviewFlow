import { QueryClient } from "@tanstack/react-query";

import { HttpError } from "./httpClient";

const ONE_MINUTE = 1000 * 60;

export const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: ONE_MINUTE,
      gcTime: 5 * ONE_MINUTE,
      refetchOnWindowFocus: false,

      retry: (failureCount, error) => {
        if (error instanceof HttpError && error.status >= 400 && error.status < 500) {
          return false;
        }

        return failureCount < 2;
      },
    },

    mutations: {
      retry: false,
    },
  },
});
