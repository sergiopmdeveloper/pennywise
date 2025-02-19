import { signUpSchema } from '@/__api/user/schemas';
import { createUser } from '@/__api/user/services';
import { type SignUpData } from '@/__api/user/types';
import { Button } from '@/__ui/components/ui/button';
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '@/__ui/components/ui/card';
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from '@/__ui/components/ui/form';
import { Input } from '@/__ui/components/ui/input';
import { zodResolver } from '@hookform/resolvers/zod';
import { useMutation } from '@tanstack/react-query';
import { type AxiosError } from 'axios';
import { Loader2 } from 'lucide-react';
import { useState } from 'react';
import { useForm } from 'react-hook-form';
import { Link, useNavigate } from 'react-router';

/**
 * Sign up form component.
 */
export function SignUpForm() {
  const form = useForm<SignUpData>({
    resolver: zodResolver(signUpSchema),
    defaultValues: {
      name: '',
      email: '',
      password: '',
    },
  });

  const [signUpStatus, setSignUpStatus] = useState<number | undefined>();
  const navigate = useNavigate();

  const signUpMutation = useMutation({
    mutationFn: createUser,
    onSuccess: () => {
      navigate('/account');
    },
    onError: (error) => {
      const responseError = error as AxiosError;
      setSignUpStatus(responseError?.response?.status);
    },
  });

  /**
   * Handles the sign up form submission.
   * @param {SignUpData} data - The new user data.
   */
  function onSubmit(data: SignUpData) {
    signUpMutation.mutate(data);
  }

  return (
    <Card className="relative w-sm">
      <CardHeader>
        <CardTitle className="text-3xl">Sign up</CardTitle>
        <CardDescription>Create a new account</CardDescription>
      </CardHeader>

      <CardContent>
        <Form {...form}>
          <form className="space-y-6" id="sign-up-form" onSubmit={form.handleSubmit(onSubmit)}>
            <FormField
              control={form.control}
              name="name"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Name</FormLabel>

                  <FormControl>
                    <Input autoComplete="name" placeholder="Pennywise" {...field} />
                  </FormControl>

                  <FormMessage />
                </FormItem>
              )}
            />

            <FormField
              control={form.control}
              name="email"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Email</FormLabel>

                  <FormControl>
                    <Input autoComplete="email" placeholder="pennywise@gmail.com" {...field} />
                  </FormControl>

                  <FormMessage />
                </FormItem>
              )}
            />

            <FormField
              control={form.control}
              name="password"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Password</FormLabel>

                  <FormControl>
                    <Input
                      type="password"
                      autoComplete="current-password"
                      placeholder="*********"
                      {...field}
                    />
                  </FormControl>

                  <FormMessage />
                </FormItem>
              )}
            />
          </form>
        </Form>

        <p className="mt-6 text-sm">
          Do you already have an account?{' '}
          <Link className="text-blue-500 underline underline-offset-4" to="/sign-in">
            Sign in
          </Link>
        </p>
      </CardContent>

      <CardFooter>
        <Button
          className="w-full"
          type="submit"
          form="sign-up-form"
          disabled={signUpMutation.isPending}
        >
          Send
          {signUpMutation.isPending && <Loader2 className="animate-spin" />}
        </Button>
      </CardFooter>

      {signUpStatus === 409 && (
        <p className="text-destructive absolute -top-6 right-0 text-xs">Email already exists</p>
      )}
    </Card>
  );
}
