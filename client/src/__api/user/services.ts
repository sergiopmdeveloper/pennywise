import apiClient from '@/__api/base';
import { type MutationResponseWithToken } from '@/__api/types';
import { type SignUpData } from '@/__api/user/types';
import { type AxiosResponse } from 'axios';

/**
 * Creates a new user.
 * @param {UserCreation} user - The user to be created.
 * @returns {Promise<AxiosResponse<MutationResponseWithToken, any>>} The user creation response.
 */
export async function createUser(
  user: SignUpData,
): Promise<AxiosResponse<MutationResponseWithToken, any>> {
  return await apiClient.post<MutationResponseWithToken>('/user', user, {
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
  });
}
