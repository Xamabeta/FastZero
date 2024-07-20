from sqlalchemy import select

from fast_api.models import User


def test_create_user(session):
    new_user = User(
        username='anamaria', password='asenha', email='anamaria@example.com'
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'anamaria'))

    assert user.username == 'anamaria'
