from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.setup import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    blogs = relationship("Blog", back_populates="user", cascade="all, delete")

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"

    @classmethod
    def create_user(cls, db, name, email):
        user = cls(name=name, email=email)
        db.add(user)
        db.commit()
        return user

    @classmethod
    def get_all(cls, db):
        return db.query(cls).all()

    @classmethod
    def find_by_id(cls, db, user_id):
        return db.query(cls).filter_by(id=user_id).first()

    @classmethod
    def delete_by_id(cls, db, user_id):
        user = cls.find_by_id(db, user_id)
        if user:
            db.delete(user)
            db.commit()
            return True
        return False

    def email_provider(self):
        return self.email.split('@')[-1] if '@' in self.email else None