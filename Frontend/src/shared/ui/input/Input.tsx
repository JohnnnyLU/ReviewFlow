import type { InputHTMLAttributes } from "react";

import { cn } from "@/shared/lib";

type InputProps = InputHTMLAttributes<HTMLInputElement>;

export function Input({ className, ...props }: InputProps) {
  return (
    <input
      className={cn(
        "w-full rounded-md border border-slate-300 px-3 py-2 text-sm outline-none focus:border-slate-900",
        className,
      )}
      {...props}
    />
  );
}
