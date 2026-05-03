import { LoginForm } from "@/features/auth/login";

export function LoginPage() {
  return (
    <main className="flex min-h-screen items-center justify-center bg-slate-50 px-6">
      <div className="w-full max-w-md">
        <LoginForm />
      </div>
    </main>
  );
}
