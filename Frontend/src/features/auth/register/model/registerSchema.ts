import { z } from "zod";
import {
  PASSWORD_MAX_LENGTH,
  PASSWORD_MIN_LENGTH,
  BUSINESS_NAME_MIN_LENGTH,
  BUSINESS_NAME_MAX_LENGTH,
} from "@/features/auth/model";

export const registerSchema = z
  .object({
    businessName: z
      .string()
      .trim()
      .min(1, "Введите название бизнеса")
      .min(
        BUSINESS_NAME_MIN_LENGTH,
        `Название бизнеса должно содержать минимум ${BUSINESS_NAME_MIN_LENGTH} символа`,
      )
      .max(
        BUSINESS_NAME_MAX_LENGTH,
        `Название бизнеса должно содержать не больше ${BUSINESS_NAME_MAX_LENGTH} символов`,
      ),
    businessType: z.string().min(1, "Выберите тип бизнеса"),
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
    passwordConfirm: z
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
  })
  .refine((values) => values.password === values.passwordConfirm, {
    message: "Пароли не совпадают",
    path: ["passwordConfirm"],
  });

export type RegisterFormValues = z.infer<typeof registerSchema>;
