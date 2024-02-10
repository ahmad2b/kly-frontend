'use server';
import { cookies } from 'next/headers';

import { fetchBackendUrl } from '@/lib/utils';

import { LoginRequest, SignupRequest } from '@/lib/validators';

export type SignupPayload = Pick<
	SignupRequest,
	'email_address' | 'username' | 'password'
>;

export interface User {
	id: string;
	username: string;
	email_address: string;
	created_at: string;
	updated_at: string;
	deleted_at: string;
}

export interface SignupResponse {
	data?: User;
	error?: string;
}

export async function signup(payload: SignupPayload): Promise<SignupResponse> {
	const baseUrl = fetchBackendUrl();

	console.log('\nSignup Payload', payload);

	const response = await fetch(`${baseUrl}/api/users`, {
		method: 'POST',
		body: JSON.stringify(payload),
		headers: {
			'Content-Type': 'application/json',
		},
		cache: 'no-store',
	});

	console.log('\nSignup Res', response.status);

	if (!response.ok) {
		const json = await response.json();
		console.log('\nSignup Res', json);
		return { error: json.message };
	}

	const res = await response.json();

	console.log('\nSignup Res', res);

	return { data: res };
}

export type LoginPayload = Pick<
	LoginRequest,
	'email_address' | 'username' | 'password'
>;

export type Token = {
	jwt: string;
	object: string;
};

export interface LoginResponse {
	data?: Token;
	error?: string;
}

export async function login(payload: LoginPayload): Promise<LoginResponse> {
	const baseUrl = fetchBackendUrl();

	console.log('\nLogin Payload', payload);

	const response = await fetch(`${baseUrl}/api/users/signin`, {
		method: 'POST',
		body: JSON.stringify(payload),
		headers: {
			'Content-Type': 'application/json',
		},
		cache: 'no-store',
	});

	console.log('\nLogin Res', response.status);

	if (!response.ok) {
		const json = await response.json();
		console.log('\nLogin Res', json);
		return { error: json.message };
	}

	const res = await response.json();

	const cookieStore = cookies();

	const tokenMaxAge = 60 * 5; // 5 minutes
	const refreshTimeExtra = 60 * 5; // 5 minutes

	for (let key in res) {
		let maxAge = tokenMaxAge; // Default max age for access_token

		const cookieOptions = {
			name: key, // Use the attribute name as the cookie name
			value: res[key], // Use the attribute value as the cookie value
			maxAge: maxAge,
			httpOnly: true,
			path: '/',
			secure: process.env.NODE_ENV === 'production',
		};

		cookieStore.set(cookieOptions);
	}

	console.log('\nLogin Res', res);

	return { data: res };
}
