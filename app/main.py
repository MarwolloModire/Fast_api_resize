from fastapi import FastAPI, status
from models.models import Feedback, ResponseModel


app = FastAPI()
lst = []


@app.post('/feedback', response_model=ResponseModel,  status_code=status.HTTP_201_CREATED)
async def post_user_feedback(feedback: Feedback) -> Feedback:
    lst.append(feedback)
    return {"message": f"Feedback received. Thank you, {feedback.name}!"}


@app.get('/comments')
async def show_feedback():
    return lst
