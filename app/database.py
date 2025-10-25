from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from app.config import settings
import logging

logging.basicConfig(level=settings.LEVEL)
logger = logging.getLogger(__name__)

class Database: 
    client: AsyncIOMotorClient = None
    db: AsyncIOMotorDatabase = None

db = Database()

async def connect_to_mongo():
    """Connect to MongoDB"""
    try:
        db.client = AsyncIOMotorClient(settings.MONGODB_URL)
        db.db = db.client[settings.MONGO_DB_NAME]

        await db.client.admin.command('ping')
        logger.info("Successfully connected to MongoDB")

        await create_indexes()
    except Exception as e:
        logger.error(f"Error connecting to MongoDB: {e}")
        raise

async def close_mongo_connection():
    """Close MongoDB connection"""
    if db.client:
        db.client.close()
        logger.info("MongoDB connection closed")

async def create_indexes():
    """Create database indexes"""
    # Users collection
    await db.db.users.create_index("email", unique=True)
    await db.db.susers.create_index("username", unique=True)

    # Article collection
    await db.db.articles.create_index([("title", "text"), ("content", "text")])
    await db.db.articles.create_index("author_id")
    await db.db.articles.create_index("created_at")
    await db.db.articles.create_index("tags")

    logger.info("Database indexes created")

def get_database() -> AsyncIOMotorDatabase:
    """Get database instance"""
    return db.db
