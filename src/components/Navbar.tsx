import { Logo } from '@/components/Logo';
import { Button } from '@/components/ui/button';

import Link from 'next/link';

function Navbar() {
	return (
		<div className='hidden md:block'>
			<div className='p-6 flex justify-between'>
				<Logo />
				<div className='flex gap-4'>
					<Link href='/log-in'>
						<Button
							variant='secondary'
							className='bg-gray-800 text-white hover:bg-gray-700'
						>
							Log In
						</Button>
					</Link>

					<Link href='/sign-up'>
						<Button
							variant='secondary'
							className='hover:bg-gray-200'
						>
							Sign Up
						</Button>
					</Link>
				</div>
			</div>
		</div>
	);
}

export default Navbar;
