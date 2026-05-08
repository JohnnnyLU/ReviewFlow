import { useId, useState } from "react";
import { Link } from "react-router";

import googleIcon from "@/shared/assets/icons/Google_Favicon_2025.svg";
import eyeOffIcon from "@/shared/assets/icons/eye-off.svg";
import eyeIcon from "@/shared/assets/icons/eye.svg";
import { routes } from "@/shared/constants";
import { cn } from "@/shared/lib";
import { Button, Card, Input } from "@/shared/ui";

const fieldClassName =
  "h-12 rounded-lg border border-slate-200 bg-white px-4 text-[15px] font-medium text-slate-950 shadow-[0_2px_10px_rgba(15,23,42,0.03)] placeholder:text-slate-400 focus:border-violet-500 focus:ring-4 focus:ring-violet-100";

export function LoginForm() {
  const formId = useId();
  const emailId = `${formId}-email`;
  const passwordId = `${formId}-password`;
  const [isPasswordVisible, setIsPasswordVisible] = useState(false);
  const passwordToggleLabel = isPasswordVisible ? "Скрыть пароль" : "Показать пароль";

  return (
    <Card className="w-full rounded-[22px] border border-slate-200/80 bg-white px-6 py-9 shadow-[0_24px_80px_rgba(15,23,42,0.08)] sm:px-10 sm:py-12">
      <header>
        <h1 className="text-[30px] leading-tight font-extrabold text-slate-950 sm:text-[34px]">
          Войдите в аккаунт
        </h1>
        <p className="mt-2 text-[15px] leading-6 font-semibold text-slate-400">
          Продолжите работу с отзывами и клиентами в ReviewFlow
        </p>
      </header>

      <form className="mt-9 space-y-5">
        <div className="space-y-2.5">
          <label className="block text-[15px] leading-5 font-bold text-slate-700" htmlFor={emailId}>
            Email
          </label>
          <Input
            autoComplete="email"
            className={fieldClassName}
            id={emailId}
            name="email"
            placeholder="you@example.com"
            required
            type="email"
          />
        </div>

        <div className="space-y-2.5">
          <label
            className="block text-[15px] leading-5 font-bold text-slate-700"
            htmlFor={passwordId}
          >
            Пароль
          </label>
          <div className="relative">
            <Input
              autoComplete="current-password"
              className={cn(fieldClassName, "pr-12", !isPasswordVisible && "text-sm")}
              id={passwordId}
              name="password"
              placeholder="••••••••••••••"
              required
              type={isPasswordVisible ? "text" : "password"}
            />
            <button
              aria-label={passwordToggleLabel}
              aria-pressed={isPasswordVisible}
              className="absolute top-1/2 right-3 inline-flex size-9 -translate-y-1/2 items-center justify-center rounded-md text-slate-400 transition-colors hover:text-slate-600 focus:outline-none focus-visible:ring-2 focus-visible:ring-violet-500 focus-visible:ring-offset-2"
              type="button"
              onClick={() => setIsPasswordVisible((currentValue) => !currentValue)}
            >
              <img alt="" className="size-5" src={isPasswordVisible ? eyeOffIcon : eyeIcon} />
            </button>
          </div>
        </div>

        <Button
          className="mt-2 h-12 w-full rounded-lg bg-violet-600 text-base font-extrabold text-white shadow-[0_14px_30px_rgba(124,58,237,0.24)] hover:bg-violet-700 focus:ring-4 focus:ring-violet-200 focus:outline-none"
          type="submit"
        >
          Войти
        </Button>
      </form>

      <div className="my-9 flex items-center gap-4">
        <div className="h-px flex-1 bg-slate-200" />
        <span className="text-sm font-semibold text-slate-400">или</span>
        <div className="h-px flex-1 bg-slate-200" />
      </div>

      <Button
        className="h-12 w-full rounded-lg border border-slate-200 bg-white text-[15px] font-extrabold text-slate-700 shadow-[0_2px_10px_rgba(15,23,42,0.03)] hover:bg-slate-50 focus:ring-4 focus:ring-slate-100 focus:outline-none"
        type="button"
        variant="secondary"
      >
        <img alt="" className="mr-4 size-5" src={googleIcon} />
        Продолжить с Google
      </Button>

      <p className="mt-9 text-center text-base font-bold text-slate-500">
        Нет аккаунта?{" "}
        <Link
          className="ml-2 text-violet-600 hover:text-violet-700 focus:ring-2 focus:ring-violet-500 focus:ring-offset-2 focus:outline-none"
          to={routes.register}
        >
          Зарегистрироваться
        </Link>
      </p>
    </Card>
  );
}
