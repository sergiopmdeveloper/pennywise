import Providers from '@/__base/providers';
import Router from '@/__base/router';
import '@/index.css';
import { createRoot } from 'react-dom/client';

createRoot(document.getElementById('root')!).render(
  <Providers>
    <Router />
  </Providers>,
);
