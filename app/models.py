class Movie:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,title,overview,poster,):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = "https://www.newsbtc.com/wp-content/uploads/2018/08/techanalysis-btc9-700x400.jpg" + poster
        