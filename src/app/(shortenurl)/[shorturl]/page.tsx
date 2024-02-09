import { getBackendUrl } from '@/app/actions/url';
import { redirect } from 'next/navigation';

interface ShortUrlProps {
	params: { shorturl: string };
}

const ShortUrlRedirect = ({ params }: ShortUrlProps) => {
	const { shorturl } = params;

	const baseUrl = getBackendUrl();

	redirect(`${baseUrl}/api/${shorturl}`);
};

export default ShortUrlRedirect;
