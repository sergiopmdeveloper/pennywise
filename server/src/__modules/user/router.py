from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session

from src.__base.dependencies import get_session
from src.__base.schemas import MutationResponseSchema
from src.__modules.auth.utils import password_hasher
from src.__modules.user.models import User
from src.__modules.user.schemas import UserCreationSchema

router = APIRouter(prefix="/user", tags=["user"])


@router.post(
    "", response_model=MutationResponseSchema, status_code=status.HTTP_201_CREATED
)
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

    user_data.password = password_hasher.hash(user_data.password.get_secret_value())

    user = User.model_validate(user_data)

    session.add(user)

    try:
        session.commit()
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Email already exists"
        )

    return MutationResponseSchema(
        entity="user", action="create", affected_ids=[str(user.id)]
    )
