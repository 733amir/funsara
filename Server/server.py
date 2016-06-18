import cherrypy

# Lowest version of android application that user should have.
APP_VERSION = 1


class Server:
    @cherrypy.expose
    def api(self, path, number=None):

        # Called with `/api/version`
        if path == 'version':
            # TODO:
            # Fetch last batch number, Version of application.
            # Build JSON object like:
            # {
            #   "lastBatchNumber": NUMBER-OF-LAST-BATCH,
            #   "appVersion": APPLICATION-VERSION
            # }
            return '/api/version'

        # Called with `/api/batch?number=%d`
        elif path == 'batch':  # TODO Check for `number` variable.
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
