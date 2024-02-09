'use server';

export interface ShortenURL {
	id: number;
	url: string;
	short_url: string;
	clicks: number;
	created_at: Date;
	updated_at: Date;
	expires_at: Date;
	deleted_at: Date;
	user_id: number;
}

interface Response {
	data?: ShortenURL;
	error?: string;
}

export const getBackendUrl = () => {
	const backendUrl = process.env.NEXT_PUBLIC_API_URL;
	if (!backendUrl) {
		throw new Error('Backend URL is not defined');
	}
	return backendUrl;
};

export async function urlShortener(data: { url: string }): Promise<Response> {
	const { url } = data;

	if (!url) {
		throw new Error('URL is not defined');
	}

	const baseUrl = getBackendUrl();

	const response = await fetch(`${baseUrl}/api/url`, {
		method: 'POST',
		body: JSON.stringify({ url }),
		headers: {
			'Content-Type': 'application/json',
		},
		cache: 'no-store',
	});

	if (!response.ok) {
		const json = await response.json();
		return { error: json.message };
	}

	const res = await response.json();

	console.log('URL Shortner Response', res);

	return { data: res };
}
