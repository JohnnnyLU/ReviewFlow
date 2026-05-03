import { RegisterForm } from "@/features/auth/register";

export function RegisterPage() {
  return (
    <main className="flex min-h-screen items-center justify-center bg-slate-50 px-6">
      <div className="w-full max-w-md">
        <RegisterForm />
      </div>
    </main>
  );
}
