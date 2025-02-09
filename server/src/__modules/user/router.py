from fastapi import APIRouter, Depends
from sqlmodel import Session

from src.__base.dependencies import get_session
from src.__base.schemas import MutationResponseSchema
from src.__modules.user.schemas import UserCreationSchema

router = APIRouter(prefix="/user", tags=["user"])


@router.post("", response_model=MutationResponseSchema)
def create_user(
    *, session: Session = Depends(get_session), user_data: UserCreationSchema
) -> MutationResponseSchema:
    """
    POST | /user | Creates a new user.

    Parameters
    ----------
    session : Session
        The database session as a dependency.
    user_data : UserCreationSchema
        The data of the user to be created.

    Returns
    -------
    MutationResponseSchema
        The user creation response.
    """

    return MutationResponseSchema(
        entity="user", action="create", affected_ids=["user_id"]
    )
