import os
from datetime import datetime
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB Configuration
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = "agentic_ai_system"
COLLECTION_NAME = "chat_history"

def get_db_collection():
    """
    Connects to MongoDB and returns the chat_history collection.
    """
    try:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        # Verify connection
        client.admin.command('ping')
        db = client[DB_NAME]
        return db[COLLECTION_NAME]
    except ConnectionFailure as e:
        print(f"MongoDB connection failed: {e}")
        return None
    except Exception as e:
        print(f"An error occurred connecting to MongoDB: {e}")
        return None

def save_chat_history(user_id: str, prompt: str, agent: str, response: str):
    """
    Saves a chat record to the MongoDB database.

    Args:
        user_id (str): Unique identifier for the user session.
        prompt (str): The user's input prompt.
        agent (str): The agent(s) that generated the response.
        response (str): The final generated response.
    """
    collection = get_db_collection()
    if collection is not None:
        chat_record = {
            "user_id": user_id,
            "prompt": prompt,
            "agent": agent,
            "response": response,
            "timestamp": datetime.utcnow()
        }
        try:
            collection.insert_one(chat_record)
        except Exception as e:
            print(f"Failed to save chat history: {e}")

def get_recent_chats(user_id: str, limit: int = 10):
    """
    Retrieves the most recent chat histories for a specific user.

    Args:
        user_id (str): Unique identifier for the user session.
        limit (int): Maximum number of records to return.

    Returns:
        list: A list of chat history documents.
    """
    collection = get_db_collection()
    if collection is not None:
        try:
            # Sort by timestamp descending to get the most recent, then limit
            cursor = collection.find({"user_id": user_id}).sort("timestamp", -1).limit(limit)
            return list(cursor)
        except Exception as e:
            print(f"Failed to retrieve chat history: {e}")
            return []
    return []
