import MobNavbar from '@/components/mobile-navbar';
import { Navbar } from '@/components/navbar';
import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
	title: 'Kly | AI URL Shortener',
	description: 'An AI URL shortener for the modern web.',
};

export default function RootLayout({
	children,
}: Readonly<{
	children: React.ReactNode;
}>) {
	return (
		<html lang='en'>
			<body className={inter.className}>
				<MobNavbar />
				<Navbar />
				{children}
			</body>
		</html>
	);
}
