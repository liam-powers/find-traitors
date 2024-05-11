import instaloader
from instaloader.exceptions import TwoFactorAuthRequiredException

L = instaloader.Instaloader()

username = input("Enter Instagram username: ")
password = input("Enter Instagram password: ")

try:
    L.login(username, password)
except TwoFactorAuthRequiredException:
    two_factor_code = input("Enter 2FA code: ")
    L.two_factor_login(two_factor_code)
print("Successfully logged in!")

user_profile = instaloader.Profile.from_username(L.context, username)
print("Successfully obtained your profile!")

print("Now obtaining followers and followees. Please grant a few minutes.")

followers = set(user_profile.get_followers())
print("Obtained followers list!")
followees = set(user_profile.get_followees())
print("Obtained followees list!")

not_following_back = followees - followers

print("Users not following you back: ")
for user in not_following_back:
    print(user.username)
