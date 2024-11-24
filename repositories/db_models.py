from sqlalchemy import Column, Integer, String, ARRAY

from .database import Base


class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)
    bday = Column(String)
    sex = Column(String)
    interests = Column(ARRAY(item_type=String()))
    city = Column(String)

    def __repr__(self) -> str:
        return f"User(id!={self.id!r}, name={self.name!r}, last_name={self.last_name!r}, email={self.email!r}, password={self.password!r}, bday={self.bday!r}, sex={self.sex!r}, city={self.city!r})"

