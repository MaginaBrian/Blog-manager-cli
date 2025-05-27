from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.setup import Base, session


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)


    user = relationship("User", back_populates="blogs")

    def __repr__(self):
        return f"<Blog(id={self.id}, title='self.title', genre='{self.genre}')"

    @classmethod
    def create_blog(cls, title, genre, user_id):
        blog = cls(title=title, genre=genre, user_id=user_id)
        session.add(blog)
        session.commit()
        return blog

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, blog_id):
        return session.query(cls).filter_by(id=blog_id).first()

    @classmethod
    def delete_by_id(cls, blog_id):
        blog = cls.find_by_id(blog_id)
        if blog:
            session.delete(blog)
            session.commit()
            return True
        return False