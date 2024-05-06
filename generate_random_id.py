import random
import string

def generate_random_id(length):
    # Generate a random alphanumeric string of given length
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
