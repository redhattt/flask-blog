#!/usr/bin/env python3

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    url_for
)
from werkzeug.exceptions import abort
from flaskr.db import get_db
from flaskr.templates.__blueprints.auth import login_required

bp = Blueprint('blog', __name__)

@bp.get('/')
def index():
    db = get_db()
    q = """
        select 
            *
        from
            posts as a
        inner join
            users as b
                on a.user_id = b.id
        order by
            create_ts desc
    """
    posts = db.execute(q).fetchall()
    return render_template('blog/index.html', posts = posts)

@bp.route('/create', methods = ('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'insert into posts (title, body, user_id) values (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))
        
    return render_template('blog/create.html')

def get_post(id, check_author = True):
    q = """
        select
            a.*,
            b.username
        from
            posts as a
        inner join
            users as b
                on a.user_id = b.id
        where
            a.id = ?
    """
    post = get_db().execute(q, (id,)).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['user_id'] != g.user['id']:
        abort(403)

    return post


@bp.route('/<int:id>/update', methods = ('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            q = "update posts set title = ?, body = ? where id = ?"

            db.execute(q, (title, body, id))
            db.commit()

            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post = post)

@bp.route('/<int:id>/delete', methods = ('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()

    db.execute("delete from posts where id = ?", (id,))
    db.commit()

    return redirect(url_for('blog.index'))