#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Пользователь': User, 'Запись': Post}

