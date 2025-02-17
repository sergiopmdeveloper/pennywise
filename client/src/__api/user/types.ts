export type User = {
  id: string;
  name: string;
  email: string;
  password: string;
};

export type UserCreation = Omit<User, 'id'> & { name?: string };
