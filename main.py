# Get instance
import instaloader

L = instaloader.Instaloader()

def main():
    try:
        # Login or load session
        username = input("Enter your Instagram Username: ")
        password = input("Enter your Instagram Password: ")
        L.login(username, password)  # (login)

        # Obtain profile metadata
        print("Loading profile metadata")
        profile = instaloader.Profile.from_username(L.context, username)

        follow_list = []
        follower_list = []

        # List of following
        print("Loading list of following...\n")
        for user in profile.get_followers():
            follow_list.append(user.username)

        # List of followers
        print("Loading list of followers...\n")
        for user in profile.get_followees():
            follower_list.append(user.username)

        print("Comparing...\n")
        for user in follower_list:
            if user not in follow_list:
                print(user)
    except Exception as e:
        print(e)
        main()
main()
