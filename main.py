from database.setup import Base, engine
from cli.menu import main_menu
import click

def init_db():
    """Initialize database tables."""
    try:
        Base.metadata.create_all(engine)
        click.echo("Database tables initialized successfully.")
    except Exception as e:
        click.echo(f"Error initializing database: {e}")
        raise

if __name__ == "__main__":
    init_db()
    main_menu()