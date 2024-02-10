'use client';

import { zodResolver } from '@hookform/resolvers/zod';
import { useForm } from 'react-hook-form';

import { SignupRequest, SignupValidator } from '@/lib/validators';

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

import { signup } from '@/app/actions/auth';
import { toast } from 'sonner';

export function SignupForm() {
	const form = useForm<SignupRequest>({
		resolver: zodResolver(SignupValidator),
		defaultValues: {
			email_address: '',
			username: '',
			password: '',
			confirmpassword: '',
		},
	});

	async function onSubmit(data: SignupRequest) {
		const { confirmpassword, ...payload } = SignupValidator.parse(data);

		const response = await signup(payload);

		if (response.error) {
			toast('An error occurred while signing up. Please try again later.', {
				description: response.error,
				action: {
					label: 'Retry',
					onClick: () => form.handleSubmit(onSubmit)(),
				},
			});
			return;
		}

		if (response.data) {
			toast('You have successfully signed up!', {
				description: `Welcome, ${response.data.username}!`,
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
				<FormField
					control={form.control}
					name='confirmpassword'
					render={({ field }) => (
						<FormItem>
							<FormLabel>Confirm Password</FormLabel>
							<FormControl>
								<Input
									{...field}
									type='password'
									placeholder='Confirm Password'
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
					Sign up
				</Button>
			</form>
		</Form>
	);
}
