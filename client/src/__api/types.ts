export type MutationResponse = {
  entity: string;
  action: string;
  affected_ids: string[];
};

export type MutationResponseWithToken = MutationResponse & {
  token: {
    value: string;
    type: string;
  };
};
