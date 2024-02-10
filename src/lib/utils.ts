import { clsx, type ClassValue } from 'clsx';
import { twMerge } from 'tailwind-merge';

export function cn(...inputs: ClassValue[]) {
	return twMerge(clsx(inputs));
}

export const fetchBackendUrl = () => {
	const backendUrl = process.env.NEXT_PUBLIC_API_URL;
	if (!backendUrl) {
		throw new Error('Backend URL is not defined');
	}
	return backendUrl;
};
