import { LoginForm } from "@/features/auth/login";

export function LoginPage() {
  return (
    <main className="flex min-h-screen items-center justify-center bg-[radial-gradient(circle_at_16%_10%,rgba(124,58,237,0.045),transparent_32%),linear-gradient(135deg,#fbfcff_0%,#ffffff_52%,#f7f4ff_100%)] px-4 py-6 sm:px-8 sm:py-10">
      <div className="w-full max-w-[560px]">
        <LoginForm />
      </div>
    </main>
  );
}
