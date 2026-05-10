import { useId } from "react";
import { Link } from "react-router";

import googleIcon from "@/shared/assets/icons/Google_Favicon_2025.svg";
import { routes } from "@/shared/constants";
import { Button, Card, Input } from "@/shared/ui";

import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import {
  loginSchema,
  type LoginFormValues,
} from "@/features/auth/login/model/loginSchema";
import { FieldError, PasswordField } from "@/features/auth/ui";

const fieldClassName =
  "h-12 rounded-lg border border-slate-200 bg-white px-4 text-[15px] font-medium text-slate-950 shadow-[0_2px_10px_rgba(15,23,42,0.03)] placeholder:text-slate-400 focus:border-violet-500 focus:ring-4 focus:ring-violet-100";

export function LoginForm() {
  const formId = useId();
  const emailId = `${formId}-email`;
  const passwordId = `${formId}-password`;

  const emailErrorId = `${emailId}-error`;
  const passwordErrorId = `${passwordId}-error`;
  const rootErrorId = `${formId}-root-error`;

  const {
    register,
    handleSubmit,
    setError,
    formState: { errors, isSubmitting },
  } = useForm<LoginFormValues>({
    resolver: zodResolver(loginSchema),
    defaultValues: {
      email: "",
      password: "",
    },
    mode: "onChange",
  });

  const onSubmit = async (_values: LoginFormValues) => {
    try {
      // Здесь к примеру будет API request
      // await login requests later
    } catch {
      setError("root", {
        type: "server",
        message: "Неверный email или пароль",
      });
    }
  };

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

      <form className="mt-9 space-y-5" onSubmit={handleSubmit(onSubmit)} noValidate>
        <div className="space-y-2.5">
          <label
            className="block text-[15px] leading-5 font-bold text-slate-700"
            htmlFor={emailId}
          >
            Email
          </label>
          <Input
            id={emailId}
            {...register("email")}
            type="email"
            autoComplete="email"
            className={fieldClassName}
            placeholder="you@example.com"
            aria-invalid={Boolean(errors.email)}
            aria-describedby={errors.email ? emailErrorId : undefined}
          />

          <FieldError id={emailErrorId} message={errors.email?.message} />
        </div>

        <PasswordField
          id={passwordId}
          autoComplete="current-password"
          label="Пароль"
          errorId={passwordErrorId}
          errorMessage={errors.password?.message}
          inputProps={register("password")}
        />

        <FieldError id={rootErrorId} message={errors.root?.message} />

        <Button
          className="mt-2 h-12 w-full rounded-lg bg-violet-600 text-base font-extrabold text-white shadow-[0_14px_30px_rgba(124,58,237,0.24)] hover:bg-violet-700 focus:ring-4 focus:ring-violet-200 focus:outline-none"
          type="submit"
          disabled={isSubmitting}
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
