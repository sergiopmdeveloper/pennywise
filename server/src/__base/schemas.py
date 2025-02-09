from typing import Literal

from pydantic import BaseModel


class MutationResponseSchema(BaseModel):
    """
    Mutation response schema.

    Attributes
    ----------
    entity : str
        The entity with which the action has occurred.
    action : Literal["create", "update", "delete"]
        The action taken.
    affected_ids : list[str]
        The IDs of the affected elements.
    """

    entity: Literal["user"]
    action: Literal["create", "update", "delete"]
    affected_ids: list[str]
