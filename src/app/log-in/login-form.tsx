'use client';

import { zodResolver } from '@hookform/resolvers/zod';
import { useForm } from 'react-hook-form';

import { login } from '@/app/actions/auth';
import { Button } from '@/components/ui/button';
import {
	Form,
	FormControl,
	FormField,
	FormItem,
	FormLabel,
	FormMessage,
} from '@/components/ui/form';
import { Input } from '@/components/ui/input';
import { LoginRequest, LoginValidator } from '@/lib/validators';
import { toast } from 'sonner';

export function LoginForm() {
	const form = useForm<LoginRequest>({
		resolver: zodResolver(LoginValidator),
		defaultValues: {
			email_address: '',
			username: '',
			password: '',
		},
	});

	async function onSubmit(data: LoginRequest) {
		const { ...payload } = LoginValidator.parse(data);

		const response = await login(payload);

		if (response.error) {
			console.error('An error occurred while logging in', response.error);
			toast('An error occurred while logging in. Please try again later.', {
				description: response.error,
				action: {
					label: 'Retry',
					onClick: () => form.handleSubmit(onSubmit)(),
				},
			});
			return;
		}

		if (response.data) {
			toast('You have successfully logged in!', {
				description: `Welcome, !`,
				position: 'bottom-right',
			});
			form.reset();
			return;
		}
	}

	return (
		<Form {...form}>
			<form
				onSubmit={form.handleSubmit(onSubmit)}
				className='space-y-4 w-full text-left'
			>
				<FormField
					control={form.control}
					name='email_address'
					render={({ field }) => (
						<FormItem>
							<FormLabel>Email</FormLabel>
							<FormControl>
								<Input
									{...field}
									type='email'
									placeholder='Email'
								/>
							</FormControl>
							<FormMessage />
						</FormItem>
					)}
				/>
				<FormField
					control={form.control}
					name='username'
					render={({ field }) => (
						<FormItem>
							<FormLabel>Username</FormLabel>
							<FormControl>
								<Input
									{...field}
									type='text'
									placeholder='Username'
								/>
							</FormControl>
							<FormMessage />
						</FormItem>
					)}
				/>
				<FormField
					control={form.control}
					name='password'
					render={({ field }) => (
						<FormItem>
							<FormLabel>Password</FormLabel>
							<FormControl>
								<Input
									{...field}
									type='password'
									placeholder='Password'
								/>
							</FormControl>
							<FormMessage />
						</FormItem>
					)}
				/>
				<Button
					type='submit'
					className='w-full'
					isLoading={form.formState.isSubmitting}
					disabled={form.formState.isSubmitting}
				>
					Login
				</Button>
			</form>
		</Form>
	);
}
