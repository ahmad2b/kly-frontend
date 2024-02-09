'use client';

import { zodResolver } from '@hookform/resolvers/zod';
import { useForm } from 'react-hook-form';

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
import { toast } from '@/components/ui/use-toast';
import { SignupRequest, SignupValidator } from '@/lib/validators';

export function SignupForm() {
	const form = useForm<SignupRequest>({
		resolver: zodResolver(SignupValidator),
		defaultValues: {
			email: '',
			password: '',
			confirmPassword: '',
		},
	});

	function onSubmit(data: SignupRequest) {
		toast({
			title: 'You submitted the following values:',
			description: (
				<pre className='mt-2 w-[340px] rounded-md bg-slate-950 p-4'>
					<code className='text-white'>{JSON.stringify(data, null, 2)}</code>
				</pre>
			),
		});
	}

	return (
		<Form {...form}>
			<form
				onSubmit={form.handleSubmit(onSubmit)}
				className='space-y-4 w-full text-left'
			>
				<FormField
					control={form.control}
					name='email'
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
							{/* <FormDescription>Enter your email address</FormDescription> */}
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
							{/* <FormDescription>Enter your password</FormDescription> */}
							<FormMessage />
						</FormItem>
					)}
				/>
				<FormField
					control={form.control}
					name='confirmPassword'
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
							{/* <FormDescription>Enter your password</FormDescription> */}
							<FormMessage />
						</FormItem>
					)}
				/>
				<Button
					type='submit'
					className='w-full'
				>
					Sign up
				</Button>
			</form>
		</Form>
	);
}
