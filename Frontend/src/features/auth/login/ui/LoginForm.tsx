import { Button, Card, Input } from "@/shared/ui";

export function LoginForm() {
  return (
    <Card>
      <h1 className="text-2xl font-bold text-slate-900">Login</h1>

      <form className="mt-6 space-y-4">
        <Input placeholder="Email" type="email" />
        <Input placeholder="Password" type="password" />

        <Button className="w-full" type="submit">
          Login
        </Button>
      </form>
    </Card>
  );
}
