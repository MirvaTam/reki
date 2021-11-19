from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)
# defines that this file is a blueprint

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.etunimi)


## kaikki vanhat sivut app.route alla
#@app.route('/')
#def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)
    # You also pass the posts object as an argument, which contains the results you got from the database, 
    # this will allow you to access the blog posts in the index.html template.

##  määrää about sivun
#@app.route('/about')
#def about():
    return render_template('about.html')

## yksittäiset id-sivut
#@app.route('/<int:post_id>')
#def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

## luo uusi resepti sivu
#@app.route('/create', methods=('GET', 'POST'))
#def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Reseptin nimi vaaditaan')
        else:
            conn = get_db_connection()
            conn.execute(
                'INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

## muokkaa reseptiä sivu
#@app.route('/<int:id>/edit', methods=('GET', 'POST'))
#def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Reseptin nimi tarvitaan')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

## poista resepti sivu
#@app.route('/<int:id>/delete', methods=('POST',))
#def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" onnistuneesti poistettu'.format(post['title']))
    return redirect(url_for('index'))
