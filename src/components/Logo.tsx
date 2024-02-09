import Image from 'next/image';
import Link from 'next/link';

interface LogoProps {
	width?: number;
	height?: number;
}

export const Logo = ({ width = 40, height = 40 }: LogoProps) => {
	return (
		<Link href={'/'}>
			<Image
				src={'/logo.svg'}
				alt='Logo'
				width={width}
				height={height}
			/>
		</Link>
	);
};
