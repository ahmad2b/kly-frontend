import { z } from 'zod';

export const LoginValidator = z.object({
	email: z.string().email(),
	password: z.string().min(8),
});

export type LoginRequest = z.infer<typeof LoginValidator>;

export const SignupValidator = z.object({
	email: z.string().email(),
	password: z.string().min(8),
	confirmPassword: z.string().min(8),
});

export type SignupRequest = z.infer<typeof SignupValidator>;

export const UrlValidator = z.object({
	url: z.string().url(),
});

export type UrlRequest = z.infer<typeof UrlValidator>;
