import { Button } from '@/__ui/components/ui/button';
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '@/__ui/components/ui/card';
import { Input } from '@/__ui/components/ui/input';
import { Label } from '@/__ui/components/ui/label';
import { Link } from 'react-router';

/**
 * Sign up form component.
 */
export default function SignUpForm() {
  return (
    <Card className="w-sm">
      <CardHeader>
        <CardTitle className="text-3xl">Sign up</CardTitle>
        <CardDescription>Create a new account</CardDescription>
      </CardHeader>

      <CardContent>
        <form className="space-y-6" id="sign-up-form">
          <div className="grid gap-2">
            <Label htmlFor="email">Email</Label>
            <Input id="email" autoComplete="email" placeholder="pennywise@gmail.com" />
          </div>

          <div className="grid gap-2">
            <Label htmlFor="password">Password</Label>

            <Input
              id="password"
              type="password"
              autoComplete="current-password"
              placeholder="*********"
            />
          </div>
        </form>

        <p className="mt-6 text-sm">
          Do you already have an account?{' '}
          <Link className="text-blue-500 underline underline-offset-4" to="/sign-in">
            Sign in
          </Link>
        </p>
      </CardContent>

      <CardFooter>
        <Button className="w-full" type="submit" form="sign-up-form">
          Send
        </Button>
      </CardFooter>
    </Card>
  );
}
