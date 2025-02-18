import { signUpSchema } from '@/__api/user/schemas';
import { z } from 'zod';

export type SignUpData = z.infer<typeof signUpSchema>;
