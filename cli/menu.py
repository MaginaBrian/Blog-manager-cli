from models.user import User
from models.blog import Blog

def main_menu():
    while True:
        print("\n📝 Blog Manager Menu")
        print("1. Manage Users")
        print("2. Manage Blogs")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            user_menu()
        elif choice == "2":
            blog_menu()
        elif choice == "3":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid input. Please try again.")


def user_menu():
    while True:
        print("\n User Menu")
        print("1. Create User")
        print("2. Delete User") 
        print("3. View all Users")
        print("4. Find User by ID")                   
        print("5. View User's Blogs")
        print("6. Back to Main Menu")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            name = input("Enter user's name: ").strip()
            email = input("Enter user's email: ").strip()
            try:
                user = User.create_user(name, email)
                print(f"Created user: {user}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "2":
            user_id = input("Enter user ID to delete: ").strip()
            if User.delete_by_id(user_id):
                print("User deleted.")
            else:
                print("User not found.")
        elif choice == "3":
            users = User.get_all()
            for user in users:
                print(user)
        elif choice == "4":
            user_id = input("Enter user ID: ").strip()
            user = User.find_by_id(user_id)
            if user:
                print(user)
            else:
                print("User not found.")  
        elif choice == "5":
            user_id = input("Enter user ID: ").strip()
            user = User.find_by_id(user_id)
            if user:
                if user.blogs:
                    for b in user.blogs:
                        print(b)
                else:
                    print("ℹ️ This user has no blogs.")  

            else:
                print("❌ User not found.")

        elif choice == "6":
            break
        else:
            print("❌ Invalid input. Try again.")      


def blog_menu():
    while True:
        print("\n📚 Blog Menu")            
        print("1. Create Blog")            
        print("2. Delete Blog")            
        print("3. View All Blogs")            
        print("4. Find Blog by ID")            
        print("5. Back to Main Menu") 

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            title = input("Enter blog title: ").strip()
            genre = input("Enter genre: ").strip()
            user_id = input("Enter user ID (owner): ").strip()
            try:
                blog = Blog.create_blog(title, genre, user_id)
                print(f"✅ Created blog: {blog}")
            except Exception as e:
                print(f"❌ Error: {e}")    

        elif choice == "2":
            blog_id = input("Enter blog ID to delete: ").strip()
            if Blog.delete_by_id(blog_id):
                print("Blog Deleted.")
            else:
                print("❌ Blog not found.")    

        elif choice ==  "3":
            blogs = Blog.get_all()
            for blog in blogs:
                print(blog)

        elif choice == "4":
            blog_id = input("Enter blog ID: ").strip()
            blog = Blog.find_by_id(blog_id)
            if blog:
                print(blog)
            else:
                print("❌ Blog not found.")  

        elif choice == "5":
            break
        else:
            print("❌ Invalid input. Try again.")