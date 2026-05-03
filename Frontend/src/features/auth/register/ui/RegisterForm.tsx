import { Button, Card, Input } from "@/shared/ui";

export function RegisterForm() {
  return (
    <Card>
      <h1 className="text-2xl font-bold text-slate-900">Register</h1>

      <form className="mt-6 space-y-4">
        <Input placeholder="Business name" />
        <Input placeholder="Email" type="email" />
        <Input placeholder="Password" type="password" />

        <Button className="w-full" type="submit">
          Create account
        </Button>
      </form>
    </Card>
  );
}
