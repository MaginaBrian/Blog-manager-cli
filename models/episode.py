from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database.setup import Base

class Episode(Base):
    __tablename__ = 'episodes'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    duration = Column(Integer, nullable=False, default=0)
    read = Column(Boolean, default=False)
    rating = Column(Integer, nullable=True)
    note = Column(String, nullable=True)
    blog_id = Column(Integer, ForeignKey('blogs.id'), nullable=False)

    blog = relationship("Blog", back_populates="episodes")

    def __repr__(self):
        return (f"<Episode(id={self.id}, title='{self.title}', duration={self.duration} mins, "
                f"read={self.read}, rating={self.rating}, note='{self.note}')>")

    @classmethod
    def create_episode(cls, db, title, duration, blog_id):
        episode = cls(title=title, duration=duration, blog_id=blog_id)
        db.add(episode)
        db.commit()
        return episode

    @classmethod
    def get_all(cls, db):
        return db.query(cls).all()

    @classmethod
    def find_by_id(cls, db, episode_id):
        return db.query(cls).filter_by(id=episode_id).first()

    @classmethod
    def get_by_blog(cls, db, blog_id):
        return db.query(cls).filter_by(blog_id=blog_id).all()

    @classmethod
    def delete_by_id(cls, db, episode_id):
        episode = cls.find_by_id(db, episode_id)
        if episode:
            db.delete(episode)
            db.commit()
            return True
        return False

    def update(self, db, title=None, duration=None, read=None, rating=None, note=None, blog_id=None):
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
        db.commit()

    def mark_read(self, db):
        self.read = True
        db.commit()