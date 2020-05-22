from sqlalchemy import create_engine
from sqlalchemy.schema import Table, MetaData 
import uuid
from db_helper.config import SQLALCHEMY_DATBASE_URI
from datetime import date

def insert(name, email, phone, deadline, services, description):        
    engine = create_engine(SQLALCHEMY_DATBASE_URI)
    meta = MetaData()

    with engine.connect() as conn:
        clients = Table("clients", meta, autoload = True, autoload_with=conn)
        jobs = Table("jobs", meta, autoload = True, autoload_with=conn)
        try:
            conn.execute (
                clients.insert(),
                {
                    "client_id": str(uuid.uuid4()),
                    "full_name": name,
                    "email": email,
                    "phone_no": phone
                }
            )
        except Exception:
            print("email not unique, no action taken")

        conn.execute (
            jobs.insert(),
            {
                "job_id": str(uuid.uuid4()),
                "posted_date": date.today(),
                "deadline": deadline,
                "full_name": name,
                "email": email,
                "phone_no": phone,
                "service_type": services,
                "job_description": description
            }
        )