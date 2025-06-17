from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metaData=MetaData()
db=SQLAlchemy(metadata=metaData)

    