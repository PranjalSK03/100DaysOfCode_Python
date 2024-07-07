class User:
    #use of the constructor
    def __init__(self, user_id, user_name):
        self.uid = user_id
        self.username = user_name
        self.followers = 0 # may provide a default value too
        self.following = 0
        
    def follow(self, user):
        user.followers += 1
        self.following += 1
        
user1 = User("001", "Hulk")
user2 = User("002", "Rack")

print(user1.uid, user1.username)

user2.follow(user1)

print("user 1", "follower ->", user1.followers, "following ->", user1.following)
print("user 2", "follower ->", user2.followers, "following ->", user2.following)