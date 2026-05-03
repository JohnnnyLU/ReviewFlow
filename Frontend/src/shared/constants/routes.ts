export const routes = {
  home: "/",
  login: "/login",
  register: "/register",

  dashboard: "/dashboard",
  customers: "/dashboard/customers",
  feedback: "/dashboard/feedback",
  campaigns: "/dashboard/campaigns",
  settings: "/dashboard/settings",

  customersRelative: "customers",
  feedbackRelative: "feedback",
  campaignsRelative: "campaigns",
  settingsRelative: "settings",

  publicFeedback: "/feedback/:token",

  buildPublicFeedback: (token: string) => `/feedback/${token}`,
};
