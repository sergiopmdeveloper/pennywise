import SignUp from '@/__features/auth/sign-up/page';
import Home from '@/__features/home/page';
import { BrowserRouter, Route, Routes } from 'react-router';

/**
 * Router component.
 */
export default function Router() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="sign-up" element={<SignUp />} />
      </Routes>
    </BrowserRouter>
  );
}
