from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.setup import Base

class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship("User", back_populates="blogs")
    episodes = relationship("Episode", back_populates="blog", cascade="all, delete")

    def __repr__(self):
        return f"<Blog(id={self.id}, title='{self.title}', genre='{self.genre}')>"

    @classmethod
    def create_blog(cls, db, title, genre, user_id):
        blog = cls(title=title, genre=genre, user_id=user_id)
        db.add(blog)
        db.commit()
        return blog

    @classmethod
    def get_all(cls, db):
        return db.query(cls).all()

    @classmethod
    def find_by_id(cls, db, blog_id):
        return db.query(cls).filter_by(id=blog_id).first()

    @classmethod
    def delete_by_id(cls, db, blog_id):
        blog = cls.find_by_id(db, blog_id)
        if blog:
            db.delete(blog)
            db.commit()
            return True
        return False

    def update(self, db, title=None, genre=None, user_id=None):
        if title is not None:
            self.title = title
        if genre is not None:
            self.genre = genre
        if user_id is not None:
            self.user_id = user_id
        db.commit()