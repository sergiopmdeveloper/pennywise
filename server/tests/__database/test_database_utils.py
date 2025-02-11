from unittest.mock import patch

from src.__database.utils import create_db_and_tables


def test_create_db_and_tables():
    """
    WHEN the create_db_and_tables function is called,
    THEN the __import__ function is called for each existing database model,
    AND the SQLModel.metadata.create_all function is called.
    """

    with (
        patch("builtins.__import__") as mock_import,
        patch("src.__database.utils.SQLModel") as mock_sqlmodel,
    ):
        create_db_and_tables()

    mock_import.assert_called_once_with("src.__modules.user.models")
    mock_sqlmodel.metadata.create_all.assert_called_once()
