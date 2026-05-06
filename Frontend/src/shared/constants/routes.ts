const rootSegments = {
  login: "login",
  register: "register",
  dashboard: "dashboard",
  publicFeedback: "feedback/:token",
} as const;

const dashboardSegments = {
  customers: "customers",
  feedback: "feedback",
  campaigns: "campaigns",
  settings: "settings",
} as const;

const joinRoute = (base: string, segment: string) => `${base}/${segment}`;

export const routes = {
  home: "/",

  login: `/${rootSegments.login}`,
  register: `/${rootSegments.register}`,

  dashboard: `/${rootSegments.dashboard}`,
  customers: joinRoute(`/${rootSegments.dashboard}`, dashboardSegments.customers),
  feedback: joinRoute(`/${rootSegments.dashboard}`, dashboardSegments.feedback),
  campaigns: joinRoute(`/${rootSegments.dashboard}`, dashboardSegments.campaigns),
  settings: joinRoute(`/${rootSegments.dashboard}`, dashboardSegments.settings),

  publicFeedback: `/${rootSegments.publicFeedback}`,
} as const;

export const relativeRoutes = {
  login: rootSegments.login,
  register: rootSegments.register,
  dashboard: rootSegments.dashboard,
  publicFeedback: rootSegments.publicFeedback,

  customers: dashboardSegments.customers,
  feedback: dashboardSegments.feedback,
  campaigns: dashboardSegments.campaigns,
  settings: dashboardSegments.settings,
} as const;

export const routeBuilders = {
  buildPublicFeedback: (token: string) => `/feedback/${encodeURIComponent(token)}`,
} as const;

export type AppRoute = (typeof routes)[keyof typeof routes];
export type RelativeRoute = (typeof relativeRoutes)[keyof typeof relativeRoutes];
export type DashboardRelativeRoute = (typeof dashboardSegments)[keyof typeof dashboardSegments];
