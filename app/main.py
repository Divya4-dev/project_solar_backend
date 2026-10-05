from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.database import get_connection
from app.user_data import UserCreate


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/users")
def create_user(user: UserCreate):
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO USERS (
                NAME,
                MOBILE_NO,
                EMAIL,
                CITY,
                ELECTRICITY_BILL
            )
            VALUES (
                :name,
                :mobile_no,
                :email,
                :city,
                :electricity_bill
            )
        """

        cursor.execute(
            query,
            {
                "name": user.name,
                "mobile_no": user.mobile_no,
                "email": user.email,
                "city": user.city,
                "electricity_bill": user.electricity_bill
            }
        )

        connection.commit()

        return {
            "message": "User created successfully"
        }

    except Exception as e:
        print("DATABASE ERROR:", e)

        if connection:
            connection.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()