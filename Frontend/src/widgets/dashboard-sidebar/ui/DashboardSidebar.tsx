import { NavLink } from "react-router";

import { routes } from "@/shared/constants";
import type { AppRoute } from "@/shared/constants/routes";
import { cn } from "@/shared/lib";

type NavigationItem = {
  label: string;
  to: AppRoute;
};

const navigationItems: NavigationItem[] = [
  {
    label: "Dashboard",
    to: routes.dashboard,
  },
  {
    label: "Customers",
    to: routes.customers,
  },
  {
    label: "Feedback",
    to: routes.feedback,
  },
  {
    label: "Campaigns",
    to: routes.campaigns,
  },
  {
    label: "Settings",
    to: routes.settings,
  },
];

export function DashboardSidebar() {
  return (
    <aside className="fixed top-0 left-0 h-screen w-64 border-r border-slate-200 bg-white p-4">
      <div className="text-lg font-bold text-slate-900">ReviewFlow</div>

      <nav className="mt-8 space-y-1">
        {navigationItems.map((item) => (
          <NavLink
            key={item.to}
            end={item.to === routes.dashboard}
            className={({ isActive }) =>
              cn(
                "block rounded-md px-3 py-2 text-sm font-medium text-slate-600 hover:bg-slate-100 hover:text-slate-900",
                isActive && "bg-slate-900 text-white hover:bg-slate-900 hover:text-white",
              )
            }
            to={item.to}
          >
            {item.label}
          </NavLink>
        ))}
      </nav>
    </aside>
  );
}
