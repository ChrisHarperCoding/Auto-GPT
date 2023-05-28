import pinterest
import os

# Login to Pinterest
pinterest.login(os.environ['PINTEREST_USERNAME'], os.environ['PINTEREST_PASSWORD'])

# Browse posts
pinterest.browse_posts()

# Logout from Pinterest
pinterest.logout()