import { Logo } from '@/components/logo';
import { buttonVariants } from '@/components/ui/button';
import { cn } from '@/lib/utils';

import Link from 'next/link';

export function Navbar() {
	return (
		<div className='hidden md:block'>
			<div className='px-6 py-4 flex justify-between'>
				<Logo />
				<ul className='flex space-x-4'>
					<li>
						<Link
							href='/log-in'
							className={cn(
								buttonVariants({ className: 'hover:bg-gray-900/90' })
							)}
						>
							Log In
						</Link>
					</li>
					<li>
						<Link
							href='/sign-up'
							className={cn(
								buttonVariants({
									variant: 'secondary',
									className: 'hover:bg-gray-900/10',
								})
							)}
						>
							Sign Up
						</Link>
					</li>
				</ul>
			</div>
		</div>
	);
}
