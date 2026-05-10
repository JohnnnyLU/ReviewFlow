import { useId } from "react";
import { ChevronDown } from "lucide-react";
import { Link } from "react-router";

import googleIcon from "@/shared/assets/icons/Google_Favicon_2025.svg";
import { routes } from "@/shared/constants";
import { cn } from "@/shared/lib";
import { Button, Card, Input } from "@/shared/ui";

import { useForm, useWatch } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import {
  registerSchema,
  type RegisterFormValues,
} from "@/features/auth/register/model/registerSchema";
import { FieldError, PasswordField } from "@/features/auth/ui";

const businessTypeOptions = [
  { value: "", label: "Выберите тип бизнеса" },
  { value: "cafe", label: "Кафе или ресторан" },
  { value: "retail", label: "Розничная торговля" },
  { value: "services", label: "Услуги" },
  { value: "healthcare", label: "Медицина и здоровье" },
  { value: "other", label: "Другое" },
] as const;

const fieldClassName =
  "h-12 rounded-lg border border-slate-200 bg-white px-4 text-[15px] font-medium text-slate-950 shadow-[0_2px_10px_rgba(15,23,42,0.03)] placeholder:text-slate-400 focus:border-violet-500 focus:ring-4 focus:ring-violet-100";

export function RegisterForm() {
  const formId = useId();

  const businessNameId = `${formId}-business-name`;
  const businessTypeId = `${formId}-business-type`;
  const emailId = `${formId}-email`;
  const passwordId = `${formId}-password`;
  const passwordConfirmId = `${formId}-password-confirm`;

  const businessNameErrorId = `${businessNameId}-error`;
  const businessTypeErrorId = `${businessTypeId}-error`;
  const emailErrorId = `${emailId}-error`;
  const passwordErrorId = `${passwordId}-error`;
  const passwordConfirmErrorId = `${passwordConfirmId}-error`;

  const rootErrorId = `${formId}-root-error`;

  const {
    register,
    handleSubmit,
    setError,
    control,
    formState: { errors, isSubmitting },
  } = useForm<RegisterFormValues>({
    resolver: zodResolver(registerSchema),
    defaultValues: {
      businessName: "",
      businessType: "",
      email: "",
      password: "",
      passwordConfirm: "",
    },
    mode: "onChange",
  });

  const businessType = useWatch({
    control,
    name: "businessType",
  });

  const onSubmit = async (_values: RegisterFormValues) => {
    try {
      // Здесь к примеру будет API request
      // await register requests later
    } catch {
      setError("root", {
        type: "server",
        message: "Не удалось создать аккаунт. Попробуйте позже",
      });
    }
  };

  return (
    <Card className="w-full rounded-[22px] border border-slate-200/80 bg-white px-6 py-9 shadow-[0_24px_80px_rgba(15,23,42,0.08)] sm:px-10 sm:py-12 lg:px-20 lg:py-[72px]">
      <div className="mx-auto w-full max-w-[560px]">
        <header>
          <h1 className="text-[30px] leading-tight font-extrabold text-slate-950 sm:text-[34px]">
            Создайте аккаунт
          </h1>
          <p className="mt-2 text-[15px] leading-6 font-semibold text-slate-400">
            Заполните данные, чтобы начать работу с ReviewFlow
          </p>
        </header>

        <form className="mt-9 space-y-5" onSubmit={handleSubmit(onSubmit)} noValidate>
          <div className="space-y-2.5">
            <label
              className="block text-[15px] leading-5 font-bold text-slate-700"
              htmlFor={businessNameId}
            >
              Название бизнеса
            </label>
            <Input
              id={businessNameId}
              {...register("businessName")}
              autoComplete="organization"
              className={fieldClassName}
              placeholder="Например, Кофейня на Ленина"
              aria-invalid={Boolean(errors.businessName)}
              aria-describedby={errors.businessName ? businessNameErrorId : undefined}
            />

            <FieldError id={businessNameErrorId} message={errors.businessName?.message} />
          </div>

          <div className="space-y-2.5">
            <label
              className="block text-[15px] leading-5 font-bold text-slate-700"
              htmlFor={businessTypeId}
            >
              Тип бизнеса
            </label>

            <div className="relative">
              <select
                id={businessTypeId}
                {...register("businessType")}
                className={cn(
                  fieldClassName,
                  "w-full appearance-none pr-12 outline-none",
                  businessType ? "text-slate-950" : "text-slate-400",
                )}
                aria-invalid={Boolean(errors.businessType)}
                aria-describedby={errors.businessType ? businessTypeErrorId : undefined}
              >
                {businessTypeOptions.map((option) => (
                  <option
                    key={option.value}
                    value={option.value}
                    disabled={!option.value}
                    hidden={!option.value}
                  >
                    {option.label}
                  </option>
                ))}
              </select>

              <ChevronDown
                aria-hidden="true"
                className="pointer-events-none absolute top-1/2 right-4 size-5 -translate-y-1/2 text-slate-400"
                strokeWidth={2.25}
              />
            </div>

            <FieldError id={businessTypeErrorId} message={errors.businessType?.message} />
          </div>

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
            autoComplete="new-password"
            label="Пароль"
            errorId={passwordErrorId}
            errorMessage={errors.password?.message}
            inputProps={register("password")}
          />

          <PasswordField
            id={passwordConfirmId}
            autoComplete="new-password"
            label="Подтвердите пароль"
            errorId={passwordConfirmErrorId}
            errorMessage={errors.passwordConfirm?.message}
            inputProps={register("passwordConfirm")}
          />

          <FieldError id={rootErrorId} message={errors.root?.message} />

          <Button
            className="mt-2 h-12 w-full rounded-lg bg-violet-600 text-base font-extrabold text-white shadow-[0_14px_30px_rgba(124,58,237,0.24)] hover:bg-violet-700 focus:ring-4 focus:ring-violet-200 focus:outline-none"
            type="submit"
            disabled={isSubmitting}
          >
            Зарегистрироваться
          </Button>
        </form>

        <p className="mx-auto mt-5 text-center text-sm leading-6 font-semibold text-slate-400">
          <span className="block">
            Регистрируясь, вы соглашаетесь с{" "}
            <a
              className="font-bold text-violet-600 hover:text-violet-700 focus:ring-2 focus:ring-violet-500 focus:ring-offset-2 focus:outline-none"
              href="/terms"
            >
              Условиями использования
            </a>
          </span>
          <span className="block">
            и{" "}
            <a
              className="font-bold text-violet-600 hover:text-violet-700 focus:ring-2 focus:ring-violet-500 focus:ring-offset-2 focus:outline-none"
              href="/privacy"
            >
              Политикой конфиденциальности
            </a>
          </span>
        </p>

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
          Уже есть аккаунт?{" "}
          <Link
            className="ml-2 text-violet-600 hover:text-violet-700 focus:ring-2 focus:ring-violet-500 focus:ring-offset-2 focus:outline-none"
            to={routes.login}
          >
            Войти
          </Link>
        </p>
      </div>
    </Card>
  );
}
