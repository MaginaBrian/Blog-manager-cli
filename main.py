from database.setup import Base, engine
from models.user import User
from models.blog import Blog
from cli.menu import main_menu

Base.metadata.create_all(engine)

main_menu()