import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { StrictMode } from 'react';

const queryClient = new QueryClient();

/**
 * Providers component.
 * @param {ProvidersProps} props - The props of the component.
 * @param {React.ReactNode} props.children - The children to render.
 */
export default function Providers({ children }: ProvidersProps) {
  return (
    <QueryClientProvider client={queryClient}>
      <StrictMode>{children}</StrictMode>
    </QueryClientProvider>
  );
}

/**
 * Providers component props.
 */
type ProvidersProps = {
  children: React.ReactNode;
};
