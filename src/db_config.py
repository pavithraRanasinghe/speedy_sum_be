import motor.motor_asyncio

uri = "mongodb+srv://pavithra:Fz4TxZicD9TBOYCN@speedysum.53wqwhq.mongodb.net/"

client = motor.motor_asyncio.AsyncIOMotorClient(uri)
db = client.speedysum