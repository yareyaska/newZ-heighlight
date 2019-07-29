
from flask import render_template ,request ,redirect,url_for
from . import main
from ..requests import get_sources, get_articles, search_articles
from ..models import Source , Articles
#Views


@main.route('/')
def index():
    '''
    View root page.
    ''' 

    title = 'Home'

    business_sources = get_sources('business')

    entertainment_sources = get_sources('entertainment')

    general_sources = get_sources('general')

    sports_sources = get_sources('sports')

    technology_sources = get_sources('technology')

    return render_template('index.html', title=title, business=business_sources, entertainment=entertainment_sources, sports=sports_sources, general=general_sources, technology=technology_sources)


@main.route('/source/<id>')
def source(id):
    '''
    View source page.
    '''
    all_articles = get_articles(id)
    title = f'NewsApp -- {id}'
    id_id = id

    return render_template('articles.html', articles=all_articles, title=title, id_id=id_id)