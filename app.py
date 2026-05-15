from flask import Flask, render_template, request, redirect, session, flash

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        post = Post(title=title, content=content)
        db.session.add(post)
        db.session.commit()

        flash('Post Created Successfully')
        return redirect('/dashboard')

    return render_template('create_post.html')


# =========================
# EDIT POST
# =========================

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    post = Post.query.get(id)

    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']

        db.session.commit()
        flash('Post Updated')

        return redirect('/dashboard')

    return render_template('edit_post.html', post=post)


# =========================
# DELETE POST
# =========================

@app.route('/delete/<int:id>')
def delete_post(id):
    post = Post.query.get(id)

    db.session.delete(post)
    db.session.commit()

    flash('Post Deleted')
    return redirect('/dashboard')


# =========================
# LOGOUT
# =========================

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged Out')
    return redirect('/')


# =========================
# RUN APP
# =========================

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
