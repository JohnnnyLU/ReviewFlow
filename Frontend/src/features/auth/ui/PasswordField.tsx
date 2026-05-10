import { useState } from "react";
import type { UseFormRegisterReturn } from "react-hook-form";

import eyeOffIcon from "@/shared/assets/icons/eye-off.svg";
import eyeIcon from "@/shared/assets/icons/eye.svg";
import { cn } from "@/shared/lib";
import { Input } from "@/shared/ui";

import { FieldError } from "./FieldError";

const fieldClassName =
  "h-12 rounded-lg border border-slate-200 bg-white px-4 text-[15px] font-medium text-slate-950 shadow-[0_2px_10px_rgba(15,23,42,0.03)] placeholder:text-slate-400 focus:border-violet-500 focus:ring-4 focus:ring-violet-100";

type PasswordFieldProps = {
  autoComplete: "current-password" | "new-password";
  errorId: string;
  errorMessage?: string;
  id: string;
  inputProps: UseFormRegisterReturn;
  label: string;
};

export function PasswordField({
  autoComplete,
  errorId,
  errorMessage,
  id,
  inputProps,
  label,
}: PasswordFieldProps) {
  const [isVisible, setIsVisible] = useState(false);
  const buttonLabel = isVisible
    ? `Скрыть ${label.toLowerCase()}`
    : `Показать ${label.toLowerCase()}`;

  return (
    <div className="space-y-2.5">
      <label
        className="block text-[15px] leading-5 font-bold text-slate-700"
        htmlFor={id}
      >
        {label}
      </label>

      <div className="relative">
        <Input
          id={id}
          {...inputProps}
          type={isVisible ? "text" : "password"}
          autoComplete={autoComplete}
          className={cn(fieldClassName, "pr-12", !isVisible && "text-sm")}
          placeholder="••••••••••••••"
          aria-invalid={Boolean(errorMessage)}
          aria-describedby={errorMessage ? errorId : undefined}
        />

        <button
          aria-label={buttonLabel}
          aria-pressed={isVisible}
          className="absolute top-1/2 right-3 inline-flex size-9 -translate-y-1/2 items-center justify-center rounded-md text-slate-400 transition-colors hover:text-slate-600 focus:outline-none focus-visible:ring-2 focus-visible:ring-violet-500 focus-visible:ring-offset-2"
          type="button"
          onClick={() => setIsVisible((currentValue) => !currentValue)}
        >
          <img alt="" className="size-5" src={isVisible ? eyeOffIcon : eyeIcon} />
        </button>
      </div>

      <FieldError id={errorId} message={errorMessage} />
    </div>
  );
}
