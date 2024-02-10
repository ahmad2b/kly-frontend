import { z } from 'zod';

export const LoginValidator = z.object({
	email_address: z.string().email(),
	username: z.string().min(6),
	password: z.string().min(8),
});

export type LoginRequest = z.infer<typeof LoginValidator>;

export const SignupValidator = z.object({
	email_address: z.string().email(),
	username: z.string().min(6, 'Username must be at least 6 characters'),
	password: z.string().min(8, 'Password must be at least 8 characters'),
	confirmpassword: z.string().min(8, 'Password must be at least 8 characters'),
});

export type SignupRequest = z.infer<typeof SignupValidator>;

export const UrlValidator = z.object({
	url: z.string().url(),
});

export type UrlRequest = z.infer<typeof UrlValidator>;
