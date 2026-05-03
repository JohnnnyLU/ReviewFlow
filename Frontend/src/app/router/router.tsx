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

import { routes } from "@/shared/constants";

export const router = createBrowserRouter([
  {
    path: routes.home,
    element: <HomePage />,
  },
  {
    path: routes.login,
    element: <LoginPage />,
  },
  {
    path: routes.register,
    element: <RegisterPage />,
  },
  {
    path: routes.dashboard,
    element: <DashboardLayout />,
    children: [
      {
        index: true,
        element: <DashboardPage />,
      },
      {
        path: routes.customersRelative,
        element: <CustomersPage />,
      },
      {
        path: routes.feedbackRelative,
        element: <FeedbackListPage />,
      },
      {
        path: routes.campaignsRelative,
        element: <CampaignsPage />,
      },
      {
        path: routes.settingsRelative,
        element: <SettingsPage />,
      },
    ],
  },
  {
    path: routes.publicFeedback,
    element: <PublicFeedbackPage />,
  },
  {
    path: "*",
    element: <NotFoundPage />,
  },
]);
