import type { ReactNode } from "react";
import { Navigate, useLocation } from "react-router";

import { routes } from "@/shared/constants";

type ProtectedRouteProps = {
  children: ReactNode;
};

const isAuthBypassEnabled =
  import.meta.env.DEV && import.meta.env.VITE_ENABLE_AUTH_BYPASS === "true";

export function ProtectedRoute({ children }: ProtectedRouteProps) {
  const location = useLocation();

  const isAuthenticated = false; // Заглушка

  if (!isAuthenticated && !isAuthBypassEnabled) {
    return <Navigate to={routes.login} state={{ from: location }} replace />;
  }

  return children;
}
