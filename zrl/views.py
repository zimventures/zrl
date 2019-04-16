from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from zrl.database import db_session
from zrl.models import Mapping

from flask import (
    Blueprint, flash, render_template, request, redirect, abort
)

bp = Blueprint('views', __name__, url_prefix='/')


@bp.route('/zrl_edit/<int:mapping_id>')
def tag_edit(mapping_id):
    try:
        mapping = Mapping.query.filter(Mapping.id == mapping_id).one()
        return render_template('edit.html', mapping=mapping)
    except NoResultFound:
        abort(404)


@bp.route('/<path:path>')
def tag_resolver(path):

    if path.endswith('/'):
        path = path[:-1]

    r = Mapping.query.filter(Mapping.tag == path).first()

    # This tag doesn't exist: flash an error
    if r is None:
        flash(message=f'A mapping does not exist for "{path}"',
              category='error')
        return render_template('index.html')
    else:
        r.hits += 1
        db_session.commit()

    return redirect(r.url)


@bp.route('/', methods=('GET', 'POST'))
def index():

    if request.method == 'POST':

        try:
            m = Mapping(tag=request.form['tag'],
                        url=request.form['url'])
            db_session.add(m)
            db_session.commit()
        except IntegrityError as e:
            flash(message=f'Tag ({request.form["tag"]}) already exists in the database',
                  category='error')

    return render_template('index.html', mappings=Mapping.query.all())
