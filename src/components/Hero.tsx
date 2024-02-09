'use client';

import { zodResolver } from '@hookform/resolvers/zod';
import { useForm } from 'react-hook-form';
import { z } from 'zod';

import { Button } from '@/components/ui/button';
import {
	Form,
	FormControl,
	FormDescription,
	FormField,
	FormItem,
	FormMessage,
} from '@/components/ui/form';
import { Input } from '@/components/ui/input';
import { toast } from '@/components/ui/use-toast';

const FormSchema = z.object({
	url: z.string().url(),
});

export function HeroSection() {
	const form = useForm<z.infer<typeof FormSchema>>({
		resolver: zodResolver(FormSchema),
		defaultValues: {
			url: '',
		},
	});

	function onSubmit(data: z.infer<typeof FormSchema>) {
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
		<div className='flex flex-col items-center justify-center p-6 min-h-2.5'>
			<h2 className='scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight first:mt-0'>
				An AI URL shortener for the modern web.{' '}
				<span
					role='img'
					aria-label='rocket'
				>
					🚀
				</span>
			</h2>
			<div className='mx-auto w-full max-w-md py-4 md:py-10'>
				<Form {...form}>
					<form
						onSubmit={form.handleSubmit(onSubmit)}
						className='space-y-4'
					>
						<FormField
							control={form.control}
							name='url'
							render={({ field }) => (
								<FormItem>
									<FormControl>
										<Input
											{...field}
											placeholder='https://example.com'
											className='w-full'
										/>
									</FormControl>
									<FormDescription>
										Enter a valid URL to shorten it.
									</FormDescription>
									<FormMessage />
								</FormItem>
							)}
						/>
						<Button type='submit'>Shorten URL</Button>
					</form>
				</Form>
			</div>
		</div>
	);
}
