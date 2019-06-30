# y2s19-flask-login-demo

## Demo 1 - Making Users
After walking students through the setup of `models.py` and `database.py`, ask them how we could use these functions to make a user directly in `database.py`. Call that function and create an example user, then open and run `print_database.py` and see that the user was indeed created and added to the database. However, would it be a good idea to hard-code in all of the users like this? Ask them what would be a better way?

## Demo 2 - Users Making Users
Have them help you walk through `app.py` and talk about each component. Then run the server and go through the process of creating a user and then signing in.

## Demo 2.5 User Being Remembered
We can use a variable to remember which user has logged in (what kind of variable do we need if it should be changed inside function and that change should take affect in other functions?).  However, there are limitations to this approach. Try signing in on one tab, then open an incognito window and go to the site (what should we see, and why doesn't this result match?). We will come back and solve this problem later, but right now we have an even bigger issue: when the database was printed, all the passwords were clear to read, which means easy to steal.

## Demo 3 - Secure Password Storage
Show the secure login example - create a user, sign in, and check the printed database. (could we use the hash stored in the database to sign in? why not?)

## Demo 4 - Login Session
Show the session example - note you need a secret key to use session. The session cannot store the user directly (sad), but it can store a string, so what string could we store and how would we use that to get the user object?
