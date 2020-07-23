import urllib.request,json
from app.models import Quote

quote_url = 'http://quotes.stormconsultancy.co.uk/random.json'



def get_quote():
    with urllib.request.urlopen(quote_url) as url:
        quote_response = json.loads(url.read())

        quote_result = None

        if quote_response:
            author = quote_response.get('author')
            quote = quote_response.get('quote')
            quote_result = Quote(author,quote)
          

        return quote_result