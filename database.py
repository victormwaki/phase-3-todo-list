from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from typing import List
import datetime
from model import Todo

Base = declarative_base()

# SQLAlchemy Database Setup
DATABASE_URL = "sqlite:///todos.db"  # You can change this to another database URL, e.g., PostgreSQL or MySQL
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# SQLAlchemy Table Definition
class TodoModel(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    task = Column(String, nullable=False)
    category = Column(String, nullable=False)
    date_added = Column(DateTime, default=datetime.datetime.now)
    date_completed = Column(DateTime, nullable=True)
    status = Column(Integer, default=1)  # 1 = open, 2 = completed
    position = Column(Integer, nullable=False)

# Create the table
Base.metadata.create_all(engine)

# CRUD Operations
def insert_todo(todo: Todo):
    count = session.query(TodoModel).count()
    new_todo = TodoModel(
        task=todo.task,
        category=todo.category,
        position=count
    )
    session.add(new_todo)
    session.commit()

def get_all_todos() -> List[Todo]:
    todos = session.query(TodoModel).all()
    return [Todo(
        task=todo.task,
        category=todo.category,
        date_added=todo.date_added.isoformat(),
        date_completed=todo.date_completed.isoformat() if todo.date_completed else None,
        status=todo.status,
        position=todo.position
    ) for todo in todos]

def delete_todo(position: int):
    todo_to_delete = session.query(TodoModel).filter_by(position=position).first()
    if todo_to_delete:
        session.delete(todo_to_delete)
        session.commit()
        # Reorder positions
        remaining_todos = session.query(TodoModel).order_by(TodoModel.position).all()
        for idx, todo in enumerate(remaining_todos):
            todo.position = idx
        session.commit()

def update_todo(position: int, task: str = None, category: str = None):
    todo_to_update = session.query(TodoModel).filter_by(position=position).first()
    if todo_to_update:
        if task:
            todo_to_update.task = task
        if category:
            todo_to_update.category = category
        session.commit()

def complete_todo(position: int):
    todo_to_complete = session.query(TodoModel).filter_by(position=position).first()
    if todo_to_complete:
        todo_to_complete.status = 2
        todo_to_complete.date_completed = datetime.datetime.now()
        session.commit()
