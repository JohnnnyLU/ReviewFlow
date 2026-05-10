import { Link } from "react-router";

import { routes } from "@/shared/constants";

export function HomePage() {
  return (
    <main className="min-h-screen bg-slate-50 px-6 py-16">
      <div className="mx-auto max-w-4xl">
        <h1 className="text-4xl font-bold tracking-tight text-slate-900">ReviewFlow</h1>

        <p className="mt-4 max-w-2xl text-lg text-slate-600">
          Сервис для сбора честной обратной связи после визита клиента и улучшения
          качества обслуживания.
        </p>

        <div className="mt-8 flex gap-3">
          <Link
            className="rounded-md bg-slate-900 px-4 py-2 text-sm font-medium text-white hover:bg-slate-800"
            to={routes.register}
          >
            Get started
          </Link>

          <Link
            className="rounded-md px-4 py-2 text-sm font-medium text-slate-900 hover:bg-slate-100"
            to={routes.login}
          >
            Login
          </Link>
        </div>
      </div>
    </main>
  );
}
