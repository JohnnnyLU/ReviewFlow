import { createBrowserRouter } from "react-router";

import { HomePage } from "@/pages/home";
import { LoginPage } from "@/pages/login";
import { RegisterPage } from "@/pages/register";
import { DashboardPage } from "@/pages/dashboard";
import { CustomersPage } from "@/pages/customers";
import { FeedbackListPage } from "@/pages/feedback-list";
import { CampaignsPage } from "@/pages/campaigns";
import { SettingsPage } from "@/pages/settings";
import { PublicFeedbackPage } from "@/pages/public-feedback";
import { NotFoundPage } from "@/pages/not-found";

import { DashboardLayout } from "@/widgets/dashboard-layout";

import { routes, relativeRoutes } from "@/shared/constants";
import { RouteErrorPage } from "@/shared/ui/route-error-page";
import { ProtectedRoute } from "./ProtectedRoute";

export const router = createBrowserRouter([
  {
    path: routes.home,
    errorElement: <RouteErrorPage />,
    children: [
      {
        index: true,
        element: <HomePage />,
      },
      {
        path: relativeRoutes.login,
        element: <LoginPage />,
      },
      {
        path: relativeRoutes.register,
        element: <RegisterPage />,
      },
      {
        path: relativeRoutes.dashboard,
        element: (
          <ProtectedRoute>
            <DashboardLayout />
          </ProtectedRoute>
        ),
        children: [
          {
            index: true,
            element: <DashboardPage />,
          },
          {
            path: relativeRoutes.customers,
            element: <CustomersPage />,
          },
          {
            path: relativeRoutes.feedback,
            element: <FeedbackListPage />,
          },
          {
            path: relativeRoutes.campaigns,
            element: <CampaignsPage />,
          },
          {
            path: relativeRoutes.settings,
            element: <SettingsPage />,
          },
        ],
      },
      {
        path: relativeRoutes.publicFeedback,
        element: <PublicFeedbackPage />,
      },
      {
        path: "*",
        element: <NotFoundPage />,
      },
    ],
  },
]);
