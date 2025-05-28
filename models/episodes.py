from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database.setup import Base, session

class Episode(Base):
    __tablename__ = 'episodes'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    duration = Column(Integer)  
    read = Column(Boolean, default=False)
    rating = Column(Integer, nullable=True)  
    note = Column(String, nullable=True)
    blog_id = Column(Integer, ForeignKey('blogs.id'), nullable=False)

    blog = relationship("Blog", back_populates="episodes")

    def __repr__(self):
        return (f"<Episode(id={self.id}, title='{self.title}', duration={self.duration} mins, "
                f"read={self.read}, rating={self.rating}, note='{self.note}')>")

    @classmethod
    def create_episode(cls, title, duration, blog_id):
        episode = cls(title=title, duration=duration, blog_id=blog_id)
        session.add(episode)
        session.commit()
        return episode

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, episode_id):
        return session.query(cls).filter_by(id=episode_id).first()

    @classmethod
    def get_by_blog(cls, blog_id):
        return session.query(cls).filter_by(blog_id=blog_id).all()

    @classmethod
    def delete_by_id(cls, episode_id):
        episode = cls.find_by_id(episode_id)
        if episode:
            session.delete(episode)
            session.commit()
            return True
        return False

    def update(self, title=None, duration=None, read=None, rating=None, note=None, blog_id=None):
        if title is not None:
            self.title = title
        if duration is not None:
            self.duration = duration
        if read is not None:
            self.read = read
        if rating is not None:
            self.rating = rating
        if note is not None:
            self.note = note
        if blog_id is not None:
            self.blog_id = blog_id
        session.commit()

    def mark_read(self):
        self.read = True
        session.commit()