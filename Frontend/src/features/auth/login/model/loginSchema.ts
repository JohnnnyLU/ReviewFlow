import { z } from "zod";
import { PASSWORD_MAX_LENGTH, PASSWORD_MIN_LENGTH } from "@/features/auth/model";

export const loginSchema = z.object({
  email: z.string().trim().min(1, "Введите email").email("Введите корректный email"),
  password: z
    .string()
    .min(1, "Введите пароль")
    .min(
      PASSWORD_MIN_LENGTH,
      `Пароль должен содержать минимум ${PASSWORD_MIN_LENGTH} символов`,
    )
    .max(
      PASSWORD_MAX_LENGTH,
      `Пароль должен содержать не больше ${PASSWORD_MAX_LENGTH} символов`,
    ),
});

export type LoginFormValues = z.infer<typeof loginSchema>;
