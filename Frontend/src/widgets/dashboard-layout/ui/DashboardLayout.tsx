import { Outlet } from "react-router";

import { DashboardHeader } from "@/widgets/dashboard-header";
import { DashboardSidebar } from "@/widgets/dashboard-sidebar";

export function DashboardLayout() {
  return (
    <div className="min-h-screen bg-slate-50">
      <DashboardSidebar />

      <div className="pl-64">
        <DashboardHeader />

        <main className="p-6">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
