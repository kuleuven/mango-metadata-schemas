from flask import (
    Flask,
    g,
    redirect,
    request,
    url_for,
    render_template,
    Blueprint,
    session,
    current_app,
)

import bleach
import os

import schema_manager
from schema_manager.editor import metadata_schema_editor_bp
from schema_manager.form import metadata_schema_form_bp
from schema_manager.view import metadata_schema_view_bp

from cache import cache

app = Flask(__name__)
app.secret_key = "HV44H6oH-eKMqJDU0W6Xw6ch_c4wpmDWf5tgD0p-0Gc"
app.config.from_pyfile("config.py")

# Caching, make sure the filesystem dir existsif CACHE_TYPE  is FileSystemCache
if app.config["CACHE_TYPE"] == "FileSystemCache" and not os.path.exists(
    app.config["CACHE_DIR"]
):
    os.makedirs(app.config["CACHE_DIR"])

cache.init_app(app)
with app.app_context():
    cache.clear()


with app.app_context():
    app.register_blueprint(metadata_schema_form_bp)
    app.register_blueprint(metadata_schema_editor_bp)
    app.register_blueprint(metadata_schema_view_bp)


# html and js escape dangerous content
@app.template_filter("bleach_clean")
def bleach_clean(suspect, **kwargs):
    return bleach.clean(suspect, **kwargs)


@app.route("/")
def index():
    return redirect(url_for("metadata_schema_editor_bp.metadata_schemas"))
