import Link from 'next/link';
import { FaFacebookF, FaGoogle, FaXTwitter } from 'react-icons/fa6';

import { cn } from '@/lib/utils';

import { Logo } from '@/components/logo';
import { buttonVariants } from '@/components/ui/button';
import { LoginForm } from './login-form';

const socialIcons = [
	{
		name: 'Facebook',
		icon: FaFacebookF,
		href: '#',
	},
	{
		name: 'X',
		icon: FaXTwitter,
		href: '#',
	},
	{
		name: 'X',
		icon: FaGoogle,
		href: '#',
	},
];

const Login = () => {
	return (
		<section className='bg-gray-1 dark:bg-dark'>
			<div className='container mx-auto'>
				<div className='-mx-4 flex flex-wrap'>
					<div className='w-full px-4'>
						<div className='relative mx-auto max-w-[525px] overflow-hidden rounded-lg bg-white px-10 py-16 text-center dark:bg-dark-2 sm:px-12 md:px-[60px]'>
							<div className='mb-10 md:mb-10 flex items-center justify-center'>
								<Logo
									height={60}
									width={60}
								/>
							</div>

							<h1 className='mb-8 text-3xl items-center font-extrabold'>
								Log In
							</h1>

							<LoginForm />

							<div className='w-full text-left'>
								<Link
									href={'/log-in'}
									className={cn(
										buttonVariants({
											variant: 'link',
											className: 'p-2',
										})
									)}
								>
									Forget Password?
								</Link>
							</div>

							<div className='flex flex-col space-y-4 py-4'>
								<p className='text-sm text-secondary-color dark:text-dark-7 '>
									Or Connect With
								</p>
								<ul className='-mx-2 mb-6 flex justify-between'>
									{socialIcons.map((icon, index) => (
										<li
											key={index}
											className='w-full px-2'
										>
											<Link
												href={icon.href}
												className={cn(
													buttonVariants({
														variant: 'secondary',
														className: 'w-full hover:bg-black/20',
													})
												)}
											>
												<icon.icon size={20} />
											</Link>
										</li>
									))}
								</ul>
							</div>

							<div className='flex items-center justify-center'>
								<span className='text-sm font-medium'>Not a member yet?</span>
								<Link
									href={'/sign-up'}
									className={cn(
										buttonVariants({
											variant: 'link',
										})
									)}
								>
									<p>Sign up</p>
								</Link>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>
	);
};

export default Login;
