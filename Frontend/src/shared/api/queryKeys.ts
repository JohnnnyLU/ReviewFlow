export const queryKeys = {
  auth: {
    currentUser: ["auth", "current-user"] as const,
  },
  customers: {
    all: ["customers"] as const,
    lists: () => [...queryKeys.customers.all, "list"] as const,
    list: (filters: unknown) => [...queryKeys.customers.lists(), filters] as const,
  },
  feedback: {
    all: ["feedback"] as const,
    lists: () => [...queryKeys.feedback.all, "list"] as const,
    list: (filters: unknown) => [...queryKeys.feedback.lists(), filters] as const,
  },
} as const;
