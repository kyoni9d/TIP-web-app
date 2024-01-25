from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import EmailHistory
from . import db
import json
import requests

views = Blueprint('views', __name__)


# new

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    try:
        # Выполняем GET-запрос к микросервису на Go
        response = requests.get('http://localhost:8080/')
        # Обрабатываем ответ
        if response.status_code == 200:
            data = response.json()
            email = data.get('email')  # Получаем адрес из ответа
            # Сохраняем сгенерированный email в базу данных
            new_email_history = EmailHistory(user_id=current_user.id, email=email)
            db.session.add(new_email_history)
            db.session.commit()
        else:
            email = 'Ошибка при вызове микросервиса'
    except Exception as e:
        email = f'Произошла ошибка: {e}'
    # Возвращаем историю email адресов на страницу Home
    email_history = EmailHistory.query.filter_by(user_id=current_user.id).all()
    return render_template("home.html", user=current_user, email=email, email_history=email_history)


@views.route('/call_microservice')
@login_required
def call_microservice():
    try:
        # Выполняем GET-запрос к микросервису на Go
        response = requests.get('http://localhost:8080/')
        # Обрабатываем ответ
        if response.status_code == 200:
            data = response.json()
            email = data.get('email')  # Получаем email из ответа
            # Сохраняем сгенерированный email в базу данных
            new_email_history = EmailHistory(user_id=current_user.id, email=email)
            db.session.add(new_email_history)
            db.session.commit()
        else:
            email = 'Ошибка при вызове микросервиса'
    except Exception as e:
        email = f'Произошла ошибка: {e}'

    return jsonify(email=email)

@views.route('/clear_history', methods=['POST'])
@login_required
def clear_history():
    try:
        # Удаляем все записи истории email адресов для текущего пользователя
        EmailHistory.query.filter_by(user_id=current_user.id).delete()
        db.session.commit()
        return jsonify(success=True)
    except Exception as e:
        
        return jsonify(success=False, error=str(e))






