import cherrypy
from database import Database

# Lowest version of android application that user should have.
APP_VERSION = 1


class Server:
    def __init__(self):
        self.db = Database()

    @cherrypy.expose
    def api(self, path, number=None):

        # Called with `/api/version`
        if path == 'version':
            # Run a query to get most recent batch number
            last_batch_number = self.db.run(('use funsara', 'SELECT MAX(number) FROM batches',))[1][0][0]

            return '''{}"lastBatchNumber": {}, "appVersion": {}{}'''.format('{', last_batch_number, APP_VERSION, '}')

        # Called with `/api/batch?number=%d`
        elif path == 'batch' and number is not None:
            # TODO:
            # Fetch last batch videos.
            # Build JSON array contains JSON object like:
            #   {
            #     "url": URL-OF-PICTURE,
            #     "bluredUrl": URL-OF-BLURED-PICTURE,
            #     "titleOfStory" : TITLE,
            #     "smallDetailOfStory": SMALL-DESCRIPTION,
            #     "fullDetailOfStory": FULL-DESCRIPTION,
            #     "time": LENGTH-OF-VIDEO,
            #     "videoUrl": URL-OF-VIDEO
            #   }
            # for each video in the batch.

            return '/api/batch/?number={}'.format(number)

        # URLs that haven't been handle or requests with bad parameters.
        else:
            return 'Bad Request!'


if __name__ == '__main__':
    cherrypy.quickstart(Server())
