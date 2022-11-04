import dotenv

dotenv.load_dotenv()

print(dotenv.get_key('../.env', 'SECRET_KEY'))
