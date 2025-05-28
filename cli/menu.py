from models.user import User
from models.blog import Blog
from models.episodes import Episode
from tabulate import tabulate

def main_menu():
    while True:
        print("\n📝 Blog Manager Menu")
        print("1. Manage Users")
        print("2. Manage Blogs")
        print("3. Manage Episodes")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            user_menu()
        elif choice == "2":
            blog_menu()
        elif choice == "3":
            episode_menu()
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("ℹ️ Invalid input. Please try again.")

# ----------------------------- User Menu -----------------------------
def user_menu():
    while True:
        print("\n👤 User Menu")
        print("1. Create User")
        print("2. View All Users")
        print("3. View User's Blogs")
        print("4. Find User by ID")
        print("5. Delete User")
        print("6. Back to Main Menu")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            name = input("Enter user's name: ").strip()
            email = input("Enter user's email: ").strip()
            try:
                user = User.create_user(name, email)
                print(f"✅ Created user: {user}")
            except Exception as e:
                print(f"ℹ️ Error: {e}")

        elif choice == "2":
            users = User.get_all()
            if users:
                table = [[u.id, u.name, u.email] for u in users]
                print(tabulate(table, headers=["ID", "Name", "Email"], tablefmt="fancy_grid"))
            else:
                print("ℹ️ No users found.")

        elif choice == "3":
            try:
                user_id = int(input("Enter user ID: ").strip())
                user = User.find_by_id(user_id)
                if user:
                    if user.blogs:
                        table = [[b.id, b.title, b.genre] for b in user.blogs]
                        print(tabulate(table, headers=["ID", "Title", "Genre"], tablefmt="fancy_grid"))
                    else:
                        print("ℹ️ This user has no blogs.")
                else:
                    print("ℹ️ User not found.")
            except ValueError:
                print("ℹ️ Invalid ID.")

        elif choice == "4":
            try:
                user_id = int(input("Enter user ID: ").strip())
                user = User.find_by_id(user_id)
                if user:
                    table = [[user.id, user.name, user.email]]
                    print(tabulate(table, headers=["ID", "Name", "Email"], tablefmt="fancy_grid"))
                else:
                    print("ℹ️ User not found.")
            except ValueError:
                print("ℹ️ Invalid ID.")

        elif choice == "5":
            try:
                user_id = int(input("Enter user ID to delete: ").strip())
                confirm = input("Are you sure you want to delete the user? (y/n): ").strip().lower()
                if confirm in ["y", "yes"]:
                    if User.delete_by_id(user_id):
                        print("✅ User deleted.")
                    else:
                        print("ℹ️ User not found.")
                elif confirm in ["n", "no"]:
                    print("Thank you for your confirmation 👍. The user was not deleted!")
                else:
                    print("ℹ️ Please enter y or n.")
            except ValueError:
                print("ℹ️ Invalid ID.")

        elif choice == "6":
            break
        else:
            print("ℹ️ Invalid input. Try again.")

# ----------------------------- Blog Menu -----------------------------
def blog_menu():
    while True:
        print("\n📚 Blog Menu")
        print("1. Create Blog")
        print("2. Delete Blog")
        print("3. View All Blogs")
        print("4. Find Blog by ID")
        print("5. Update Blog")
        print("6. Back to Main Menu")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            title = input("Enter blog title: ").strip()
            genre = input("Enter genre: ").strip()
            try:
                user_id = int(input("Enter user ID (owner): ").strip())
                blog = Blog.create_blog(title, genre, user_id)
                print(f"✅ Created blog: {blog}")
            except ValueError:
                print("ℹ️ Invalid user ID.")
            except Exception as e:
                print(f"ℹ️ Error: {e}")

        elif choice == "2":
            try:
                blog_id = int(input("Enter blog ID to delete: ").strip())
                confirm = input("Are you sure you want to delete the blog? (y/n): ").strip().lower()
                if confirm in ["y", "yes"]:
                    if Blog.delete_by_id(blog_id):
                        print("✅ Blog deleted.")
                    else:
                        print("ℹ️ Blog not found.")
                elif confirm in ["n", "no"]:
                    print("Thank you for your confirmation 👍. The blog was not deleted!")
                else:
                    print("ℹ️ Please enter y or n.")
            except ValueError:
                print("ℹ️ Invalid blog ID.")

        elif choice == "3":
            blogs = Blog.get_all()
            if blogs:
                table = [[b.id, b.title, b.genre, b.user_id] for b in blogs]
                print(tabulate(table, headers=["ID", "Title", "Genre", "User ID"], tablefmt="fancy_grid"))
            else:
                print("ℹ️ No blogs found.")

        elif choice == "4":
            try:
                blog_id = int(input("Enter blog ID: ").strip())
                blog = Blog.find_by_id(blog_id)
                if blog:
                    table = [[blog.id, blog.title, blog.genre, blog.user_id]]
                    print(tabulate(table, headers=["ID", "Title", "Genre", "User ID"], tablefmt="fancy_grid"))
                else:
                    print("ℹ️ Blog not found.")
            except ValueError:
                print("ℹ️ Invalid blog ID.")

        elif choice == "5":
            try:
                blog_id = int(input("Enter blog ID to edit: ").strip())
                blog = Blog.find_by_id(blog_id)
                if blog:
                    print(f"Editing: {blog}")
                    new_title = input("New title (Enter to skip): ").strip()
                    new_genre = input("New genre (Enter to skip): ").strip()
                    new_user_id = input("New user ID (Enter to skip): ").strip()
                    blog.update(
                        title=new_title or None,
                        genre=new_genre or None,
                        user_id=int(new_user_id) if new_user_id else None
                    )
                    print("✅ Blog updated.")
                else:
                    print("ℹ️ Blog not found.")
            except ValueError:
                print("ℹ️ Invalid ID.")
            except Exception as e:
                print(f"ℹ️ Error: {e}")

        elif choice == "6":
            break
        else:
            print("ℹ️ Invalid input. Try again.")

# ----------------------------- Episode Menu -----------------------------
def episode_menu():
    while True:
        print("\n🎬 Episode Menu")
        print("1. Create Episode")
        print("2. View All Episodes")
        print("3. View Episodes by Blog")
        print("4. Mark Episode as Read/Unread")
        print("5. Rate and Add Note to Episode")
        print("6. Delete Episode")
        print("7. Back to Main Menu")

        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            title = input("Enter episode title: ").strip()
            try:
                duration = input("Enter duration (e.g., 25:30): ").strip()
                blog_id = int(input("Enter blog ID: ").strip())
                episode = Episode.create_episode(title, duration, blog_id)
                print(f"✅ Episode created: {episode}")
            except ValueError:
                print("ℹ️ Invalid blog ID or duration format.")
            except Exception as e:
                print(f"ℹ️ Error: {e}")

        elif choice == "2":
            episodes = Episode.get_all()
            if episodes:
                table = [[
                    ep.id,
                    ep.title,
                    f"{ep.duration} mins" if ep.duration else "N/A",
                    "✅" if ep.read else "❌",
                    ep.rating if ep.rating and 1 <= ep.rating <= 10 else "N/A",
                    ep.note if ep.note else "No note",
                    ep.blog_id
                ] for ep in episodes]
                print(tabulate(table, headers=["ID", "Title", "Duration", "Read", "Rating", "Notes", "Blog ID"], tablefmt="fancy_grid"))
            else:
                print("ℹ️ No episodes found.")

        elif choice == "3":
            try:
                blog_id = int(input("Enter blog ID to view episodes: ").strip())
                episodes = Episode.get_by_blog(blog_id)
                if episodes:
                    table = [[ep.id, ep.title, ep.duration, "✅" if ep.read else "❌"] for ep in episodes]
                    print(tabulate(table, headers=["ID", "Title", "Duration", "Read"], tablefmt="fancy_grid"))
                else:
                    print("ℹ️ No episodes for this blog.")
            except ValueError:
                print("ℹ️ Invalid blog ID.")

        elif choice == "4":
            try:
                episode_id = int(input("Enter episode ID: ").strip())
                episode = Episode.find_by_id(episode_id)
                if episode:
                    status = input("Mark as read? (yes/no): ").strip().lower()
                    episode.update(read=(status == "yes"))
                    print("✅ Episode updated.")
                else:
                    print("ℹ️ Episode not found.")
            except ValueError:
                print("ℹ️ Invalid ID.")

        elif choice == "5":
            try:
                episode_id = int(input("Enter episode ID: ").strip())
                episode = Episode.find_by_id(episode_id)
                if episode:
                    while True:
                        try:
                            rating = input("Rate the episode (1-10, leave blank to skip): ").strip()
                            if rating == "":
                                rating = None
                                break
                            rating = int(rating)
                            if rating < 1 or rating > 10:
                                print("ℹ️ Rating must be between 1 and 10.")
                                continue
                            break
                        except ValueError:
                            print("ℹ️ Invalid rating. Enter a number between 1 and 10.")
                    note = input("Add a note (leave blank to skip): ").strip()
                    note = note if note else None
                    episode.update(rating=rating, note=note)
                    print("✅ Episode updated with rating and note.")
                else:
                    print("ℹ️ Episode not found.")
            except ValueError:
                print("ℹ️ Invalid episode ID.")

        elif choice == "6":
            try:
                episode_id = int(input("Enter episode ID to delete: ").strip())
                episode = Episode.find_by_id(episode_id)
                if episode:
                    confirm = input(f"Are you sure you want to delete episode '{episode.title}'? (y/n): ").strip().lower()
                    if confirm in ["y", "yes"]:
                        if Episode.delete_by_id(episode_id):
                            print("✅ Episode deleted.")
                        else:
                            print("ℹ️ Could not delete episode.")
                    else:
                        print("ℹ️ Deletion cancelled.")
                else:
                    print("ℹ️ Episode not found.")
            except ValueError:
                print("ℹ️ Invalid episode ID.")

        elif choice == "7":
            break
        else:
            print("ℹ️ Invalid input. Try again.")