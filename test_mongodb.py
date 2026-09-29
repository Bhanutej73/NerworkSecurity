import asyncio
from pymongo import AsyncMongoClient

async def main():
    uri = "mongodb+srv://bhanutej930:<password>@cluster0.wzczjnq.mongodb.net/?appName=Cluster0"
    client = AsyncMongoClient(uri)

    await client.admin.command("ping")
    print("Connected successfully")
    await client.close()

asyncio.run(main())